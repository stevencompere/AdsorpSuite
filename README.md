# AdsorpSuite

Python GUI for adsorption isotherms fitting, excess-to-absolute conversion, and IAST mixture calculations.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22011513.svg)](https://doi.org/10.5281/zenodo.22011513)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Citation

If you use **AdsorpSuite** in your research or publications, please cite the software as follows:


<pre><code>@software{compere_adsorpsuite_2026,
  author       = {Compère, Steven},
  title        = {AdsorpSuite: Comprehensive Adsorption Isotherm Analysis, Excess-to-Absolute Conversion, and IAST Mixture Modeling},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {v3.0},
  doi          = {10.5281/zenodo.22011513},
  url          = {https://doi.org/10.5281/zenodo.22011513}
}</code></pre>

S. Compère, AdsorpSuite: Comprehensive Adsorption Isotherm Analysis, Excess-to-Absolute Conversion, and IAST Mixture Modeling (v3.0). Zenodo. (2026), https://doi.org/10.5281/zenodo.22011513

## Author & Contact

* **Author:** Steven Compère (PhD, Materials Chemistry)
* **Email:** compere.steven@gmail.com
* **ORCID:** [0009-0006-3474-8748](https://orcid.org/0009-0006-3474-8748)
* **Bug reports & feature requests:** Please use [GitHub Issues](https://github.com/stevencompere/AdsorpSuite/issues).

## About AdsorpSuite v3.0.0

First public release of **AdsorpSuite**, a comprehensive Python GUI application (Tkinter) dedicated to thermodynamic analysis and adsorption isotherm modeling for porous materials (microporous/mesoporous carbons such as ZTCs, MOFs, zeolites).

### Key Features

* **Data Import & Management:**
* Support for `.xlsx`, `.xls`, `.csv`, `.txt`, and `.dat` file formats.
* Editable data grid with full Excel copy/paste support (`Ctrl+V`).
* Automatic unit conversion for pressure (bar, Pa, MPa, atm, Torr, psi) and loading ($\text{mmol/g}$, $\text{mol/kg}$, $\text{cm}^3\text{(STP)/g}$, $\text{wt}\%$, etc.).


* **Excess-to-Absolute Conversion ($n_{\text{tot}}$):**
* Methods: Pore volume, Adsorbed phase density, Custom external density.
* Bulk gas density calculation $\rho_{\text{gas}}(T, P)$ via Peng-Robinson Equation of State (with Péneloux volume translation) and CoolProp support.
* Automated detection of near-critical and supercritical fluid conditions.


* **Robust Non-Linear Isotherm Fitting:**
* 7 implemented models: Langmuir, Dual-Site Langmuir (DSL), Freundlich, Sips, Toth, Dubinin-Radushkevich (D-R), and Dubinin-Astakhov (D-A).
* Multi-start random optimization algorithm (mitigating local minima traps for Sips and Toth models).
* 95% confidence intervals calculated via non-parametric residual bootstrapping.
* Parameter collinearity analysis ($\vert{}r\vert{}_{\max}$) and comprehensive statistical ranking (AIC, AICc, BIC, $R^2$, RMSE, ARE).


* **Mixture Adsorption Thermodynamics (IAST):**
* Binary and ternary mixture predictions over total pressure or gas molar fraction ($y$) sweeps.
* 1D reduced spreading pressure ($\pi^*$) solver based on Brent's method.
* Extrapolation diagnostic system flagging data outside experimental pressure bounds ($P^0 / P_{\text{exp}} > 1$ and $> 2$).


* **Visualization & Export:**
* Interactive plotting canvas with style customization, dual Y-axis, residual plots, and annotations.
* Publication-ready graphic exports (PNG, PDF, SVG, EPS, TIFF).
* Comprehensive multi-sheet Excel workbooks export (`.xlsx`) and human-readable JSON project save files (`.adsp`).


* **Internal Validation:**
* Built-in automated test suite executable directly via `python AdsorpSuite.py --selftest`.



### Dependencies

* Python $\ge 3.9$
* `numpy`, `scipy`, `pandas`, `matplotlib`, `openpyxl`
* *(Optional)* `CoolProp`
