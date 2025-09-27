# DSCI-511 Project

Collaborative repo for our DSCI 511 course project (Jupyter + LaTeX). Private repo shared by a 4-person team.

## TL;DR
- Code in `notebooks/` for exploration, `src/` for reusable functions.
- Keep raw/large data **out of Git** (use `data/raw/`, which is gitignored).
- Write the paper in LaTeX at `reports/paper/main.tex`; put figures/tables under `reports/`.
- Work on feature branches, PR back to `dev`, and merge to `main` when stable.

## Repo Structure
```
.
├── notebooks/           # Jupyter notebooks (EDA, experiments)
├── src/                 # Python modules reusable across notebooks
├── tests/               # Optional unit tests for src
├── data/
│   ├── raw/             # Original, immutable data dumps (gitignored)
│   ├── processed/       # Cleaned/engineered data (gitignored)
│   └── external/        # Third-party data (gitignored)
├── reports/
│   ├── paper/           # LaTeX paper (main.tex)
│   ├── figures/         # Saved plots/diagrams
│   └── tables/          # Exported CSV/LaTeX tables
├── references/          # BibTeX (references.bib), notes
├── docs/                # Extra documentation (e.g., screenshots)
├── environment.yml      # Reproducible Conda environment
├── CONTRIBUTING.md      # Team workflow and conventions
└── .gitignore
```

## Getting Started

### 1) Create the Conda env
```bash
conda env create -f environment.yml
conda activate dsci511
python -m ipykernel install --user --name dsci511 --display-name "Python (dsci511)"
```

### 2) Install notebook output stripping (optional but recommended)
```bash
nbstripout --install
```
This keeps notebook diffs small by removing heavy outputs on commit (you can still keep key result cells as images under `reports/figures/`).

### 3) Data
- Put original files in `data/raw/` (not tracked by Git).
- Save any intermediate artifacts to `data/processed/`.
- Check in **tiny samples only** if needed for reproducibility (prefix with `sample_`).

## Collaboration Workflow

**Branches**
- `main` = stable, presentation-ready.
- `dev`  = integration branch for features.
- `feature/<name>` = your work branch (e.g., `feature/eda-roy`).

**Typical Cycle**
1. `git checkout -b feature/eda-roy dev`
2. Work in `notebooks/` and `src/`.
3. Commit early/often with clear messages.
4. Open a Pull Request into `dev`, request a teammate review.
5. When `dev` is stable, open a PR into `main` before deadlines.

**Notebook Naming**
- `01-eda-roy.ipynb`, `02-modeling-justin.ipynb`, etc. Use a prefix order tag and your name.

## LaTeX Paper

- Main file: `reports/paper/main.tex`
- Add figures to `reports/figures/` and reference with `\includegraphics{../figures/your_figure}`
- Build locally (one option):
```bash
latexmk -pdf -interaction=nonstopmode reports/paper/main.tex
```
- BibTeX file: `references/references.bib`

## Code Style

- Use Python 3.11.
- Keep reusable logic in `src/` and import into notebooks.
- If adding tests, place them in `tests/` with `pytest` style.

## Quick Git Cookbook

```bash
# First time
git clone <repo-url>
cd DSCI-511-Project
conda env create -f environment.yml && conda activate dsci511

# New branch from dev
git checkout dev
git pull
git checkout -b feature/<name>

# Commit and push
git add .
git commit -m "feat: EDA on shipments dataset (Roy)"
git push -u origin feature/<name>

# Open PR → dev, review, then merge
```

## License
Private class project. Do not distribute without team consent.
