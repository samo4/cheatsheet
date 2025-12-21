
# The order of filters matters in Pandoc. pandoc-crossref should run before citeproc:

# Build all PDFs
build: pandoc simulations calculus modern

# Individual targets
pandoc:
    pandoc pandoc.md -o pandoc.pdf --pdf-engine=xelatex -V geometry:margin=1in --number-sections --toc \
    --filter pandoc-crossref --citeproc -V colorlinks=true -V linkcolor=red -V citecolor=blue -V urlcolor=red

simulations:
    pandoc SIMULATIONS.md -o simulations.pdf --pdf-engine=xelatex -V geometry:margin=1in

calculus:
    pandoc calculus.md -o calculus.pdf --pdf-engine=xelatex -V geometry:margin=1in --filter pandoc-crossref --number-sections \
    --toc -V colorlinks=true -V linkcolor=blue -V citecolor=blue -V urlcolor=blue

modern:
    pandoc modern-c.md -o modern-c.pdf --pdf-engine=xelatex --citeproc -V geometry:margin=1in -V colorlinks=true -V linkcolor=blue -V citecolor=blue -V urlcolor=blue

as:
    pandoc AS.md -o AS.pdf --pdf-engine=xelatex -V geometry:margin=1in

meas:
    pandoc MEASUREMENTS.md -o MEASUREMENTS.pdf --pdf-engine=xelatex -V geometry:margin=1in --filter pandoc-crossref \
    --number-sections -V colorlinks=true -V linkcolor=blue -V citecolor=blue -V urlcolor=blue

# --filter pandoc-crossref -V colorlinks=true -V linkcolor=blue -V citecolor=blue
