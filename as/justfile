# Build AS PDFs from within this folder.
#   just           -> full document (as/AS.pdf)
#   just ch1..ch7  -> single chapter (as/01-*.pdf)
# Shared LaTeX preamble: as/preamble.tex (via -H).
default: as

as:
    pandoc AS.md 01-modeling.md 02-state-space.md 03-properties.md 04-transfer-functions.md 05-linearization.md 06-discrete.md 07-appendix.md -o AS.pdf --pdf-engine=xelatex -H preamble.tex -V geometry:margin=1in --toc

ch1:
    pandoc 01-modeling.md -o 01-modeling.pdf --pdf-engine=xelatex -H preamble.tex -V geometry:margin=1in

ch2:
    pandoc 02-state-space.md -o 02-state-space.pdf --pdf-engine=xelatex -H preamble.tex -V geometry:margin=1in

ch3:
    pandoc 03-properties.md -o 03-properties.pdf --pdf-engine=xelatex -H preamble.tex -V geometry:margin=1in

ch4:
    pandoc 04-transfer-functions.md -o 04-transfer-functions.pdf --pdf-engine=xelatex -H preamble.tex -V geometry:margin=1in

ch5:
    pandoc 05-linearization.md -o 05-linearization.pdf --pdf-engine=xelatex -H preamble.tex -V geometry:margin=1in

ch6:
    pandoc 06-discrete.md -o 06-discrete.pdf --pdf-engine=xelatex -H preamble.tex -V geometry:margin=1in

ch7:
    pandoc 07-appendix.md -o 07-appendix.pdf --pdf-engine=xelatex -H preamble.tex -V geometry:margin=1in

ko23:
    pandoc AS-kolokvij-2023-11-24.md -o AS-kolokvij-2023-11-24.pdf --pdf-engine=xelatex -H preamble.tex -V geometry:margin=1in

ko24:
    pandoc AS-kolokvij-2024-11-22.md -o AS-kolokvij-2024-11-22.pdf --pdf-engine=xelatex -H preamble.tex -V geometry:margin=1in
