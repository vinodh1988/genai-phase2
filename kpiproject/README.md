# KPI Project

This folder contains a synthetic e-commerce KPI dataset, a generator script, a Jupyter notebook for analysis, and a lightweight dashboard.

## Contents
- `generate_kpi_data.py` - Generates `ecommerce_kpi.csv` with controlled relationships.
- `ecommerce_kpi.csv` - Synthetic daily KPI data (730 rows).
- `kpi_analysis.ipynb` - KPI + scatter + regression notebook.
- `dashboard.html` - Simple KPI dashboard (Chart.js).

## Generate the dataset
From this folder:

```bash
python generate_kpi_data.py
```

## Run the notebook
Install dependencies (if needed):

```bash
pip install pandas numpy matplotlib
```

Then open `kpi_analysis.ipynb` in VS Code and run all cells.

## View the dashboard
To avoid browser file access limits, serve this folder:

```bash
python -m http.server 8000
```

Open: http://localhost:8000/dashboard.html

## Generate a static HTML dashboard
This creates a dashboard folder with PNG charts and an index.html file:

```bash
python build_dashboard.py
```

Then open: dashboard/index.html

## Notes
- Relationships are intentionally controlled to make scatter plots and regressions meaningful.
- You can change `SEED`, `DAYS`, or the seasonality logic in `generate_kpi_data.py` to create new scenarios.
