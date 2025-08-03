
# The order of filters matters in Pandoc. pandoc-crossref should run before citeproc:

build: 
    pandoc pandoc.md -o pandoc.pdf --pdf-engine=xelatex -V geometry:margin=1in --number-sections --toc --filter pandoc-crossref --citeproc
	
# --filter pandoc-crossref -V colorlinks=true -V linkcolor=blue -V citecolor=blue
