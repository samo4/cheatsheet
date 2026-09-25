# Reference setup, mirroring the root justfile: any crossref-style filters run BEFORE citeproc.
# The bibliography is declared here rather than in AS.md YAML so that standalone chapter builds
# (`just ch FILE`) get citations too. Cite in pandoc syntax: `@ogata2002modern` -> "Ogata (2002)".
# The CSL style is vendored next to this file (same content as
# https://www.zotero.org/styles/harvard-cite-them-right), so builds need no network;
# re-download it if the style changes upstream.
csl := "harvard-cite-them-right.csl"
# citeproc adds NO heading of its own, so the reference list would float untitled;
# reference-section-title gives it a level-1 heading (same level as the chapter titles).
refs_title := "References"

default: as

as:
    pandoc AS.md 00-introduction.md 01-modeling.md 02-state-space.md 03-properties.md 04-transfer-functions.md \
    05-linearization.md 06-discrete.md 07-appendix-A.md 08-appendix-B.md -o AS.pdf --pdf-engine=xelatex -H preamble.tex \
    -V geometry:margin=1in --toc --citeproc --bibliography=references.bib --csl={{csl}} \
    --metadata reference-section-title={{refs_title}}

# Standalone build of any single file: `just ch 03-properties.md` -> 03-properties.pdf
ch file:
    pandoc {{file}} -o {{replace(file, ".md", ".pdf")}} --pdf-engine=xelatex -H preamble.tex \
    -V geometry:margin=1in --citeproc --bibliography=references.bib --csl={{csl}} \
    --metadata reference-section-title={{refs_title}}
