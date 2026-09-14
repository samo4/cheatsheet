default: as

as:
    pandoc AS.md 00-introduction.md 01-modeling.md 02-state-space.md 03-properties.md 04-transfer-functions.md \
    05-linearization.md 06-discrete.md 07-appendix-A.md -o AS.pdf --pdf-engine=xelatex -H preamble.tex \
    -V geometry:margin=1in --toc

# Standalone build of any single file: `just ch 03-properties.md` -> 03-properties.pdf
ch file:
    pandoc {{file}} -o {{replace(file, ".md", ".pdf")}} --pdf-engine=xelatex -H preamble.tex \
    -V geometry:margin=1in
