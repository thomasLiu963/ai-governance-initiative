#!/usr/bin/env python3
"""Reproduce DPV concept-membership queries for issue #484.

Reads pinned public Turtle from the w3c-cg/dpv repository. No model API.
Install: python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
Run:    .venv/bin/python reproduce.py
"""

from __future__ import annotations

import hashlib
import sys
import urllib.request
from pathlib import Path

from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import OWL, RDF, RDFS, SKOS

ROOT = Path(__file__).resolve().parent
CACHE = ROOT / "cache"
FIX = ROOT / "fixture"
OUT = ROOT / "results"

MASTER = "689d32c0f7c571d32f7f8635ae548fcc1c3ff695"
DEV = "aff91c294b105d9a261ea8622350b0fc7ef0e293"
RAW = "https://raw.githubusercontent.com/w3c-cg/dpv/{commit}/{path}"

FILES = {
    "m-dpv": (MASTER, "2.3/dpv/dpv.ttl"),
    "m-pd": (MASTER, "2.3/pd/pd.ttl"),
    "m-owl": (MASTER, "2.3/dpv/dpv-owl.ttl"),
    "m-pd-owl": (MASTER, "2.3/pd/pd-owl.ttl"),
    "d-dpv": (DEV, "2.4-dev/dpv/dpv.ttl"),
    "d-pd": (DEV, "2.4-dev/pd/pd.ttl"),
    "d-pd-owl": (DEV, "2.4-dev/pd/pd-owl.ttl"),
}

OWL_SUBCLASS = URIRef("http://www.w3.org/2002/07/owl#subClassOf")
DPV = Namespace("https://w3id.org/dpv#")
PD = Namespace("https://w3id.org/dpv/pd#")
DPVO = Namespace("https://w3id.org/dpv/owl#")
PDO = Namespace("https://w3id.org/dpv/pd/owl#")

BLOOD = PD.BloodType
SPECIAL = DPV.SpecialCategoryPersonalData
PERSONAL = DPV.PersonalData
SCHEME = PD["specialcategory-classes"]


def fetch(name: str, commit: str, path: str) -> Path:
    CACHE.mkdir(parents=True, exist_ok=True)
    dest = CACHE / f"{name}.ttl"
    if not dest.exists():
        url = RAW.format(commit=commit, path=path)
        print(f"GET {url}", file=sys.stderr)
        urllib.request.urlretrieve(url, dest)
    return dest


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def load(*names: str) -> Graph:
    g = Graph()
    for name in names:
        g.parse(CACHE / f"{name}.ttl", format="turtle")
    return g


def local(node) -> str:
    text = str(node)
    return text.rsplit("#", 1)[-1] if "#" in text else text.rsplit("/", 1)[-1]


def ask(g: Graph, query: str) -> bool:
    return bool(g.query(ask_query(query)))


def ask_query(body: str) -> str:
    return "ASK { " + body + " }"


def rows(g: Graph, query: str):
    return list(g.query(query))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    FIX.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []

    def emit(text: str = "") -> None:
        lines.append(text)
        print(text)

    for name, (commit, path) in FILES.items():
        dest = fetch(name, commit, path)
        emit(f"FILE {name} {path} commit {commit[:12]} sha256 {sha256(dest)} bytes {dest.stat().st_size}")

    rdfs = load("m-dpv", "m-pd")
    pd = load("m-pd")
    owl = load("m-owl", "m-pd-owl")
    dev = load("d-dpv", "d-pd")

    emit("\n== BloodType direct triples (RDFS+SKOS, 2.3 dpv+pd) ==")
    for p in (RDF.type, SKOS.broader, RDFS.subClassOf, SKOS.inScheme):
        objs = sorted(local(o) for o in rdfs.objects(BLOOD, p))
        emit(f"  {p.n3()} -> {objs}")

    emit("\n== broader chain from BloodType (shortest hop) ==")
    seen = {BLOOD: 0}
    frontier = [BLOOD]
    while frontier:
        current = frontier.pop(0)
        for mid in sorted(rdfs.objects(current, SKOS.broader), key=local):
            if mid in seen:
                continue
            seen[mid] = seen[current] + 1
            frontier.append(mid)
            types = sorted(
                local(t) for t in rdfs.objects(mid, RDF.type)
                if str(t).startswith("https://w3id.org/dpv")
            )
            direct = sorted(local(o) for o in rdfs.objects(mid, SKOS.broader))
            emit(f"  hop {seen[mid]} {local(mid)} dpv-type={types} broader={direct}")

    emit("\n== ASK on published 2.3 RDFS+SKOS (dpv.ttl + pd.ttl) ==")
    checks = {
        "type special": f"<{BLOOD}> a <{SPECIAL}>",
        "type personal": f"<{BLOOD}> a <{PERSONAL}>",
        "direct broader special": f"<{BLOOD}> <{SKOS.broader}> <{SPECIAL}>",
        "path broader special": f"<{BLOOD}> <{SKOS.broader}>+ <{SPECIAL}>",
        "path broader personal": f"<{BLOOD}> <{SKOS.broader}>+ <{PERSONAL}>",
        "direct subclass special": f"<{BLOOD}> <{RDFS.subClassOf}> <{SPECIAL}>",
        "path subclass special": f"<{BLOOD}> <{RDFS.subClassOf}>+ <{SPECIAL}>",
        "in scheme": f"<{BLOOD}> <{SKOS.inScheme}> <{SCHEME}>",
        "predicate owl:subClassOf exists": f"<{BLOOD}> <http://www.w3.org/2002/07/owl#subClassOf>+ <{SPECIAL}>",
    }
    for label, body in checks.items():
        emit(f"  {label}: {ask(rdfs, body)}")

    emit("\n== ASK on published 2.3 OWL (dpv-owl.ttl + pd-owl.ttl) ==")
    blood_o = PDO.BloodType
    special_o = DPVO.SpecialCategoryPersonalData
    personal_o = DPVO.PersonalData
    owl_checks = {
        "type special (owl IRI)": f"<{blood_o}> a <{special_o}>",
        "type personal (owl IRI)": f"<{blood_o}> a <{personal_o}>",
        "skos:broader any": f"<{blood_o}> <{SKOS.broader}> ?o",
        "path rdfs:subClassOf special": f"<{blood_o}> <{RDFS.subClassOf}>+ <{special_o}>",
        "path rdfs:subClassOf personal": f"<{blood_o}> <{RDFS.subClassOf}>+ <{personal_o}>",
        "in scheme": f"<{blood_o}> <{SKOS.inScheme}> ?o",
        "owl:subClassOf any": f"<{blood_o}> <{OWL_SUBCLASS}> ?o",
        "unversioned dpv IRI type": f"<{BLOOD}> a <{SPECIAL}>",
    }
    for label, body in owl_checks.items():
        emit(f"  {label}: {ask(owl, body)}")

    emit("\n== same ASKs on 2.4-dev RDFS ==")
    for label, body in checks.items():
        emit(f"  {label}: {ask(dev, body)}")

    emit("\n== special-category sets in pd.ttl alone ==")
    typed = set(pd.subjects(RDF.type, SPECIAL))
    scheme = set(pd.subjects(SKOS.inScheme, SCHEME))
    walked = set(x for (x,) in pd.query(f"SELECT ?s WHERE {{ ?s <{SKOS.broader}>+ <{SPECIAL}> }}"))
    direct = set(pd.subjects(SKOS.broader, SPECIAL))

    def names(items) -> str:
        return ", ".join(sorted(local(x) for x in items)) or "(none)"

    emit(f"  rdf:type count {len(typed)}")
    emit(f"  inScheme count {len(scheme)}")
    emit(f"  broader+ count {len(walked)}")
    emit(f"  direct broader count {len(direct)}")
    emit(f"  type minus path: {names(typed - walked)}")
    emit(f"  path minus type: {names(walked - typed)}")
    emit(f"  type minus scheme: {names(typed - scheme)}")
    emit(f"  scheme minus type: {names(scheme - typed)}")
    emit(f"  typed but not direct child ({len(typed - direct)}): {names(typed - direct)}")

    emit("\n== personal-data type versus broader path, in pd.ttl ==")
    typed_pd = set(pd.subjects(RDF.type, PERSONAL))
    walked_pd = set(x for (x,) in pd.query(f"SELECT ?s WHERE {{ ?s <{SKOS.broader}>+ <{PERSONAL}> }}"))
    emit(f"  rdf:type PersonalData {len(typed_pd)}")
    emit(f"  broader+ PersonalData {len(walked_pd)}")
    emit(f"  type minus path ({len(typed_pd - walked_pd)}): {names(typed_pd - walked_pd)}")
    emit(f"  path minus type ({len(walked_pd - typed_pd)}): {names(walked_pd - typed_pd)}")

    emit("\n== dpv.ttl alone, classes with prefLabel ==")
    core = load("m-dpv")
    core_classes = {t for t in core.subjects(SKOS.prefLabel, None) if (t, RDF.type, RDFS.Class) in core}

    def has_pred(pred, pool, graph):
        return sum(1 for t in pool if (t, pred, None) in graph)

    emit(
        f"  classes {len(core_classes)} broader {has_pred(SKOS.broader, core_classes, core)} "
        f"subClassOf {has_pred(RDFS.subClassOf, core_classes, core)}"
    )

    emit("\n== pd:ProfessionalExperience uses a different PersonalData IRI ==")
    experience = URIRef("https://w3id.org/dpv/pd#ProfessionalExperience")
    dangling = URIRef("https://w3id.org/dpv/pd#PersonalData")
    for label, graph in (("2.3", pd), ("2.4-dev", load("d-pd"))):
        types = sorted(str(o) for o in graph.objects(experience, RDF.type) if "w3id.org/dpv" in str(o))
        defined = any(graph.triples((dangling, SKOS.prefLabel, None)))
        reaches = ask(graph, f"<{experience}> <{SKOS.broader}>+ <{PERSONAL}>")
        emit(f"  {label} types {types}")
        emit(f"  {label} pd:PersonalData has a prefLabel: {defined}; broader+ reaches dpv:PersonalData: {reaches}")

    emit("\n== predicate counts, subjects with skos:prefLabel ==")
    for label, graph in (("rdfs-2.3", rdfs), ("owl-2.3", owl)):
        terms = set(graph.subjects(SKOS.prefLabel, None))
        classes = {t for t in terms if (t, RDF.type, RDFS.Class) in graph or (t, RDF.type, OWL.Class) in graph}
        props = {t for t in terms if (t, RDF.type, RDF.Property) in graph}
        def has(pred, pool):
            return sum(1 for t in pool if (t, pred, None) in graph)
        emit(
            f"  {label} terms {len(terms)} classes {len(classes)} properties {len(props)} "
            f"class broader {has(SKOS.broader, classes)} class subClassOf {has(RDFS.subClassOf, classes)} "
            f"prop broader {has(SKOS.broader, props)} owl:subClassOf triples {sum(1 for _ in graph.triples((None, OWL_SUBCLASS, None)))} "
            f"skos:broader triples {sum(1 for _ in graph.triples((None, SKOS.broader, None)))}"
        )

    emit("\n== class subClassOf targets that are not also skos:broader targets ==")
    mismatch = rows(
        rdfs,
        """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT ?s ?o WHERE {
          ?s a rdfs:Class ; rdfs:subClassOf ?o .
          FILTER NOT EXISTS { ?s skos:broader ?o }
          FILTER EXISTS { ?s skos:prefLabel ?lab }
        } ORDER BY ?s
        """,
    )
    emit(f"  count {len(mismatch)}")
    for s, o in mismatch:
        broader = sorted(local(b) for b in rdfs.objects(s, SKOS.broader))
        emit(f"  {local(s)} subClassOf {local(o)} broader {broader or '(none)'}")

    emit("\n== imports and disjointness (2.3 dpv+pd and owl) ==")
    for label, graph in (("rdfs", rdfs), ("owl", owl)):
        imports = list(graph.objects(None, OWL.imports))
        disjoint = list(graph.triples((None, OWL.disjointWith, None)))
        emit(f"  {label} owl:imports {len(imports)} owl:disjointWith {len(disjoint)}")

    write_fixture(rdfs, owl)
    text = "\n".join(lines) + "\n"
    (OUT / "report.txt").write_text(text)
    emit(f"\nWROTE {OUT / 'report.txt'}")


def write_fixture(rdfs: Graph, owl: Graph) -> None:
    """Minimal excerpt. Triples are copied from the parsed publication, not rewritten by hand."""
    keep_rdfs = {
        BLOOD,
        PD.MedicalHealth,
        PD.External,
        SPECIAL,
        DPV.SensitivePersonalData,
        PERSONAL,
        DPV.Data,
        SCHEME,
    }
    # Include every broader target of the kept PD/DPV concepts so the path is complete.
    changed = True
    while changed:
        changed = False
        for s in list(keep_rdfs):
            for o in rdfs.objects(s, SKOS.broader):
                if isinstance(o, URIRef) and o not in keep_rdfs and str(o).startswith("https://w3id.org/dpv"):
                    keep_rdfs.add(o)
                    changed = True
    preds = {RDF.type, SKOS.broader, RDFS.subClassOf, SKOS.inScheme, SKOS.prefLabel, SKOS.definition}
    fg = Graph()
    for s in keep_rdfs:
        for p, o in rdfs.predicate_objects(s):
            if p in preds and (isinstance(o, URIRef) and (o in keep_rdfs or str(o).startswith("http://www.w3.org/")) or p == SKOS.prefLabel or p == SKOS.definition):
                if p in (SKOS.prefLabel, SKOS.definition) or o in keep_rdfs or str(o).startswith("http://www.w3.org/"):
                    fg.add((s, p, o))
    fg.bind("dpv", DPV)
    fg.bind("pd", PD)
    fg.bind("skos", SKOS)
    fg.bind("rdfs", RDFS)
    fg.bind("rdf", RDF)
    rdfs_path = FIX / "membership-rdfs.ttl"
    fg.serialize(rdfs_path, format="turtle")

    keep_owl = {URIRef(str(n).replace("https://w3id.org/dpv#", "https://w3id.org/dpv/owl#").replace("https://w3id.org/dpv/pd#", "https://w3id.org/dpv/pd/owl#")) for n in keep_rdfs}
    og = Graph()
    for s in keep_owl:
        for p, o in owl.predicate_objects(s):
            if p in preds:
                og.add((s, p, o))
    og.bind("dpv-owl", DPVO)
    og.bind("pd-owl", PDO)
    og.bind("skos", SKOS)
    og.bind("rdfs", RDFS)
    og.bind("rdf", RDF)
    og.bind("owl", OWL)
    owl_path = FIX / "membership-owl.ttl"
    og.serialize(owl_path, format="turtle")

    # Confirm the fixture preserves the published answers.
    fg2 = Graph()
    fg2.parse(rdfs_path)
    assert (BLOOD, RDF.type, SPECIAL) in fg2
    assert (BLOOD, SKOS.broader, SPECIAL) not in fg2
    assert ask(fg2, f"<{BLOOD}> <{SKOS.broader}>+ <{SPECIAL}>")
    assert not ask(fg2, f"<{BLOOD}> <{RDFS.subClassOf}>+ <{SPECIAL}>")
    og2 = Graph()
    og2.parse(owl_path)
    assert ask(og2, f"<{PDO.BloodType}> <{RDFS.subClassOf}>+ <{DPVO.SpecialCategoryPersonalData}>")
    assert not ask(og2, f"<{PDO.BloodType}> <{SKOS.broader}> ?o")


if __name__ == "__main__":
    main()
