"""
Validation of AdsorpSuite's IAST against pyIAST
(Simon, Smit & Haranczyk, Comput. Phys. Commun. 200 (2016) 364-380).

Both codes receive EXACTLY the same pure-component isotherms (same models,
same parameters) and compute the same mixtures over a grid of total pressures
and compositions. The adsorbed amount of every component is compared point
by point.

  * Langmuir, dual-site Langmuir, ternary: pyIAST uses the same analytical
    formulas -> agreement expected at the level of the solver tolerances.
  * Toth, Dubinin-Astakhov (no analytical spreading pressure): pyIAST works
    on a dense table (InterpolatorIsotherm) -> agreement expected ~1e-5.
  * Fitting: the same noisy data set is fitted by both codes (Langmuir).

Usage:   python validate_iast_vs_pyiast.py  [path/to/AdsorpSuite.py]
Outputs: "results" folder (text report, CSV of every point, figure).
"""
import os, sys, time, math, platform, importlib.util, warnings
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
APPFILE = (sys.argv[1] if len(sys.argv) > 1 else
           os.path.join(os.path.dirname(HERE), "AdsorpSuite.py"))
OUT = os.path.join(HERE, "results")
os.makedirs(OUT, exist_ok=True)

spec = importlib.util.spec_from_file_location("adsorpsuite", APPFILE)
A = importlib.util.module_from_spec(spec)
spec.loader.exec_module(A)
import pyiast                                                   # noqa: E402
try:
    from importlib.metadata import version as _ver
    PYIAST_V = _ver("pyiast")
except Exception:
    PYIAST_V = getattr(pyiast, "__version__", "?")

warnings.filterwarnings("ignore")
T = 303.15

# ---------------------------------------------------------------- isothermes
def q_model(key, params, P, ctx=None):
    ctx = ctx or {"T": T, "P0": 64.0}
    return np.asarray(A.MODELS[key].func(np.asarray(P, float), ctx, *params),
                      float)


def pyiast_iso(key, params, ctx=None):
    """Isotherme pyIAST equivalente (analytique si possible, sinon table)."""
    if key in ("langmuir", "dsl"):
        P = np.geomspace(1e-3, 100.0, 60)
        df = pd.DataFrame({"P": P, "q": q_model(key, params, P, ctx)})
        if key == "langmuir":
            pr = {"M": params[0], "K": params[1]}
            iso = pyiast.ModelIsotherm(df, loading_key="q", pressure_key="P",
                                       model="Langmuir", param_guess=pr)
        else:
            pr = {"M1": params[0], "K1": params[1], "M2": params[2],
                  "K2": params[3]}
            iso = pyiast.ModelIsotherm(df, loading_key="q", pressure_key="P",
                                       model="DSLangmuir", param_guess=pr)
        iso.params = dict(pr)              # parametres imposes, pas refittes
        return iso, "analytical"
    P = np.geomspace(1e-9, 1e5, 6000)
    q = q_model(key, params, P, ctx)
    df = pd.DataFrame({"P": P, "q": q})
    iso = pyiast.InterpolatorIsotherm(df, loading_key="q", pressure_key="P",
                                      fill_value=float(q[-1]))
    return iso, "table, 6000 pts"


def ads_comp(key, params, ctx=None):
    return A.SpreadingPressure(A.MODELS[key], ctx or {"T": T, "P0": 64.0},
                               params)


CASES = [
    ("Langmuir / Langmuir (CO2/CH4-like)",
     [("langmuir", [10.87, 0.181]), ("langmuir", [7.12, 0.0817])],
     [0.1, 0.5, 1, 5, 10, 20, 40], "binaire", 1e-5),
    ("Langmuir / Langmuir, very different capacities (CO2/N2-like)",
     [("langmuir", [4.0, 2.0]), ("langmuir", [8.0, 0.02])],
     [0.01, 0.1, 1, 5, 10], "binaire", 1e-5),
    ("Dual-site Langmuir / Langmuir",
     [("dsl", [2.0, 5.0, 6.0, 0.1]), ("langmuir", [7.0, 0.05])],
     [0.05, 0.5, 2, 10, 30], "binaire", 1e-5),
    ("Ternary Langmuir (CO2/CH4/H2-like)",
     [("langmuir", [10.87, 0.181]), ("langmuir", [7.12, 0.0817]),
      ("langmuir", [5.29, 0.0131])],
     [1, 10, 40], "ternaire", 1e-5),
    ("Toth / Sips (no analytical spreading pressure for Toth)",
     [("toth", [18.0, 0.05, 0.7]), ("sips", [9.0, 0.03, 0.85])],
     [0.5, 5, 20, 40], "binaire", 1e-3),
    ("Dubinin-Astakhov (P0 = 64 bar) / Langmuir",
     [("da", [12.0, 18000.0, 2.4]), ("langmuir", [7.12, 0.0817])],
     [0.5, 5, 20, 40], "binaire", 1e-3),
]
Y_BIN = [0.05, 0.15, 0.25, 0.5, 0.75, 0.95]
Y_TER = [(1 / 3., 1 / 3., 1 / 3.), (0.5, 0.3, 0.2), (0.15, 0.15, 0.7),
         (0.05, 0.9, 0.05)]

rows, summary = [], []
t_ads = t_py = 0.0
for title, comps, Ptot, kind, tol in CASES:
    a_comps = [ads_comp(k, p) for k, p in comps]
    p_isos, how = zip(*[pyiast_iso(k, p) for k, p in comps])
    ys = Y_BIN if kind == "binaire" else Y_TER
    worst, worst_abs, n = 0.0, 0.0, 0
    for Pt in Ptot:
        for y in ys:
            y = np.array([y, 1 - y]) if kind == "binaire" else np.array(y)
            t0 = time.perf_counter()
            r = A.iast_point(float(Pt), y, a_comps)
            t_ads += time.perf_counter() - t0
            t0 = time.perf_counter()
            qp = pyiast.iast(y * Pt, list(p_isos), warningoff=True)
            t_py += time.perf_counter() - t0
            qa = np.asarray(r["q"], float)
            rel = np.abs(qa - qp) / np.maximum(np.abs(qp), 1e-12)
            worst = max(worst, float(rel.max()))
            worst_abs = max(worst_abs, float(np.abs(qa - qp).max()))
            n += 1
            row = {"cas": title, "P_total (bar)": Pt}
            for i in range(len(y)):
                row["y%d" % (i + 1)] = y[i]
                row["q%d AdsorpSuite (mmol/g)" % (i + 1)] = qa[i]
                row["q%d pyIAST (mmol/g)" % (i + 1)] = qp[i]
                row["ecart relatif %d" % (i + 1)] = rel[i]
            rows.append(row)
    summary.append((title, how[0] if len(set(how)) == 1 else "table + analytical",
                    n, worst, worst_abs, tol, worst <= tol))

# ---------------------------------------------------- ajustement d'un meme jeu
rng = np.random.default_rng(7)
Pf = np.geomspace(0.05, 40, 18)
qf = 10.87 * 0.181 * Pf / (1 + 0.181 * Pf) * (1 + rng.normal(0, 0.01, Pf.size))
fa = A.fit_isotherm(A.MODELS["langmuir"], Pf, qf, {"T": T, "P0": 64.0},
                    n_starts=1, n_boot=0)
fp = pyiast.ModelIsotherm(pd.DataFrame({"P": Pf, "q": qf}), loading_key="q",
                          pressure_key="P", model="Langmuir")
fit_rel = max(abs(fa["params"][0] - fp.params["M"]) / fp.params["M"],
              abs(fa["params"][1] - fp.params["K"]) / fp.params["K"])

# ---------------------------------------------------------------- sorties
df = pd.DataFrame(rows)
df = df.rename(columns=lambda c: c.replace("cas", "case").replace(
    "ecart relatif", "relative deviation"))
df.to_csv(os.path.join(OUT, "validation_pyIAST_points.csv"), index=False)
ok_all = all(s[-1] for s in summary) and fit_rel < 1e-3
L = []
L.append("VALIDATION OF ADSORPSUITE'S IAST AGAINST pyIAST")
L.append("=" * 78)
L.append("AdsorpSuite %s   |   pyIAST %s   |   Python %s, numpy %s, scipy %s"
         % (A.APP_VERSION, PYIAST_V, platform.python_version(), np.__version__,
            __import__("scipy").__version__))
L.append("Date: %s" % time.strftime("%Y-%m-%d %H:%M"))
L.append("")
L.append("Both codes receive the same pure-component isotherms; deviation = "
         "|q_AdsorpSuite - q_pyIAST| / q_pyIAST,")
L.append("maximum over all points and all components.")
L.append("")
L.append("%-62s %-19s %4s %11s %11s  %s" % ("Case", "pyIAST isotherm", "pts",
                                            "max rel.", "max abs.", ""))
for title, how, n, w, wa, tol, ok in summary:
    L.append("%-62s %-19s %4d %11.2e %9.2e mmol/g  %s"
             % (title[:62], how, n, w, wa, "OK" if ok else "CHECK"))
L.append("")
L.append("Langmuir fit of the same noisy data set (18 points, 1 % noise):")
L.append("   AdsorpSuite : q_max = %.5f, b = %.6f" % tuple(fa["params"]))
L.append("   pyIAST      : q_max = %.5f, b = %.6f" % (fp.params["M"], fp.params["K"]))
L.append("   max relative deviation on the parameters: %.1e  %s"
         % (fit_rel, "OK" if fit_rel < 1e-3 else "CHECK"))
L.append("")
L.append("Total computing time: AdsorpSuite %.2f s, pyIAST %.2f s (%d mixtures)"
         % (t_ads, t_py, sum(s[2] for s in summary)))
L.append("")
L.append("CONCLUSION: %s" % ("both codes give the same results within "
                             "numerical tolerance." if ok_all else
                             "at least one case exceeds its tolerance, see "
                             "the CSV file."))
txt = "\n".join(L)
open(os.path.join(OUT, "validation_pyIAST.txt"), "w", encoding="utf-8").write(txt)
print(txt)

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.6))
    qa_all, qp_all, rel_all = [], [], []
    for _, r in df.iterrows():
        for i in (1, 2, 3):
            k = "q%d AdsorpSuite (mmol/g)" % i
            if k in r and np.isfinite(r[k]):
                qa_all.append(r[k]); qp_all.append(r["q%d pyIAST (mmol/g)" % i])
                rel_all.append(r["relative deviation %d" % i])
    qa_all, qp_all, rel_all = map(np.asarray, (qa_all, qp_all, rel_all))
    a1.loglog(qp_all, qa_all, "o", ms=4, alpha=0.7)
    lim = [qp_all[qp_all > 0].min() * 0.7, qp_all.max() * 1.3]
    a1.plot(lim, lim, "k--", lw=1)
    a1.set_xlabel("q pyIAST (mmol/g)"); a1.set_ylabel("q AdsorpSuite (mmol/g)")
    a1.set_title("%d adsorbed amounts compared" % qa_all.size)
    a2.hist(np.log10(np.maximum(rel_all, 1e-16)), bins=30)
    a2.set_xlabel("log10(relative deviation)"); a2.set_ylabel("number of points")
    a2.set_title("Relative deviation AdsorpSuite / pyIAST")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "validation_pyIAST.png"), dpi=150)
except Exception as e:
    print("figure not produced:", e)
sys.exit(0 if ok_all else 1)
