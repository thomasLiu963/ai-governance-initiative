# Source inventory — NIST sprint

Inspection date: 2026-11-20.  
Workspace: `/Users/thomas/Desktop/ai-governance-initiative`.  
Prior records read, not treated as new measurements: `audits/research-reuse/AUDIT.md` (2026-11-18), `execution/phase1/NIST.md` and `execution/phase1/drafts/nist-metrology-structure.md` (2026-11-19), `execution/phase1/MASTER_RANKING.md`, `PROJECT_CONTEXT.md`, `MASTER_TRACKER.md`, `audits/SUMMARY.md`.

This inventory searches the workspace for D1 and D2 papers, experiments, figures, statistical results, code, and evaluation artifacts. It does not stop at the two research directories. It does not read disks outside this workspace. No experimental result is stated, because none was found.

`execution/sprint4/` contains `california-ai/` only. It has no NIST file.

## What was searched

On 2026-11-20:

- A full filesystem walk of the workspace, including hidden paths, virtual environments, and empty directories.
- A separate listing of regular files whose names end in `pdf`, `docx`, `tex`, `bib`, `csv`, `tsv`, `png`, `svg`, `ipynb`, `R`, `r`, or `xlsx`, excluding virtual environments and `.git`.
- An extension count of every regular file outside `.git`, virtual environments, and `__pycache__`.
- `git log --all` restricted to `research/`, `experiments/`, `references/`, and `evidence/`.
- Text search across Markdown, text, Python, JSON, CSV, and YAML for D1, D2, preference dependence, human judgment, evaluation reliability, Kendall, sample size, and related statistical wording.
- Directory listings and modification times for `research/D1/`, `research/D2/`, `research/incident-evidence/`, `experiments/`, `evidence/`, and `references/`.

The 2026-11-18 research-reuse audit and the 2026-11-19 NIST report both say they did not treat files outside `research/D1/` and `research/D2/` as those tracks. This inventory does that wider workspace search. Files outside `/Users/thomas/Desktop/ai-governance-initiative` were not opened.

## Designated research locations

| Path | Entries | Modification time | Bytes of the directory inode |
| --- | --- | --- | --- |
| `research/D1/` | 0 files, 0 subdirectories | 2026-11-18 13:42:59 | 64 |
| `research/D2/` | 0 files, 0 subdirectories | 2026-11-18 13:42:59 | 64 |
| `research/incident-evidence/` | 0 files, 0 subdirectories | 2026-11-18 13:42:59 | 64 |
| `experiments/` | 0 files, 0 subdirectories | 2026-11-18 13:42:59 | 64 |
| `evidence/` | 0 files, 0 subdirectories | 2026-11-18 13:42:59 | 64 |
| `references/` | 0 files, 0 subdirectories | 2026-11-18 13:42:59 | 64 |

`PROJECT_CONTEXT.md` names D1 and D2 as research tracks and names `experiments/` as the place for raw outputs. It does not describe a paper, a dataset, a metric, or a result. Git history for those four paths is empty: no commit has added a research file there.

## Workspace file census

Outside `.git`, virtual environments, and bytecode caches, the workspace holds 129 Markdown files, 15 Turtle files, 11 Python files, 10 patches, 10 HTML files, 9 text files, 3 JSON files, 2 Jinja templates, 1 PDF, 1 CSV, and 1 `.DS_Store`.

The only PDF is `Statewide opportunity database.pdf`, a California-opportunity extract used by other sprints. The only CSV is `contributions/T004-DPV-Rights/cache/d-csv.csv`, a Data Privacy Vocabulary export whose first rows are purpose and sector terms. There is no `.tex`, `.bib`, `.docx`, `.png`, `.svg`, `.ipynb`, `.R`, or spreadsheet anywhere in that census.

## Artifact classes

| Class | Count in the workspace that belongs to D1 or D2 |
| --- | --- |
| Manuscript, preprint, or internal research note | 0 |
| Dataset or data dictionary for an AI-behavior or human-judgment study | 0 |
| Figure | 0 |
| Result table, interval, sample size, model identifier, or run log | 0 |
| Protocol that states population, assignment, control, baseline, metric, and stopping rule | 0 |
| Author limitation text | 0 |
| License, coauthor approval, or confidentiality record for either track | 0 |
| Code that calculates a D1 or D2 metric | 0 |

Experiments named in the research-reuse audit remain unrun. E-0, the 2026-11-18 directory walk, is the only executed experiment, and it measured directory emptiness. E-1 (recompute a printed number from stored observations), E-2 (protocol completeness), and E-3 (separate results, hypotheses, and limitations) have no inputs and no outputs.

## Files that exist and are not D1 or D2

These files contain numbers or procedures. None is a D1 or D2 study of AI behavior, human judgment, preference dependence, or evaluation reliability. None supplies a sample size, a model identifier, or a human-rating table for those themes.

| Path | What it actually is |
| --- | --- |
| `audits/fcc/sim_revocation.py`, `contributions/C-007-FCC/reproduce.py`, `contributions/C-007-FCC/results/report.txt` | Local assertions about a revocation procedure. The audit summary says the 2026-11-18 run had 9 cases and 0 failed assertions, and that those assertions are local objects. |
| `contributions/T003-DPV-Membership/reproduce.py` and its `results/report.txt` | A SPARQL check of DPV concept membership. |
| `contributions/T004-DPV-Rights/` | A vocabulary comment and the CSV cache above. |
| `contributions/T005-GPC-WPT/local-run/*.json` and the GPC Python support file | A browser run of a Global Privacy Control navigation-cache test. The preference is an HTTP privacy signal, not a model preference. |
| `execution/sprint2/owasp/*/reproduce.py` and `results.txt` | Probes of agent-security specification cases. |
| `audits/owasp-testing/AUDIT.md`, the AITG-APP-10 paragraph | A proposed test-case sentence for the OWASP AI Testing Guide. It was not executed. It cites no local dataset. |
| `audits/research-reuse/AUDIT.md` | The blocked designs RR-1 through RR-5 and the unrun experiments E-1 through E-3. |
| `execution/phase1/NIST.md` | The 2026-11-19 process inspection. It records zero surviving candidates. |
| `execution/phase1/drafts/nist-metrology-structure.md` | An empty YAML shape. Every evidence field is blank on purpose. |

Text mentions of “human judgment,” “preference,” and “Kendall” elsewhere in the workspace are policy drafts, catalog descriptions, or the statement that D1 and D2 are empty. They are not stored measurements.

## Established results

| Class | Count |
| --- | --- |
| Established D1 or D2 result: a number tied to a stored table, a protocol, and an author-stated limitation | 0 |
| Author-labeled D1 or D2 hypothesis | 0 |
| Sentence that could be classified as a result or a hypothesis | 0 |

## Files the user must supply

Place each track’s own files under `research/D1/` or `research/D2/`. A file that stays outside this workspace is still unread. For every track that is supposed to support a metric, supply these ten records. A missing record blocks use of that track.

1. Manuscript or note. Required contents: title, authors, date, version, and a status word the authors wrote: published, accepted, submitted, preprint, unpublished, or internal.
2. Locator or quotation permission. If the manuscript is public, the stable locator. If it is unpublished, a sentence that says whether external quotation is permitted.
3. License notice and the name of the rights holder.
4. Coauthor list and a written decision from each living author whose text or numbers would be reused, covering local reanalysis and a later public submission.
5. Confidentiality record: public, embargoed until a stated date, confidential, or restricted. If human-subjects or institutional rules apply, the record names them.
6. Dataset description for every dataset: filename, row or item count, schema, license, the authors’ collection method, and whether the file may leave this machine. Include the data file itself when the protocol needs it.
7. Stored result for every reported number: the table or log, the metric definition, the sample size, the model or system identifier, the run date, the baseline, and the control condition.
8. Protocol sufficient to recompute the stored numbers from stored observations, without a new model call.
9. The authors’ limitation text, kept verbatim.
10. The authors’ own split between a reported result and a hypothesis. A sentence they did not split stays “not classifiable.”

NIST’s public submission adds three further records those ten do not satisfy: one or two references about the metric itself, an implementation that calculates that metric and is already released or merged, and a contact email that will be published. Those gates are recorded in `EVIDENCE_GAPS.md`. They are not a reason to draft a metric before the ten records exist.
