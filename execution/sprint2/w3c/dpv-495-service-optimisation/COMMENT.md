# Comment for w3c-cg/dpv issue 495

Not posted. One comment on the existing issue. No pull request, and no edit of generated Turtle, HTML, or CSV.

The person who posts this is responsible for every sentence. An LLM drafted it from the files named below. Keep the disclosure line.

## Body

```markdown
The stale scope note is still present. I re-read it on 2026-11-19 at these commits:

- `dev` `aff91c294b105d9a261ea8622350b0fc7ef0e293`, `2.4-dev/dpv/modules/purposes.ttl` line 1606, and `2.4-dev/dpv/modules/purposes-owl.ttl` line 1496
- `master` `689d32c0f7c571d32f7f8635ae548fcc1c3ff695`, `2.3/dpv/modules/purposes.ttl` line 1606

In both serialisations the parent is ServiceManagement (`skos:broader` in the RDFS+SKOS file, `rdfs:subClassOf` in the OWL file). The note still says "Subclass of ServiceProvision since optimisation is usually considered part of providing services".

ServiceProvision's own scope note, line 1645 of the same RDFS file on both branches, says that concept was narrowed in v2.3 and should not be used for management or other non-provision purposes.

Please replace the ServiceOptimisation scope note with:

"Part of ServiceManagement: optimisation is one of the activities of managing a service."

That is the first option already stated on this issue. I am not sending a pull request. The generated files should be updated from the spreadsheet.

LLM use: an LLM drafted this comment from those files and from this issue. The person who posts it is responsible for the sentences.
```
