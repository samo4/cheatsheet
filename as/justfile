default: as

as:
    pandoc AS.md 01-modeling.md 02-state-space.md 03-properties.md 04-transfer-functions.md 05-linearization.md 06-discrete.md 07-appendix-A.md 08-appendix-B.md -o AS.pdf --pdf-engine=xelatex -H preamble.tex -V geometry:margin=1in --toc

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
    pandoc 07-appendix-A.md -o 07-appendix-A.pdf --pdf-engine=xelatex -H preamble.tex -V geometry:margin=1in

ch7a:
    pandoc 07a-exchange-eigenvectors.md -o 07a-exchange-eigenvectors.pdf --pdf-engine=xelatex -H preamble.tex -V geometry:margin=1in

ch8:
    pandoc 08-appendix-B.md -o 08-appendix-B.pdf --pdf-engine=xelatex -H preamble.tex -V geometry:margin=1in
