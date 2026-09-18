
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
    cd as && just as

control:
    pandoc control.md -o control.pdf --pdf-engine=xelatex -V geometry:margin=1in

meas:
    pandoc measurements-a-nigh-time-story.md -o MEASUREMENTS.pdf --pdf-engine=xelatex -V geometry:margin=1in --filter pandoc-crossref \
    --number-sections -V colorlinks=true -V linkcolor=blue -V citecolor=blue -V urlcolor=blue

magnetics:
    pandoc magnetics.md -o MAGNETICS.pdf  --pdf-engine=xelatex -V geometry:margin=1in --number-sections \
    --filter pandoc-crossref --citeproc -V colorlinks=true -V linkcolor=red -V citecolor=blue -V urlcolor=red

# Lens-current stability for a three-lens SEM column. `sem` builds the note;
# `sem-numbers`, `sem-compare` and `sem-markdown` run the script behind its tables.
sem:
    pandoc sem-lens-current-stability.md -o sem-lens-current-stability.pdf --pdf-engine=xelatex \
    -V geometry:margin=1in --number-sections

sem-numbers:
    python python/sem_lens_current_stability.py

sem-compare:
    python python/sem_lens_current_stability.py --compare

sem-markdown:
    python python/sem_lens_current_stability.py --markdown

# The 2 A supply that has to hit those numbers: architecture and drift budget.
sem-supply:
    pandoc sem-lens-current-supply.md -o sem-lens-current-supply.pdf --pdf-engine=xelatex \
    -V geometry:margin=1in --number-sections

supply-numbers:
    python python/sem_lens_supply_budget.py

supply-markdown:
    python python/sem_lens_supply_budget.py --markdown

supply-thermal:
    python python/sem_lens_supply_budget.py --thermal

supply-trade:
    python python/sem_lens_supply_budget.py --trade

supply-parts:
    python python/sem_lens_supply_budget.py --parts

supply-sums:
    python python/sem_lens_supply_budget.py --sums

supply-verify:
    python python/sem_lens_supply_budget.py --verify

# --filter pandoc-crossref -V colorlinks=true -V linkcolor=blue -V citecolor=blue
