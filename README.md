## Hot Jupiter Inflation Analysis (Topic 2)

A Python Jupyter notebook project for analysing the inflation of transiting hot Jupiters using the NASA Exoplanet Archive PSCompPars dataset.

## Project Description

This project investigates the radius inflation of well-characterised transiting hot Jupiters. The analysis uses the PSCompPars table downloaded from the NASA Exoplanet Archive and focuses on the relationship between planetary radius and equilibrium temperature, as well as the role of incident flux and host-star properties such as stellar mass and metallicity.

The workflow includes data import, sample filtering, descriptive statistics, scatter plots, binned trend analysis, transition-temperature scanning, correlation tests, multiple linear regression, and Monte Carlo uncertainty analysis. The final goal is to identify whether inflated radii become more common above a characteristic irradiation or temperature threshold and to test how robust these conclusions are when observational uncertainties are included.

## File Structure
```
.
├── analysis.ipynb                          # Primary analysis notebook
├── README.md                               # Project description and instructions
├── PSCompPars_2026.03.15_01.30.06.csv      # NASA Exoplanet Archive dataset
├── topic2_hot_jupiters_clean.csv           # Filtered hot Jupiter sample
├── topic2_summary_results.csv              # Summary correlation results
├── figures/                                # Output plots
│   ├── 01_radius_vs_teq.png
│   ├── 02_binned_radius_vs_teq.png
│   ├── 03_transition_scan.png
│   ├── 04_radius_vs_flux.png
│   ├── 05_radius_vs_host_properties.png
│   └── 06_mc_flux_correlation.png
└── .venv/                                  # Python virtual environment
```

## Required packages

- `pandas` - Data import and table processing
- `numpy` - Numerical computation
- `matplotlib` - Data visualisation
- `scipy` - Correlation statistics
- `statsmodels` - Regression modelling
- `jupyter` - Notebook environment

## Start

### 1. Clone repository
```bash
git clone <your-repository-link>
cd <your-project-folder>
```

### 2. Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate

For Windows:
.venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install pandas numpy matplotlib scipy statsmodels jupyter
```

### 4. Operational Analysis
```bash
jupyter notebook analysis.ipynb
```

## Data file

## Contributor

**Cource:**  PHYS 2116 Computational Assessment (UNSW Sydney)