#!/usr/bin/env python3
"""Check dpv:RightsFulfilment parents for issue #486.

Reads pinned public files from w3c-cg/dpv. No model API.
Install: python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
Run:    .venv/bin/python reproduce.py
"""

from __future__ import annotations

import hashlib
import sys
import urllib.request
from pathlib import Path

from rdflib import Graph, Literal, Namespace, URIRef
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
    "m-owl": (MASTER, "2.3/dpv/dpv-owl.ttl"),
    "m-html": (MASTER, "2.3/dpv/modules/purposes.html"),
    "d-dpv": (DEV, "2.4-dev/dpv/dpv.ttl"),
    "d-owl": (DEV, "2.4-dev/dpv/dpv-owl.ttl"),
    "d-csv": (DEV, "code/vocab_csv/Purpose.csv"),
    "d-html": (DEV, "2.4-dev/dpv/modules/purposes.html"),
}

DPV = Namespace("https://w3id.org/dpv#")
DPVO = Namespace("https://w3id.org/dpv/owl#")

TERMS = [
    DPV.RightsFulfilment,
    DPV.LegalObligation,
    DPV.LegalBasis,
    DPV.Purpose,
    DPV.LegalCompliance,
    DPV.FulfilmentOfObligation,
    DPV.FulfilmentOfContractualObligation,
    DPV.ProtectionOfIPR,
    DPV.OrganisationComplianceManagement,
    DPV.hasPurpose,
    DPV.hasLegalBasis,
]


def fetch(name: str, commit: str, path: str) -> Path:
    CACHE.mkdir(parents=True, exist_ok=True)
    suffix = Path(path).suffix or ".bin"
    dest = CACHE / f"{name}{suffix}"
    if not dest.exists():
        url = RAW.format(commit=commit, path=path)
        print(f"GET {url}", file=sys.stderr)
        urllib.request.urlretrieve(url, dest)
    return dest


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def local(node) -> str:
    text = str(node)
    return text.rsplit("#", 1)[-1] if "#" in text else text.rsplit("/", 1)[-1]


def load(name: str) -> Graph:
    g = Graph()
    g.parse(CACHE / f"{name}.ttl", format="turtle")
    return g


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    FIX.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []

    def emit(text: str = "") -> None:
        lines.append(text)
        print(text)

    paths = {}
    for name, (commit, path) in FILES.items():
        dest = fetch(name, commit, path)
        paths[name] = dest
        emit(f"FILE {name} {path} commit {commit[:12]} sha256 {sha256(dest)} bytes {dest.stat().st_size}")

    for label, name in (("2.3", "m-dpv"), ("2.4-dev", "d-dpv")):
        g = load(name)
        emit(f"\n== {label} purpose parent guard ==")
        bad = list(g.query(
            """
            PREFIX dpv: <https://w3id.org/dpv#>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT ?s ?parent ?ptype WHERE {
              ?s a dpv:Purpose ; skos:broader ?parent .
              FILTER (?parent != dpv:Purpose)
              FILTER NOT EXISTS { ?parent a dpv:Purpose }
              OPTIONAL { ?parent a ?ptype FILTER (?ptype != <http://www.w3.org/2000/01/rdf-schema#Class> && ?ptype != <http://www.w3.org/2004/02/skos/core#Concept>) }
            } ORDER BY ?s ?parent ?ptype
            """
        ))
        emit(f"  purpose whose broader target is not a purpose and is not dpv:Purpose: {len({str(s)+str(p) for s,p,_ in bad})} pairs")
        for s, parent, ptype in bad:
            emit(f"  {local(s)} broader {local(parent)} parent-type {local(ptype) if ptype else ''}")

        emit(f"  children of FulfilmentOfObligation:")
        for s in sorted(g.subjects(SKOS.broader, DPV.FulfilmentOfObligation), key=local):
            emit(f"    {local(s)} type={[local(t) for t in g.objects(s, RDF.type) if 'w3.org/200' not in str(t)]}")
        emit(f"  children of LegalCompliance: {[local(s) for s in g.subjects(SKOS.broader, DPV.LegalCompliance)] or '(none)'}")
        emit(f"  children of RightsFulfilment: {[local(s) for s in g.subjects(SKOS.broader, DPV.RightsFulfilment)] or '(none)'}")
        emit(f"  children of LegalObligation: {[local(s) for s in g.subjects(SKOS.broader, DPV.LegalObligation)]}")

    g = load("m-dpv")
    emit("\n== definitions and scope notes (2.3) ==")
    for term in TERMS:
        if term in (DPV.hasPurpose, DPV.hasLegalBasis):
            continue
        definition = next(g.objects(term, SKOS.definition), None)
        note = next(g.objects(term, SKOS.scopeNote), None)
        broader = [local(o) for o in g.objects(term, SKOS.broader)]
        types = [local(o) for o in g.objects(term, RDF.type) if "w3.org/200" not in str(o)]
        schemes = [local(o) for o in g.objects(term, SKOS.inScheme)]
        emit(f"{local(term)}")
        emit(f"  type {types} broader {broader} scheme {schemes}")
        emit(f"  definition: {definition}")
        if note:
            emit(f"  scope: {note}")

    emit("\n== OWL 2.3 subclass chain ==")
    owl = load("m-owl")
    rf = DPVO.RightsFulfilment
    emit(f"  type {[local(o) for o in owl.objects(rf, RDF.type)]}")
    emit(f"  subClassOf {[local(o) for o in owl.objects(rf, RDFS.subClassOf)]}")
    emit(f"  skos:broader any {any(owl.triples((rf, SKOS.broader, None)))}")
    path = list(owl.query(
        """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?o WHERE {
          <https://w3id.org/dpv/owl#RightsFulfilment> rdfs:subClassOf+ ?o .
        }
        """
    ))
    emit("  subClassOf+ " + ", ".join(sorted(local(o) for (o,) in path)))
    disjoint = list(owl.triples((None, OWL.disjointWith, None)))
    emit(f"  owl:disjointWith triples {len(disjoint)}")
    direct = [local(o) for o in owl.objects(DPVO.Purpose, RDFS.subClassOf)]
    emit(f"  Purpose direct subClassOf {direct or '(none)'}")
    toward = list(owl.query(
        """
        SELECT ?mid WHERE {
          <https://w3id.org/dpv/owl#Purpose> <http://www.w3.org/2000/01/rdf-schema#subClassOf>+ ?mid .
          FILTER EXISTS {
            ?mid <http://www.w3.org/2000/01/rdf-schema#subClassOf>* <https://w3id.org/dpv/owl#LegalBasis>
          }
        }
        """
    ))
    emit("  Purpose subClassOf+ nodes that can reach LegalBasis: " + (", ".join(sorted(local(m) for (m,) in toward)) or "(none)"))
    entailed = list(owl.query(
        """
        ASK {
          <https://w3id.org/dpv/owl#RightsFulfilment> <http://www.w3.org/2000/01/rdf-schema#subClassOf>+ <https://w3id.org/dpv/owl#LegalBasis> .
          <https://w3id.org/dpv/owl#RightsFulfilment> a <https://w3id.org/dpv/owl#Purpose> .
        }
        """
    ))
    emit(f"  RightsFulfilment is typed Purpose and is a subclass of LegalBasis: {bool(entailed)}")

    emit("\n== dev Purpose.csv ParentTerm ==")
    csv_text = paths["d-csv"].read_text()
    header = csv_text.splitlines()[0]
    emit(f"  header: {header}")
    for line in csv_text.splitlines():
        if line.startswith("RightsFulfilment,") or line.startswith("LegalCompliance,") or line.startswith("FulfilmentOfObligation,") or line.startswith("ProtectionOfIPR,") or line.startswith("FulfilmentOfContractualObligation,"):
            cols = line.split(",")
            emit(f"  {cols[0]} ParentTerm={cols[3]} ParentType={cols[4]}")

    emit("\n== generated HTML object-of-relation ==")
    for label, key in (("2.3", "m-html"), ("2.4-dev", "d-html")):
        html = paths[key].read_text(errors="replace")
        for anchor in ("RightsFulfilment", "LegalCompliance", "FulfilmentOfObligation"):
            start = html.find(f'id="{anchor}"')
            chunk = html[start:start + 4000]
            relation = "hasLegalBasis" if "dpv#hasLegalBasis" in chunk or "hasLegalBasis" in chunk else ""
            purpose = "hasPurpose" if "hasPurpose" in chunk else ""
            parent = "LegalObligation" if "LegalObligation" in chunk[:1500] else ""
            emit(f"  {label} {anchor}: hasLegalBasis={('hasLegalBasis' in chunk)} hasPurpose={('hasPurpose' in chunk)} snippet_has_LegalObligation_parent={'#LegalObligation' in chunk[:1800]}")

    write_fixture(g)
    text = "\n".join(lines) + "\n"
    (OUT / "report.txt").write_text(text)
    emit(f"\nWROTE {OUT / 'report.txt'}")


def write_fixture(g: Graph) -> None:
    preds = {RDF.type, SKOS.broader, SKOS.definition, SKOS.scopeNote, SKOS.inScheme, SKOS.prefLabel}
    fg = Graph()
    for term in TERMS:
        for p, o in g.predicate_objects(term):
            if p in preds or p in (URIRef("http://purl.org/dc/dcam/rangeIncludes"), URIRef("https://schema.org/rangeIncludes")):
                fg.add((term, p, o))
    fg.bind("dpv", DPV)
    fg.bind("skos", SKOS)
    fg.bind("rdfs", RDFS)
    fg.bind("rdf", RDF)
    path = FIX / "rights.ttl"
    fg.serialize(path, format="turtle")
    check = Graph()
    check.parse(path)
    assert (DPV.RightsFulfilment, SKOS.broader, DPV.LegalObligation) in check
    assert (DPV.LegalObligation, RDF.type, DPV.LegalBasis) in check
    assert (DPV.LegalCompliance, SKOS.broader, DPV.FulfilmentOfObligation) in check
    assert (DPV.RightsFulfilment, RDF.type, DPV.Purpose) in check


if __name__ == "__main__":
    main()
