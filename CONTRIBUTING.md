# Contributing Guide

## Branching
- `main`: stable, presentation-ready.
- `dev`: integration branch.
- Feature branches: `feature/<short-name>`

## Workflow
1. Branch from `dev`.
2. Commit small, focused changes with clear messages.
3. Open a PR into `dev` and request one review.
4. Use notebooks in `notebooks/` and reusable code in `src/`.
5. Keep data out of Git except small samples; place raw files in `data/raw/` (gitignored).

## Notebooks
- Start with an issue number and short title, e.g., `01-eda-roy.ipynb`.
- Keep outputs light; consider `nbstripout`:
  ```bash
  nbstripout --install
  ```

## LaTeX
- Main file at `reports/paper/main.tex`.
- Put figures in `reports/figures/` and tables in `reports/tables/`.
- Build example:
  ```bash
  latexmk -pdf -interaction=nonstopmode reports/paper/main.tex
  ```
