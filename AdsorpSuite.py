# -*- coding: utf-8 -*-
"""
===============================================================================
 AdsorpSuite  v3.2
 Suite complete d'analyse d'isothermes d'adsorption  (tout-en-un)
===============================================================================

 Onglets :
   1. Donnees        : saisie manuelle / collage Excel / import .xlsx-.csv
                       + IMPORT EN LOT de plusieurs fichiers (v3)
   2. Conversion     : quantite en EXCES  ->  quantite TOTALE (n_tot)
                       + conversion de TOUS les jeux en une fois (v3)
   3. Ajustement     : Langmuir, Langmuir bi-site, Freundlich, Sips, Toth,
                       Dubinin-Radushkevich (D-R), Dubinin-Astakhov (D-A)
                       + ajustement en lot et matrice de comparaison (v3)
   4. IAST           : melanges binaires et ternaires, tous modeles
                       + melanges types en un clic (v3)
   5. Chaleur isost. : Clausius-Clapeyron (fugacite) et viriel (v3.1)
   6. Graphiques     : figure personnalisable + export PNG/PDF/SVG/EPS/TIFF
   7. Export         : classeur Excel multi-feuilles, projet .adsp (JSON)
                       + export Origin (Long Name / Units) (v3)

-------------------------------------------------------------------------------
 NOUVEAUTES 3.2  (ergonomie)
-------------------------------------------------------------------------------
   * IAST : les constituants sont proposes d'apres les ajustements (un par
     gaz, jeux 'total', meme temperature) et controles avant le calcul ; leur
     configuration est conservee dans la session.
   * Journal et barre d'etat toujours visibles (bouton "Journal") ; onglets
     Conversion, IAST et Chaleur isosterique en deux colonnes, reglages a
     gauche et resultats a droite ; panneaux des graphiques cote a cote quand
     la place manque : tout tient dans une fenetre de 1150 x 720.
   * Ajustement : jeu 'total' propose au depart, jeux en exces deja convertis
     laisses hors de l'ajustement en lot, menus "Comparer" et "Exporter".
   * Un seul import : gaz, temperature et echantillon lus dans le nom du
     fichier, lignes a verifier en jaune, noms de jeux uniques.
   * Fenetre : taille memorisee sans depasser l'ecran ; le changement de
     langue rouvre la session en cours.
   * Graphiques : bouton "Ajouter" et message d'accueil quand la figure est
     vide ; "Vers Graphiques" confirme ce qui a ete envoye.
   * V_pore n'est plus prerempli ; P max de l'IAST suit la gamme mesuree.
   * Francais affiche avec ses accents (le code reste sans accents, voir
     FR_ACCENTS) ; Ctrl+1..7 repond aussi sur un clavier AZERTY.
   * Correctifs : une valeur modifiee ou collee dans le tableau des donnees
     est bien enregistree automatiquement (elle etait perdue en changeant de
     jeu, en enregistrant la session ou en quittant) ; un jeu saisi apres
     "Nouveau jeu vide" n'ecrase plus le jeu ouvert avant ; Qst suit la
     temperature actuelle du jeu ; l'ancienne session
     reste en place si l'ecriture echoue ; unites de pi* et de P0/P_exp dans
     l'export Origin.

-------------------------------------------------------------------------------
 NOUVEAUTES 3.1
-------------------------------------------------------------------------------
   * Interface en francais ou en anglais (menu Langue / Language).
   * Onglet "Chaleur isosterique" : Clausius-Clapeyron a partir des modeles
     ajustes (base fugacite ou pression, sans extrapolation, incertitude-type
     des 3 temperatures) et equation du viriel (Qst0, degres choisis par AICc).
   * Gaz ajoutes : C2H2, C3H6, i-C4H10, SF6, N2O, D2 ; reconnaissance du gaz
     dans les noms de fichiers etendue (formules et noms en toutes lettres).
   * Melanges types : CO2/N2, CO2/H2, CH4/N2, C2H2/CO2, C2H2/C2H4, C2H4/C2H6,
     C3H6/C3H8, Xe/Kr, en plus des melanges CO2/CH4 et CH4/H2.
   * Calcul IAST compare a pyIAST (rapport de validation fourni).
   * Alerte quand des points depassent la pression de vapeur saturante
     (ex. CO2 a 273 K au-dela de 34,9 bar) : conversion, ajustement, Qst.
   * Conversion en lot : un volume poreux par echantillon ; melanges types :
     ajustements choisis a la meme temperature et sur le meme echantillon.
   * Programme Windows autonome (.exe) incluant CoolProp.

-------------------------------------------------------------------------------
 CORRECTIFS 3.0.1
-------------------------------------------------------------------------------
   * Les panneaux des onglets 2 a 6 s'ouvraient replies (liste des modeles de
     l'onglet Ajustement, graphiques de l'onglet IAST, tableau de l'onglet
     Conversion) : la position des separateurs est maintenant appliquee a la
     premiere ouverture de chaque onglet.
   * Conversion : l'avertissement "etat quasi-critique, utilisez CoolProp"
     s'affichait meme quand la densite venait de la table NIST ou de CoolProp.
     Il n'apparait plus que lorsque la densite vient reellement d'une EOS cubique.

-------------------------------------------------------------------------------
 NOUVEAUTES DE LA VERSION 3.0
-------------------------------------------------------------------------------
 EXACTITUDE
   * Densites de gaz de reference tabulees (NIST Chemistry WebBook) pour CO2,
     CH4 et H2 a 303 K, choisies par defaut pour la conversion exces -> total.
     Peng-Robinson s'ecarte de 1 a 3 % de ces valeurs, et cet ecart se propage
     directement dans n_total. Repli automatique sur Peng-Robinson hors table.
   * La verification interne compte desormais 39 controles (contre 30).

 ERGONOMIE
   * PLUS DE PERTE DE SAISIE : le jeu de donnees en cours est enregistre
     automatiquement quand on change de jeu, quand on quitte l'onglet, et avant
     tout calcul. Un temoin "modifications non enregistrees / a jour" indique
     l'etat en permanence.
   * Champ de filtre au-dessus de la liste des jeux de donnees.
   * Import en lot : selection multiple de fichiers, deduction automatique du
     gaz et de l'echantillon d'apres le nom, recapitulatif modifiable avant
     validation (double-clic pour corriger une ligne).
   * Conversion en lot : tous les jeux "Exces" convertis d'un coup.
   * Ajustement en lot : tous les jeux x tous les modeles coches, avec barre de
     progression et rapport d'echecs.
   * Matrice de comparaison des modeles : tableau croise jeu x modele
     (R2, RMSE, AICc) avec le meilleur modele signale par jeu.
   * Melanges types IAST en un clic (CO2/CH4 50:50, 25:75, 75:25, CH4/H2 50:50,
     ternaire), avec association automatique des ajustements par gaz.
   * Export Origin : classeur au format large, ligne 1 = Long Name,
     ligne 2 = Units, donnees a partir de la ligne 3.
   * Raccourcis : Maj+F5 = action en lot de l'onglet actif, Ctrl+I = import
     multiple, Ctrl+E = export Origin.

-------------------------------------------------------------------------------
 Dependances : numpy, scipy, pandas, matplotlib, openpyxl
               (optionnel : CoolProp pour les densites de gaz reel)

 Lancement   : python AdsorpSuite.py
-------------------------------------------------------------------------------
 Auteur : genere pour Steven Compere - analyse d'adsorption sur carbones ZTC
===============================================================================
"""

from __future__ import annotations

import os
import re
import sys
import json
import math
import copy
import datetime
import traceback
import unicodedata

import numpy as np
import pandas as pd

import matplotlib
try:
    matplotlib.use("TkAgg")
except Exception:
    pass
from matplotlib.figure import Figure
try:
    from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                                   NavigationToolbar2Tk)
except Exception:
    FigureCanvasTkAgg = None
    NavigationToolbar2Tk = None

from scipy.optimize import curve_fit, brentq
from scipy.integrate import quad
from scipy.special import gammaincc, gamma as gamma_fn

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, colorchooser

try:
    from CoolProp.CoolProp import PropsSI
    HAS_COOLPROP = True
except Exception:
    HAS_COOLPROP = False


# =============================================================================
# 0. LANGUE DE L'INTERFACE (francais / anglais)
# =============================================================================
# Le francais est la langue source du code. Toute chaine affichee passe par
# _() qui renvoie sa traduction anglaise lorsque l'interface est en anglais,
# et le francais avec ses accents sinon (section 17).
# Les valeurs internes (cles, noms de colonnes, contenu des sessions) restent
# en francais : une session enregistree s'ouvre dans les deux langues.

LANG = "fr"
LANGUAGES = [("fr", "Français"), ("en", "English")]
TR_EN = {}          # francais -> anglais (rempli a la fin du fichier)
TR_FR = {}          # francais du code (sans accents) -> francais affiche


def _(s):
    """Traduit une chaine de l'interface dans la langue courante."""
    if isinstance(s, str):
        return (TR_FR if LANG == "fr" else TR_EN).get(s, s)
    return s


def set_language(lang):
    global LANG
    LANG = "en" if str(lang or "").lower().startswith("en") else "fr"
    return LANG


def system_language():
    """'fr' si l'interface de Windows (ou la locale) est en francais."""
    try:
        if sys.platform.startswith("win"):
            import ctypes
            lid = ctypes.windll.kernel32.GetUserDefaultUILanguage()
            return "fr" if (lid & 0x3FF) == 0x0C else "en"
    except Exception:
        pass
    try:
        import locale
        loc = (locale.getlocale()[0] or os.environ.get("LANG", "") or "").lower()
        return "fr" if (loc.startswith("fr") or "french" in loc) else "en"
    except Exception:
        return "en"


# noms de colonnes construits (gaz, temperature...) : traduction par motifs
_COL_PATTERNS = [
    (r" pur \(", " pure ("),
    (r"^P a (.+) K \(bar\)$", r"P at \1 K (bar)"),
    (r"viriel", "virial"),
    (r"^Densite ", "Density "),
    (r"_err$", "_err"),
    (r"_nom$", "_name"),
    (r"_unite$", "_unit"),
    (r"^R2_ajuste$", "R2_adj"),
    (r" IC (\d)", r" CI \1"),
]


def tr_col(c, screen=False):
    """Nom de colonne ou d'en-tete dans la langue courante. En francais les
    accents ne sont ajoutes qu'a l'ecran (screen=True) : les fichiers exportes
    gardent leurs en-tetes d'origine."""
    if not isinstance(c, str):
        return c
    if LANG == "fr":
        return TR_FR.get(c, c) if screen else c
    if c in TR_EN:
        return TR_EN[c]
    import re as _re
    out = c
    for pat, rep in _COL_PATTERNS:
        out = _re.sub(pat, rep, out)
    return out


def tr_df(df):
    """Copie d'un DataFrame aux colonnes traduites (pour les exports)."""
    if LANG == "fr" or df is None:
        return df
    return df.rename(columns=tr_col)


_PD_TO_EXCEL = pd.DataFrame.to_excel
_PD_TO_CSV = pd.DataFrame.to_csv


def _to_excel_tr(self, *a, **k):
    return _PD_TO_EXCEL(tr_df(self), *a, **k)


def _to_csv_tr(self, *a, **k):
    return _PD_TO_CSV(tr_df(self), *a, **k)


# tous les exports de tableaux passent par la : en anglais, les en-tetes
# sont traduits au moment de l'ecriture, les donnees internes restent intactes
pd.DataFrame.to_excel = _to_excel_tr
pd.DataFrame.to_csv = _to_csv_tr


class TCombobox(ttk.Combobox):
    """Liste deroulante traduite : affiche _(valeur) mais get(), set(),
    ["values"] et cget("values") manipulent la valeur interne (francaise)."""

    def __init__(self, master=None, **kw):
        vals = kw.pop("values", None)
        self._internal = []
        ttk.Combobox.__init__(self, master, **kw)
        if vals is not None:
            self._set_values(vals)

    def _set_values(self, vals):
        self._internal = list(vals) if vals is not None else []
        ttk.Combobox.configure(self, values=[_(v) if isinstance(v, str) else v
                                             for v in self._internal])

    def configure(self, cnf=None, **kw):
        if isinstance(cnf, dict):
            kw = dict(cnf, **kw)
            cnf = None
        if "values" in kw:
            self._set_values(kw.pop("values"))
            if not kw and cnf is None:
                return None
        return ttk.Combobox.configure(self, cnf, **kw)

    config = configure

    def __setitem__(self, key, value):
        self.configure(**{key: value})

    def cget(self, key):
        if key == "values":
            return tuple(self._internal)
        return ttk.Combobox.cget(self, key)

    def __getitem__(self, key):
        return self.cget(key)

    def get(self):
        disp = ttk.Combobox.get(self)
        for v in self._internal:
            if isinstance(v, str) and _(v) == disp:
                return v
        return disp

    def set(self, value):
        ttk.Combobox.set(self, _(value) if isinstance(value, str) else value)


# =============================================================================
# 1. CONSTANTES ET DONNEES PHYSIQUES
# =============================================================================

APP_NAME = "AdsorpSuite"
APP_VERSION = "3.2.0"

R_J = 8.314462618          # J / (mol.K)
_TRAPZ = getattr(np, "trapezoid", None) or np.trapz   # numpy 1.x et 2.x
V_MOLAR_STP = 22.413969    # L/mol  a 273.15 K et 1 atm  (=> cm3/mmol)

# Base de donnees des gaz : Tc (K), Pc (bar), facteur acentrique, M (g/mol)
GAS_DB = {
    "CO2":     dict(Tc=304.1282, Pc=73.773,  w=0.22394,   M=44.0095),
    "CH4":     dict(Tc=190.564,  Pc=45.992,  w=0.01142,   M=16.0425),
    "H2":      dict(Tc=33.145,   Pc=12.964,  w=-0.219,    M=2.01588),
    "N2":      dict(Tc=126.192,  Pc=33.958,  w=0.0372,    M=28.0134),
    "O2":      dict(Tc=154.581,  Pc=50.430,  w=0.0222,    M=31.9988),
    "Ar":      dict(Tc=150.687,  Pc=48.630,  w=-0.00219,  M=39.948),
    "CO":      dict(Tc=132.860,  Pc=34.940,  w=0.0497,    M=28.0101),
    "He":      dict(Tc=5.1953,   Pc=2.2746,  w=-0.385,    M=4.0026),
    "Ne":      dict(Tc=44.4918,  Pc=26.786,  w=-0.0387,   M=20.1797),
    "Kr":      dict(Tc=209.48,   Pc=55.250,  w=-0.000894, M=83.798),
    "Xe":      dict(Tc=289.733,  Pc=58.420,  w=0.00363,   M=131.293),
    "C2H6":    dict(Tc=305.322,  Pc=48.722,  w=0.0995,    M=30.069),
    "C2H4":    dict(Tc=282.35,   Pc=50.418,  w=0.0866,    M=28.054),
    "C3H8":    dict(Tc=369.89,   Pc=42.512,  w=0.1521,    M=44.0956),
    "n-C4H10": dict(Tc=425.125,  Pc=37.960,  w=0.201,     M=58.122),
    "NH3":     dict(Tc=405.40,   Pc=113.33,  w=0.25601,   M=17.0305),
    "H2S":     dict(Tc=373.10,   Pc=90.000,  w=0.1005,    M=34.081),
    "SO2":     dict(Tc=430.64,   Pc=78.840,  w=0.2557,    M=64.064),
    "H2O":     dict(Tc=647.096,  Pc=220.640, w=0.3443,    M=18.01528),
    # ajouts v3.1 : constantes de CoolProp 8 (equations de reference), sauf
    # C2H2 (absent de CoolProp) : Tc, Pc du NIST WebBook, w ~ 0,187
    "C2H2":    dict(Tc=308.3,    Pc=61.38,   w=0.187,     M=26.0373),
    "C3H6":    dict(Tc=364.211,  Pc=45.550,  w=0.146,     M=42.0797),
    "i-C4H10": dict(Tc=407.81,   Pc=36.290,  w=0.18353,   M=58.1222),
    "SF6":     dict(Tc=318.7232, Pc=37.550,  w=0.21,      M=146.0554),
    "N2O":     dict(Tc=309.5207, Pc=72.448,  w=0.1613,    M=44.0128),
    "D2":      dict(Tc=38.34,    Pc=16.796,  w=-0.13629,  M=4.0282),
}
GAS_LIST = list(GAS_DB.keys())

# Noms CoolProp correspondants
COOLPROP_NAMES = {
    "CO2": "CarbonDioxide", "CH4": "Methane", "H2": "Hydrogen",
    "N2": "Nitrogen", "O2": "Oxygen", "Ar": "Argon", "CO": "CarbonMonoxide",
    "He": "Helium", "Ne": "Neon", "Kr": "Krypton", "Xe": "Xenon",
    "C2H6": "Ethane", "C2H4": "Ethylene", "C3H8": "n-Propane",
    "n-C4H10": "n-Butane", "NH3": "Ammonia", "H2S": "HydrogenSulfide",
    "SO2": "SulfurDioxide", "H2O": "Water",
    "C3H6": "Propylene", "i-C4H10": "IsoButane", "SF6": "SulfurHexafluoride",
    "N2O": "NitrousOxide", "D2": "Deuterium",
}

# Facteurs de conversion vers le bar
P_UNITS = {
    "bar": 1.0, "mbar": 1e-3, "Pa": 1e-5, "kPa": 1e-2, "MPa": 10.0,
    "atm": 1.01325, "torr": 1.0/750.06168, "mmHg": 1.0/750.06168,
    "psi": 0.0689475729,
}

Q_UNITS = ["mmol/g", "mol/kg", "cm3(STP)/g", "mg/g", "wt%", "g/g", "mmol/cm3"]


def q_to_mmol_g(q, unit, M_gmol, rho_bulk=None):
    """Convertit une quantite adsorbee vers mmol/g."""
    q = np.asarray(q, dtype=float)
    if unit in ("mmol/g", "mol/kg"):
        return q
    if unit == "cm3(STP)/g":
        return q / V_MOLAR_STP
    if unit == "mg/g":
        return q / M_gmol
    if unit == "wt%":
        # g adsorbat / 100 g adsorbant  ->  mmol/g
        return q * 10.0 / M_gmol
    if unit == "g/g":
        return q * 1000.0 / M_gmol
    if unit == "mmol/cm3":
        if not rho_bulk:
            return q
        return q / rho_bulk
    return q


def mmol_g_to_unit(q, unit, M_gmol, rho_bulk=None):
    """Conversion inverse de q_to_mmol_g."""
    q = np.asarray(q, dtype=float)
    if unit in ("mmol/g", "mol/kg"):
        return q
    if unit == "cm3(STP)/g":
        return q * V_MOLAR_STP
    if unit == "mg/g":
        return q * M_gmol
    if unit == "wt%":
        return q * M_gmol / 10.0
    if unit == "g/g":
        return q * M_gmol / 1000.0
    if unit == "mmol/cm3":
        if not rho_bulk:
            return q
        return q * rho_bulk
    return q



# -----------------------------------------------------------------------------
# Densites molaires de reference (NIST Chemistry WebBook) le long d'isothermes
# usuelles. Sert d'alternative "exacte" a l'EOS cubique pour la conversion
# exces -> total, ou l'erreur sur rho se propage directement sur n_total.
#   cle   : (gaz, T en K)
#   valeur: (tableau P en bar, tableau rho en mol/L == mmol/cm3)
# Sources : Span & Wagner 1996 (CO2), Setzmann & Wagner 1991 (CH4),
#           Leachman et al. 2009 (H2 normal).
# CO2 est SOUS-critique a 303 K (Tc = 304,128 K) : la table s'arrete a
# Psat = 71,89 bar, au-dela le fluide est liquide.
# -----------------------------------------------------------------------------

_NIST_RAW = {
 ("CO2", 303.0): (
  "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 "
  "28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 "
  "53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71",
  "0 0.0398818 0.0801462 0.120802 0.161860 0.203329 0.245220 0.287544 0.330313 "
  "0.373538 0.417231 0.461406 0.506075 0.551254 0.596956 0.643198 0.689995 "
  "0.737365 0.785324 0.833893 0.883090 0.932936 0.983453 1.03466 1.08659 "
  "1.13927 1.19271 1.24695 1.30203 1.35796 1.41479 1.47256 1.53129 1.59104 "
  "1.65185 1.71376 1.77683 1.84111 1.90666 1.97354 2.04183 2.11159 2.18292 "
  "2.25589 2.33061 2.40719 2.48573 2.56637 2.64925 2.73454 2.82241 2.91307 "
  "3.00673 3.10366 3.20416 3.30856 3.41727 3.53073 3.64951 3.77425 3.90576 "
  "4.04500 4.19320 4.35192 4.52320 4.70980 4.91558 5.14622 5.41063 5.72425 "
  "6.11813 6.67526"),
 ("CH4", 303.0): (
  " ".join(str(i) for i in range(0, 101)),
  "0 0.0397584 0.0796467 0.119665 0.159814 0.200094 0.240505 0.281047 0.321721 "
  "0.362527 0.403466 0.444536 0.485740 0.527077 0.568547 0.610150 0.651887 "
  "0.693758 0.735763 0.777902 0.820176 0.862584 0.905126 0.947804 0.990616 "
  "1.03356 1.07664 1.11986 1.16321 1.20670 1.25032 1.29408 1.33797 1.38200 "
  "1.42616 1.47045 1.51488 1.55945 1.60414 1.64898 1.69394 1.73904 1.78427 "
  "1.82963 1.87513 1.92076 1.96652 2.01241 2.05843 2.10458 2.15086 2.19727 "
  "2.24380 2.29047 2.33726 2.38417 2.43122 2.47838 2.52567 2.57309 2.62062 "
  "2.66828 2.71605 2.76395 2.81196 2.86009 2.90833 2.95669 3.00517 3.05375 "
  "3.10245 3.15125 3.20016 3.24918 3.29830 3.34753 3.39686 3.44629 3.49582 "
  "3.54544 3.59516 3.64497 3.69487 3.74487 3.79495 3.84511 3.89537 3.94570 "
  "3.99611 4.04660 4.09716 4.14780 4.19850 4.24928 4.30012 4.35102 4.40199 "
  "4.45302 4.50410 4.55523 4.60642"),
 ("H2", 303.0): (
  " ".join(str(i) for i in range(0, 101)),
  "0 0.0396708 0.0792956 0.118874 0.158407 0.197894 0.237335 0.276730 0.316080 "
  "0.355384 0.394642 0.433854 0.473021 0.512143 0.551219 0.590250 0.629235 "
  "0.668176 0.707070 0.745920 0.784725 0.823484 0.862199 0.900868 0.939492 "
  "0.978072 1.01661 1.05510 1.09354 1.13194 1.17030 1.20861 1.24687 1.28510 "
  "1.32327 1.36141 1.39950 1.43754 1.47554 1.51349 1.55141 1.58927 1.62710 "
  "1.66487 1.70261 1.74030 1.77795 1.81555 1.85311 1.89062 1.92809 1.96552 "
  "2.00290 2.04024 2.07754 2.11479 2.15200 2.18917 2.22629 2.26337 2.30040 "
  "2.33739 2.37434 2.41125 2.44811 2.48493 2.52170 2.55843 2.59512 2.63177 "
  "2.66837 2.70493 2.74145 2.77793 2.81436 2.85075 2.88709 2.92340 2.95966 "
  "2.99588 3.03205 3.06819 3.10428 3.14033 3.17633 3.21230 3.24822 3.28410 "
  "3.31994 3.35573 3.39148 3.42720 3.46287 3.49849 3.53408 3.56962 3.60512 "
  "3.64058 3.67600 3.71138 3.74671"),
}

NIST_TABLES = {}
for _k, (_pp, _rr) in _NIST_RAW.items():
    _P = np.array([float(x) for x in _pp.split()])
    _R = np.array([float(x) for x in _rr.split()])
    if len(_P) == len(_R):
        NIST_TABLES[_k] = (_P, _R)

NIST_GASES = sorted({g for (g, _T) in NIST_TABLES})
NIST_TEMPS = sorted({T for (_g, T) in NIST_TABLES})


def nist_available(gas, T, tol=0.6):
    """Renvoie la cle (gas, T_table) si une table de reference couvre ce cas."""
    for (g, Tt) in NIST_TABLES:
        if g == gas and abs(Tt - T) <= tol:
            return (g, Tt)
    return None


def nist_density_mmol_cm3(T, P_bar, gas):
    """Densite molaire de reference interpolee (mmol/cm3 == mol/L).
    Renvoie nan hors table (extrapolation volontairement interdite)."""
    key = nist_available(gas, T)
    if key is None:
        return float("nan")
    Pt, Rt = NIST_TABLES[key]
    P = float(P_bar)
    if P < 0 or P > Pt[-1] * 1.0000001:
        return float("nan")
    if 0.0 < P < Pt[1] and Pt[0] == 0.0 and Rt[1] > 0:
        # Entre 0 et le premier point de la table, Z - 1 est proportionnel a P
        # (second coefficient du viriel). Interpoler rho lineairement y
        # donnerait un Z constant, ce qui fausse l'integrale de ln(phi).
        Z1 = Pt[1] * 1e5 / (Rt[1] * 1e3 * R_J * float(T))
        Z = 1.0 + (Z1 - 1.0) * P / Pt[1]
        return P * 1e5 / (Z * R_J * float(T)) * 1e-3
    return float(np.interp(min(P, Pt[-1]), Pt, Rt))

# =============================================================================
# 2. EQUATION D'ETAT (PENG-ROBINSON) ET DENSITES DE GAZ
# =============================================================================

def pr_compressibility(T, P_bar, Tc, Pc_bar, omega):
    """Facteur de compressibilite Z de la phase vapeur (Peng-Robinson, 1976)."""
    if P_bar <= 0:
        return 1.0
    Tr = T / Tc
    if omega <= 0.49:
        kappa = 0.37464 + 1.54226 * omega - 0.26992 * omega ** 2
    else:
        kappa = 0.379642 + 1.48503 * omega - 0.164423 * omega ** 2 \
                + 0.016666 * omega ** 3
    alpha = (1.0 + kappa * (1.0 - math.sqrt(Tr))) ** 2
    Pc = Pc_bar * 1e5
    P = P_bar * 1e5
    a = 0.45723553 * R_J ** 2 * Tc ** 2 / Pc * alpha
    b = 0.07779607 * R_J * Tc / Pc
    A = a * P / (R_J * T) ** 2
    B = b * P / (R_J * T)
    coeffs = [1.0, -(1.0 - B), A - 3.0 * B ** 2 - 2.0 * B,
              -(A * B - B ** 2 - B ** 3)]
    roots = np.roots(coeffs)
    real = roots[np.abs(roots.imag) < 1e-8].real
    real = real[real > B]
    if real.size == 0:
        return 1.0
    return float(np.max(real))       # racine vapeur


def pr_molar_volume(T, P_bar, Tc, Pc_bar, omega, translate=True):
    """Volume molaire (m3/mol) par Peng-Robinson avec translation de Peneloux."""
    Z = pr_compressibility(T, P_bar, Tc, Pc_bar, omega)
    V = Z * R_J * T / (P_bar * 1e5)
    if translate:
        Zra = 0.29056 - 0.08775 * omega
        c = 0.40768 * (R_J * Tc / (Pc_bar * 1e5)) * (0.29441 - Zra)
        V = V - c
    return max(V, 1e-9)


def gas_density_mmol_cm3(T, P_bar, gas, eos="Peng-Robinson"):
    if eos == "Table NIST":
        v = nist_density_mmol_cm3(T, P_bar, gas)
        if np.isfinite(v):
            return v
        eos = "Peng-Robinson"   # repli automatique hors table

    """Densite molaire du gaz libre, en mmol/cm3.

    eos : "Gaz parfait" | "Peng-Robinson" | "CoolProp"
    """
    P_bar = float(P_bar)
    if P_bar <= 0:
        return 0.0
    if eos == "CoolProp" and HAS_COOLPROP and gas in COOLPROP_NAMES:
        try:
            rho = PropsSI("Dmolar", "T", T, "P", P_bar * 1e5,
                          COOLPROP_NAMES[gas])      # mol/m3
            return rho * 1e-3                        # -> mmol/cm3
        except Exception:
            pass
    if eos == "Gaz parfait" or gas not in GAS_DB:
        rho_mol_m3 = (P_bar * 1e5) / (R_J * T)
    else:
        g = GAS_DB[gas]
        rho_mol_m3 = 1.0 / pr_molar_volume(T, P_bar, g["Tc"], g["Pc"], g["w"])
    return rho_mol_m3 * 1e-3                        # mol/m3 -> mmol/cm3


def eos_z_effective(T, P_bar, gas, eos="Peng-Robinson"):
    """Facteur de compressibilite effectif reellement utilise pour rho."""
    if P_bar <= 0:
        return 1.0
    rho = gas_density_mmol_cm3(T, P_bar, gas, eos)      # mmol/cm3 = kmol/m3
    if rho <= 0:
        return 1.0
    return (P_bar * 1e5) / (rho * 1e3 * R_J * T)


def near_critical(gas, T, P_bar):
    """Signale un etat ou les EOS cubiques sont peu fiables (+/- 10-25 %)."""
    if gas not in GAS_DB:
        return False, ""
    g = GAS_DB[gas]
    Tr = T / g["Tc"]
    Pr = P_bar / g["Pc"]
    if 0.85 < Tr < 1.25 and Pr > 0.4:
        return True, (_("Etat quasi-critique (Tr=%.2f, Pr=%.2f) : l'ecart de "
                      "Peng-Robinson sur la densite peut atteindre 10 a 25 %%. "
                      "Utilisez CoolProp (pip install CoolProp) ou la methode "
                      "\"Densite fournie\" avec des valeurs NIST/REFPROP.")
                      % (Tr, Pr))
    return False, "Tr=%.2f, Pr=%.2f" % (Tr, Pr)


def density_is_reference(gas, T, P_max, eos):
    """Vrai si les densites viennent d'une source de reference (table NIST ou
    CoolProp) et non d'une equation d'etat cubique."""
    if eos == "CoolProp":
        return True
    if eos == "Table NIST":
        key = nist_available(gas, T)
        return key is not None and float(P_max) <= NIST_TABLES[key][0][-1]
    return False


def excess_to_total(P_bar, n_exc, T, gas, method="Volume poreux",
                    V_pore=0.0, rho_ads=None, eos="Peng-Robinson",
                    rho_gas_user=None):
    """Conversion quantite en exces -> quantite totale (absolue).

    Methodes :
      "Volume poreux"     : n_tot = n_exc + V_pore * rho_gaz(T,P)
      "Densite adsorbee"  : n_tot = n_exc / (1 - rho_gaz/rho_ads)
      "Densite fournie"   : idem "Volume poreux" avec rho_gaz donne par l'utilisateur
    Unites : P (bar), n (mmol/g), V_pore (cm3/g), rho_ads (mmol/cm3)
    """
    P_bar = np.asarray(P_bar, dtype=float)
    n_exc = np.asarray(n_exc, dtype=float)

    if method == "Densite fournie" and rho_gas_user is not None:
        rho = np.asarray(rho_gas_user, dtype=float)
    else:
        rho = np.array([gas_density_mmol_cm3(T, p, gas, eos) for p in P_bar])

    if method == "Densite adsorbee":
        if not rho_ads or rho_ads <= 0:
            raise ValueError(_("Densite de phase adsorbee invalide."))
        denom = 1.0 - rho / rho_ads
        denom = np.where(np.abs(denom) < 1e-9, np.nan, denom)
        return n_exc / denom, rho
    # methodes volumetriques
    return n_exc + V_pore * rho, rho


# =============================================================================
# 3. MODELES D'ISOTHERMES
# =============================================================================
# Chaque modele est decrit par :
#   func(P, ctx, *params)   -> q (mmol/g)
#   pi  (P, ctx, *params)   -> pression d'etalement reduite pi*A/RT (mmol/g)
#                              (None => integration numerique)
#   pinv(pi, ctx, *params)  -> P0 tel que pi(P0) = pi  (None => inversion num.)
#   guess(P, q, ctx)        -> valeurs initiales
#   bounds(P, q, ctx)       -> (bornes_inf, bornes_sup)
#   needs                   -> parametres de contexte requis ('T', 'P0')
# ctx = {'T': temperature (K), 'P0': pression de saturation / reference (bar)}

_EPS = 1e-300


def _safe_P(P):
    return np.maximum(np.atleast_1d(np.asarray(P, dtype=float)), 0.0)


# ---------------------------------------------------------------- Langmuir --
def f_langmuir(P, ctx, qm, b):
    P = _safe_P(P)
    return qm * b * P / (1.0 + b * P)


def pi_langmuir(P, ctx, qm, b):
    P = _safe_P(P)
    return qm * np.log1p(b * P)


def pinv_langmuir(pi, ctx, qm, b):
    if qm <= 0 or b <= 0:
        return np.nan
    return np.expm1(min(pi / qm, 700.0)) / b


def g_langmuir(P, q, ctx):
    qm = max(np.max(q) * 1.05, 1e-6)
    b = _initial_slope(P, q) / qm if qm > 0 else 0.1
    return [qm, max(b, 1e-4)]


def b_langmuir(P, q, ctx):
    return ([0.0, 0.0], [np.inf, np.inf])


# ------------------------------------------------- Langmuir bi-site (DSL) ---
def f_dsl(P, ctx, qm1, b1, qm2, b2):
    P = _safe_P(P)
    return qm1 * b1 * P / (1.0 + b1 * P) + qm2 * b2 * P / (1.0 + b2 * P)


def pi_dsl(P, ctx, qm1, b1, qm2, b2):
    P = _safe_P(P)
    return qm1 * np.log1p(b1 * P) + qm2 * np.log1p(b2 * P)


def g_dsl(P, q, ctx):
    qm = max(np.max(q) * 1.05, 1e-6)
    b = max(_initial_slope(P, q) / qm, 1e-4)
    return [0.5 * qm, 10.0 * b, 0.6 * qm, 0.1 * b]


def b_dsl(P, q, ctx):
    return ([0, 0, 0, 0], [np.inf] * 4)


# -------------------------------------------------------------- Freundlich --
def f_freundlich(P, ctx, KF, nF):
    P = _safe_P(P)
    return KF * np.power(P, nF, where=P > 0, out=np.zeros_like(P))


def pi_freundlich(P, ctx, KF, nF):
    P = _safe_P(P)
    return KF * np.power(P, nF, where=P > 0, out=np.zeros_like(P)) / nF


def pinv_freundlich(pi, ctx, KF, nF):
    if KF <= 0 or nF <= 0:
        return np.nan
    return (nF * pi / KF) ** (1.0 / nF)


def g_freundlich(P, q, ctx):
    try:
        m, c = np.polyfit(np.log(P[P > 0]), np.log(np.maximum(q[P > 0], 1e-12)), 1)
        return [float(np.exp(c)), float(np.clip(m, 0.05, 3.0))]
    except Exception:
        return [max(np.max(q), 1e-3), 0.5]


def b_freundlich(P, q, ctx):
    return ([0.0, 1e-4], [np.inf, 5.0])


# -------------------------------------------------------------------- Sips --
def f_sips(P, ctx, qm, b, ns):
    P = _safe_P(P)
    bp = b * P
    bpn = np.power(bp, ns, where=bp > 1e-300, out=np.zeros_like(bp))
    return qm * bpn / (1.0 + bpn)


def pi_sips(P, ctx, qm, b, ns):
    P = _safe_P(P)
    bp = b * P
    bpn = np.power(bp, ns, where=bp > 1e-300, out=np.zeros_like(bp))
    return (qm / ns) * np.log1p(bpn)


def pinv_sips(pi, ctx, qm, b, ns):
    if qm <= 0 or b <= 0 or ns <= 0:
        return np.nan
    val = np.expm1(min(ns * pi / qm, 700.0))
    return (val ** (1.0 / ns)) / b


def g_sips(P, q, ctx):
    qm = max(np.max(q) * 1.05, 1e-6)
    b = max(_initial_slope(P, q) / qm, 1e-4)
    return [qm, b, 0.9]


def b_sips(P, q, ctx):
    return ([0.0, 0.0, 1e-3], [np.inf, np.inf, 5.0])


# -------------------------------------------------------------------- Toth --
def f_toth(P, ctx, qm, b, t):
    P = _safe_P(P)
    bp = b * P
    bpt = np.power(bp, t, where=bp > 1e-300, out=np.zeros_like(bp))
    denom = np.power(1.0 + bpt, 1.0 / t)
    return qm * bp / denom


def g_toth(P, q, ctx):
    qm = max(np.max(q) * 1.05, 1e-6)
    b = max(_initial_slope(P, q) / qm, 1e-4)
    return [qm, b, 0.9]


def b_toth(P, q, ctx):
    return ([0.0, 0.0, 1e-3], [np.inf, np.inf, 3.0])


# ------------------------------------------- Dubinin-Astakhov / Radushkevich
def _da_core(P, T, P0, qm, E, n):
    """q = qm * exp( -( R T ln(P0/P) / E )^n ),  q = qm si P >= P0."""
    P = np.atleast_1d(np.asarray(P, dtype=float))
    out = np.zeros_like(P)
    valid = P > 0
    below = valid & (P < P0)
    above = valid & (P >= P0)
    if np.any(below):
        A = R_J * T * np.log(P0 / P[below])
        u = np.clip((A / E) ** n, 0.0, 700.0)
        out[below] = qm * np.exp(-u)
    out[above] = qm
    return out


def _pi_da_core(P, T, P0, qm, E, n):
    """pi* = qm E /(R T n) * Gamma(1/n) * Q(1/n, u^n),  u = R T ln(P0/P)/E."""
    P = np.atleast_1d(np.asarray(P, dtype=float))
    out = np.zeros_like(P)
    pref = qm * E / (R_J * T * n) * gamma_fn(1.0 / n)
    below = (P > 0) & (P < P0)
    above = P >= P0
    if np.any(below):
        u = R_J * T * np.log(P0 / P[below]) / E
        out[below] = pref * gammaincc(1.0 / n, np.clip(u ** n, 0.0, 700.0))
    if np.any(above):
        out[above] = pref + qm * np.log(P[above] / P0)
    return out


def f_da(P, ctx, qm, E, n):
    return _da_core(P, ctx["T"], ctx["P0"], qm, E, n)


def pi_da(P, ctx, qm, E, n):
    return _pi_da_core(P, ctx["T"], ctx["P0"], qm, E, n)


def g_da(P, q, ctx):
    return [max(np.max(q) * 1.05, 1e-6), 15000.0, 2.0]


def b_da(P, q, ctx):
    return ([0.0, 100.0, 0.3], [np.inf, 1e6, 6.0])


def f_da_p0(P, ctx, qm, E, n, P0):
    return _da_core(P, ctx["T"], P0, qm, E, n)


def pi_da_p0(P, ctx, qm, E, n, P0):
    return _pi_da_core(P, ctx["T"], P0, qm, E, n)


def g_da_p0(P, q, ctx):
    return [max(np.max(q) * 1.05, 1e-6), 15000.0, 2.0, float(np.max(P)) * 1.5]


def b_da_p0(P, q, ctx):
    return ([0.0, 100.0, 0.3, float(np.max(P)) * 1.001],
            [np.inf, 1e6, 6.0, np.inf])


def f_dr(P, ctx, qm, K):
    E = 1.0 / math.sqrt(max(K, 1e-30))
    return _da_core(P, ctx["T"], ctx["P0"], qm, E, 2.0)


def pi_dr(P, ctx, qm, K):
    E = 1.0 / math.sqrt(max(K, 1e-30))
    return _pi_da_core(P, ctx["T"], ctx["P0"], qm, E, 2.0)


def g_dr(P, q, ctx):
    T, P0 = ctx["T"], ctx["P0"]
    try:
        m = (P > 0) & (P < P0) & (q > 0)
        eps2 = (R_J * T * np.log(P0 / P[m])) ** 2
        s, c = np.polyfit(eps2, np.log(q[m]), 1)
        return [max(float(np.exp(c)), 1e-6), max(-float(s), 1e-12)]
    except Exception:
        return [max(np.max(q) * 1.05, 1e-6), 1e-9]


def b_dr(P, q, ctx):
    return ([0.0, 0.0], [np.inf, np.inf])


def f_dr_p0(P, ctx, qm, K, P0):
    E = 1.0 / math.sqrt(max(K, 1e-30))
    return _da_core(P, ctx["T"], P0, qm, E, 2.0)


def pi_dr_p0(P, ctx, qm, K, P0):
    E = 1.0 / math.sqrt(max(K, 1e-30))
    return _pi_da_core(P, ctx["T"], P0, qm, E, 2.0)


def g_dr_p0(P, q, ctx):
    g = g_dr(P, q, ctx)
    return g + [float(np.max(P)) * 1.5]


def b_dr_p0(P, q, ctx):
    return ([0.0, 0.0, float(np.max(P)) * 1.001], [np.inf, np.inf, np.inf])


def _initial_slope(P, q):
    """Estimation de la constante de Henry (pente initiale)."""
    P = np.asarray(P, float)
    q = np.asarray(q, float)
    idx = np.argsort(P)
    P, q = P[idx], q[idx]
    n = max(2, min(4, len(P)))
    try:
        s = np.polyfit(P[:n], q[:n], 1)[0]
        if s > 0:
            return float(s)
    except Exception:
        pass
    with np.errstate(divide="ignore", invalid="ignore"):
        r = q[P > 0] / P[P > 0]
    r = r[np.isfinite(r)]
    return float(np.max(r)) if r.size else 0.1


class Model:
    def __init__(self, key, label, pnames, punits, func, guess, bounds,
                 pi=None, pinv=None, needs=(), formula="", note=""):
        self.key = key
        self._label = label
        self.pnames = pnames
        self.punits = punits
        self.func = func
        self.guess = guess
        self.bounds = bounds
        self.pi = pi
        self.pinv = pinv
        self.needs = needs
        self.formula = formula
        self._note = note

    @property
    def label(self):
        return _(self._label)

    @property
    def note(self):
        return _(self._note) if self._note else self._note

    @property
    def nparam(self):
        return len(self.pnames)

    def derived(self, params, ctx):
        """Grandeurs derivees utiles (dictionnaire nom -> (valeur, unite))."""
        d = {}
        if self.key in ("dr", "dr_p0"):
            K = params[1]
            if K > 0:
                E = 1.0 / math.sqrt(K)
                d["E (energie caract.)"] = (E / 1000.0, "kJ/mol")
        if self.key in ("da", "da_p0"):
            d["E (energie caract.)"] = (params[1] / 1000.0, "kJ/mol")
        if self.key in ("langmuir", "sips", "toth"):
            d["K_H (Henry, approx.)"] = (params[0] * params[1], "mmol/g/bar")
        if self.key == "dsl":
            d["K_H (Henry)"] = (params[0] * params[1] + params[2] * params[3],
                                "mmol/g/bar")
            d["q_max total"] = (params[0] + params[2], "mmol/g")
        return d


MODELS = {}


def _reg(m):
    MODELS[m.key] = m


_reg(Model("langmuir", "Langmuir", ["q_max", "b"], ["mmol/g", "1/bar"],
           f_langmuir, g_langmuir, b_langmuir, pi_langmuir, pinv_langmuir,
           formula="q = q_max b P / (1 + b P)"))

_reg(Model("dsl", "Langmuir bi-site (DSL)",
           ["q_m1", "b1", "q_m2", "b2"],
           ["mmol/g", "1/bar", "mmol/g", "1/bar"],
           f_dsl, g_dsl, b_dsl, pi_dsl, None,
           formula="q = q_m1 b1 P/(1+b1 P) + q_m2 b2 P/(1+b2 P)"))

_reg(Model("freundlich", "Freundlich", ["K_F", "n_F"],
           ["mmol/g/bar^n", "-"],
           f_freundlich, g_freundlich, b_freundlich,
           pi_freundlich, pinv_freundlich,
           formula="q = K_F P^n_F",
           note="Pas de limite de saturation ; IAST valable seulement si "
                "n_F < 1 et loin de la saturation."))

_reg(Model("sips", "Sips (Langmuir-Freundlich)", ["q_max", "b", "n_s"],
           ["mmol/g", "1/bar", "-"],
           f_sips, g_sips, b_sips, pi_sips, pinv_sips,
           formula="q = q_max (bP)^n_s / (1 + (bP)^n_s)"))

_reg(Model("toth", "Toth", ["q_max", "b", "t"], ["mmol/g", "1/bar", "-"],
           f_toth, g_toth, b_toth, None, None,
           formula="q = q_max b P / (1 + (bP)^t)^(1/t)",
           note="Pression d'etalement calculee par integration numerique."))

_reg(Model("dr", "Dubinin-Radushkevich (P0 fixe)", ["q_m", "K"],
           ["mmol/g", "mol2/J2"],
           f_dr, g_dr, b_dr, pi_dr, None, needs=("T", "P0"),
           formula="q = q_m exp(-K eps^2),  eps = R T ln(P0/P)",
           note="Modele de remplissage de micropores : constante de Henry "
                "nulle => usage de l'IAST a tres basse pression a eviter."))

_reg(Model("dr_p0", "Dubinin-Radushkevich (P0 ajuste)", ["q_m", "K", "P0"],
           ["mmol/g", "mol2/J2", "bar"],
           f_dr_p0, g_dr_p0, b_dr_p0, pi_dr_p0, None, needs=("T",),
           formula="q = q_m exp(-K eps^2),  eps = R T ln(P0/P)"))

_reg(Model("da", "Dubinin-Astakhov (P0 fixe)", ["q_m", "E", "n"],
           ["mmol/g", "J/mol", "-"],
           f_da, g_da, b_da, pi_da, None, needs=("T", "P0"),
           formula="q = q_m exp(-(R T ln(P0/P)/E)^n)",
           note="Constante de Henry nulle => prudence avec l'IAST."))

_reg(Model("da_p0", "Dubinin-Astakhov (P0 ajuste)", ["q_m", "E", "n", "P0"],
           ["mmol/g", "J/mol", "-", "bar"],
           f_da_p0, g_da_p0, b_da_p0, pi_da_p0, None, needs=("T",),
           formula="q = q_m exp(-(R T ln(P0/P)/E)^n)"))

MODEL_ORDER = ["langmuir", "dsl", "freundlich", "sips", "toth",
               "dr", "dr_p0", "da", "da_p0"]


# =============================================================================
# 4. AJUSTEMENT NON LINEAIRE ET STATISTIQUES
# =============================================================================

WEIGHT_MODES = ["Aucune (moindres carres)", "1/q (poids intermediaire)",
                "1/q^2 (erreur relative)"]


def _perturb(p0, lb, ub, rng, span=0.8):
    """Point de depart aleatoire autour de p0 (jitter multiplicatif borne)."""
    out = []
    for i, v in enumerate(p0):
        base = v if abs(v) > 1e-12 else 1.0
        x = base * 10.0 ** rng.uniform(-span, span)
        lo = lb[i] if np.isfinite(lb[i]) else -np.inf
        hi = ub[i] if np.isfinite(ub[i]) else np.inf
        if np.isfinite(lo) and np.isfinite(hi):
            x = float(np.clip(x, lo + 1e-12, hi - 1e-12))
            if not np.isfinite(x):
                x = 0.5 * (lo + hi)
        elif np.isfinite(lo):
            x = max(x, lo + 1e-12)
        elif np.isfinite(hi):
            x = min(x, hi - 1e-12)
        out.append(float(x))
    return out


def fit_isotherm(model, P, q, ctx, p0=None, lower=None, upper=None,
                 weights="Aucune (moindres carres)", maxfev=50000,
                 n_starts=1, n_boot=0, seed=12345, progress=None):
    """Ajuste un modele sur (P, q). Retourne un dictionnaire de resultats.

    n_starts : nombre de departs (1 = depart unique ; >1 = multi-depart
               aleatoire pour echapper aux minima locaux).
    n_boot   : nombre de reechantillonnages bootstrap des residus pour les
               intervalles de confiance (0 = desactive).
    """
    P = np.asarray(P, dtype=float)
    q = np.asarray(q, dtype=float)
    m = np.isfinite(P) & np.isfinite(q) & (P > 0)
    P, q = P[m], q[m]
    if len(P) < model.nparam + 1:
        raise ValueError(_("Pas assez de points valides (%d) pour %d parametres.")
                         % (len(P), model.nparam))

    if p0 is None:
        p0 = model.guess(P, q, ctx)
    lb, ub = model.bounds(P, q, ctx)
    if lower is not None:
        lb = [lb[i] if lower[i] is None else lower[i] for i in range(len(lb))]
    if upper is not None:
        ub = [ub[i] if upper[i] is None else upper[i] for i in range(len(ub))]
    p0 = [float(np.clip(p0[i], lb[i] + 1e-15, ub[i] - 1e-15))
          if np.isfinite(ub[i]) else float(max(p0[i], lb[i] + 1e-15))
          for i in range(len(p0))]

    if weights.startswith("1/q^2"):
        sigma = np.maximum(np.abs(q), 1e-9)
    elif weights.startswith("1/q "):
        sigma = np.sqrt(np.maximum(np.abs(q), 1e-9))
    else:
        sigma = None

    def f(x, *pars):
        return np.asarray(model.func(x, ctx, *pars), dtype=float).ravel()

    def _ssr(pars):
        r = (q - f(P, *pars))
        if sigma is not None:
            r = r / sigma
        return float(np.sum(r ** 2))

    def _run(start):
        po, pc = curve_fit(f, P, q, p0=start, bounds=(lb, ub), sigma=sigma,
                           absolute_sigma=False, maxfev=maxfev)
        return po, pc, _ssr(po)

    rng = np.random.default_rng(seed)
    popt, pcov, best = None, None, np.inf
    n_ok, n_ko = 0, 0
    for it in range(max(1, int(n_starts))):
        start = p0 if it == 0 else _perturb(p0, lb, ub, rng)
        try:
            po, pc, ss = _run(start)
        except Exception:
            n_ko += 1
            continue
        n_ok += 1
        if ss < best * (1.0 - 1e-12):
            popt, pcov, best = po, pc, ss
    if popt is None:
        raise RuntimeError(_("aucun depart n'a converge (%d essais)")
                           % max(1, int(n_starts)))
    with np.errstate(invalid="ignore"):
        try:
            perr = np.sqrt(np.diag(pcov))
        except Exception:
            perr = np.full(len(popt), np.nan)

    # ------- matrice de correlation des parametres -------------------------
    k_ = len(popt)
    corr = np.full((k_, k_), np.nan)
    try:
        with np.errstate(invalid="ignore"):
            sd = np.sqrt(np.diag(pcov))
        if np.all(np.isfinite(sd)) and np.all(sd > 0):
            corr = pcov / np.outer(sd, sd)
            corr = np.clip(corr, -1.0, 1.0)
    except Exception:
        pass
    off = [abs(corr[i, j]) for i in range(k_) for j in range(i + 1, k_)
           if np.isfinite(corr[i, j])]
    rmax = float(max(off)) if off else np.nan

    qpred = f(P, *popt)
    res = q - qpred
    N, k = len(q), len(popt)
    SSR = float(np.sum(res ** 2))
    SST = float(np.sum((q - np.mean(q)) ** 2))
    R2 = 1.0 - SSR / SST if SST > 1e-15 else (1.0 if SSR < 1e-15 else 0.0)
    R2adj = (1.0 - (1.0 - R2) * (N - 1) / (N - k - 1)) if N - k - 1 > 0 else np.nan
    RMSE = math.sqrt(SSR / N)
    MSSR = SSR / N
    with np.errstate(divide="ignore", invalid="ignore"):
        ARE = np.abs(res / np.where(np.abs(q) > 1e-12, q, np.nan))
    ARE = float(np.nanmean(ARE) * 100.0)
    chi2 = float(np.nansum(res ** 2 / np.where(np.abs(qpred) > 1e-12,
                                               qpred, np.nan)))
    AIC = N * math.log(max(SSR / N, 1e-300)) + 2 * k
    AICc = AIC + (2 * k * (k + 1) / (N - k - 1)) if N - k - 1 > 0 else np.nan
    BIC = N * math.log(max(SSR / N, 1e-300)) + k * math.log(N)

    # ------- intervalles de confiance par bootstrap des residus ------------
    ci_lo = ci_hi = None
    boot_ok = 0
    if n_boot and n_boot >= 20:
        qhat = f(P, *popt)
        draws = []
        for ib in range(int(n_boot)):
            qs = qhat + rng.choice(res, size=len(res), replace=True)
            try:
                pb, _u = curve_fit(f, P, qs, p0=popt, bounds=(lb, ub),
                                  sigma=sigma, absolute_sigma=False,
                                  maxfev=maxfev)
                draws.append(pb)
            except Exception:
                pass
            if progress is not None and (ib + 1) % 25 == 0:
                progress(ib + 1, int(n_boot))
        if len(draws) >= 10:
            D = np.asarray(draws, dtype=float)
            boot_ok = len(draws)
            ci_lo = np.percentile(D, 2.5, axis=0).tolist()
            ci_hi = np.percentile(D, 97.5, axis=0).tolist()
            perr_boot = D.std(axis=0, ddof=1).tolist()
        else:
            perr_boot = None
    else:
        perr_boot = None

    return dict(model_key=model.key, params=[float(v) for v in popt],
                errors=[float(v) for v in perr], ctx=dict(ctx),
                corr=corr.tolist(), r_max=rmax,
                ci_lo=ci_lo, ci_hi=ci_hi, err_boot=perr_boot,
                n_boot=boot_ok, n_starts=int(max(1, n_starts)),
                starts_ok=n_ok, starts_ko=n_ko,
                P_exp_min=float(np.min(P)), P_exp_max=float(np.max(P)),
                stats=dict(N=N, R2=R2, R2adj=R2adj, SSR=SSR, MSSR=MSSR,
                           RMSE=RMSE, ARE=ARE, chi2=chi2, AIC=AIC,
                           AICc=AICc, BIC=BIC),
                P=P.tolist(), q=q.tolist(), qpred=qpred.tolist(),
                residuals=res.tolist(), weights=weights)


# =============================================================================
# 5. PRESSION D'ETALEMENT ET IAST
# =============================================================================

class SpreadingPressure:
    """pi* = (pi A)/(R T) = integrale de 0 a P de q(p)/p dp   [mmol/g]."""

    def __init__(self, model, ctx, params, P_lo=1e-10, P_hi=1e5, ngrid=2000,
                 P_exp_max=None):
        self.model = model
        self.ctx = dict(ctx) if ctx else {}
        self.params = [float(v) for v in params]
        # pression experimentale maximale du corps pur : sert a signaler
        # l'extrapolation implicite du modele lors du calcul IAST
        self.P_exp_max = (float(P_exp_max)
                          if P_exp_max and np.isfinite(P_exp_max) and P_exp_max > 0
                          else None)
        self._table = None
        if model.pi is None:
            self._build_table(P_lo, P_hi, ngrid)

    # -- integrande en y = ln(p) : q(e^y) --------------------------------
    def _integrand(self, y):
        v = self.model.func(np.exp(y), self.ctx, *self.params)
        return float(np.asarray(v, dtype=float).ravel()[0])

    def _build_table(self, P_lo, P_hi, ngrid):
        ygrid = np.linspace(math.log(P_lo), math.log(P_hi), ngrid)
        pig = np.zeros(ngrid)
        acc = quad(self._integrand, ygrid[0] - 34.0, ygrid[0], limit=200)[0]
        pig[0] = acc
        for i in range(1, ngrid):
            acc += quad(self._integrand, ygrid[i - 1], ygrid[i], limit=200)[0]
            pig[i] = acc
        self._table = (ygrid, np.maximum.accumulate(pig))

    def value(self, P):
        P = np.atleast_1d(np.asarray(P, dtype=float))
        if self.model.pi is not None:
            out = np.asarray(self.model.pi(P, self.ctx, *self.params),
                             dtype=float)
            return np.atleast_1d(out)
        ygrid, pig = self._table
        y = np.log(np.maximum(P, 1e-300))
        out = np.interp(y, ygrid, pig)
        # correction locale exacte : integration depuis le noeud inferieur
        inside = (y > ygrid[0]) & (y <= ygrid[-1])
        if np.any(inside):
            idx = np.searchsorted(ygrid, y[inside]) - 1
            idx = np.clip(idx, 0, len(ygrid) - 1)
            vals = []
            for k, i0 in enumerate(idx):
                y1 = float(np.atleast_1d(y[inside])[k])
                vals.append(pig[i0] + quad(self._integrand, ygrid[i0], y1,
                                           limit=100)[0])
            out[inside] = vals
        hi = y > ygrid[-1]
        if np.any(hi):
            base = pig[-1]
            out[hi] = [base + quad(self._integrand, ygrid[-1], float(v),
                                   limit=200)[0] for v in np.atleast_1d(y[hi])]
        lo = y < ygrid[0]
        if np.any(lo):
            out[lo] = pig[0] * np.exp(y[lo] - ygrid[0])
        return out

    def inverse(self, pi):
        """Retourne P0 tel que pi*(P0) = pi."""
        pi = float(pi)
        if pi <= 0:
            return 1e-300
        if self.model.pinv is not None:
            v = self.model.pinv(pi, self.ctx, *self.params)
            if np.isfinite(v) and v > 0:
                return float(v)
        if self.model.pi is None:
            ygrid, pig = self._table
            if pi <= pig[-1]:
                lp = float(np.interp(pi, pig, ygrid))
            else:
                slope = max((pig[-1] - pig[-2]) / (ygrid[-1] - ygrid[-2]), 1e-12)
                lp = float(ygrid[-1] + (pi - pig[-1]) / slope)
            # affinage de Newton : d(pi*)/d ln P = q(P)
            for _u in range(2):
                Pk = math.exp(lp)
                dq = float(self.q(Pk)[0])
                if dq <= 1e-14:
                    break
                lp -= (float(self.value(Pk)[0]) - pi) / dq
            return float(math.exp(lp))
        # inversion numerique d'une expression analytique de pi
        g = lambda t: float(self.value(math.exp(t))[0]) - pi
        t_hi, t_lo = 0.0, 0.0
        it = 0
        while g(t_hi) < 0 and it < 400:
            t_hi += 1.0
            it += 1
        it = 0
        while g(t_lo) > 0 and it < 400:
            t_lo -= 1.0
            it += 1
        try:
            return float(math.exp(brentq(g, t_lo, t_hi, xtol=1e-12,
                                         rtol=1e-12, maxiter=300)))
        except Exception:
            return np.nan

    def q(self, P):
        return np.atleast_1d(np.asarray(
            self.model.func(P, self.ctx, *self.params), dtype=float))


def iast_point(P_total, y, comps):
    """IAST pour un point de pression totale.

    comps : liste de SpreadingPressure (un par constituant)
    y     : fractions molaires en phase gaz (somme = 1)
    Retourne un dict : P0, x, q, q_total, pi, converged
    """
    n = len(comps)
    y = np.asarray(y, dtype=float)
    p_part = y * P_total
    act = [i for i in range(n) if y[i] > 1e-12]

    out = dict(P0=np.full(n, np.nan), x=np.zeros(n), q=np.zeros(n),
               q_total=np.nan, pi=np.nan, converged=False, message="")

    if P_total <= 0 or not act:
        out.update(converged=True, q_total=0.0, pi=0.0)
        return out

    def sum_x(t):
        pi = math.exp(t)
        s = 0.0
        for i in act:
            P0 = comps[i].inverse(pi)
            if not np.isfinite(P0) or P0 <= 0:
                return np.inf
            s += p_part[i] / P0
        return s

    g = lambda t: sum_x(t) - 1.0

    # encadrement de ln(pi)
    t_hi = 0.0
    it = 0
    while g(t_hi) > 0 and it < 500:
        t_hi += 0.5
        it += 1
    t_lo = t_hi
    it = 0
    while g(t_lo) < 0 and it < 500:
        t_lo -= 0.5
        it += 1
    if g(t_lo) < 0 or g(t_hi) > 0:
        out["message"] = _("Encadrement de la pression d'etalement impossible.")
        return out
    try:
        t = brentq(g, t_lo, t_hi, xtol=1e-13, rtol=1e-13, maxiter=400)
    except Exception as e:
        out["message"] = _("Echec du solveur : %s") % e
        return out

    pi = math.exp(t)
    P0 = np.full(n, np.nan)
    x = np.zeros(n)
    for i in act:
        P0[i] = comps[i].inverse(pi)
        x[i] = p_part[i] / P0[i]
    sx = x.sum()
    if sx > 1e-12:
        x = x / sx

    inv = 0.0
    ok = True
    for i in act:
        q0 = float(comps[i].q(P0[i])[0])
        if q0 <= 1e-12:
            ok = False
            break
        inv += x[i] / q0
    if not ok or inv <= 0:
        out["message"] = _("Quantite adsorbee pure nulle a P0.")
        return out
    q_tot = 1.0 / inv
    out.update(P0=P0, x=x, q=x * q_tot, q_total=q_tot, pi=pi, converged=True)
    return out


def iast_scan(P_totals, y, comps, names):
    """Balayage en pression totale. Retourne un DataFrame."""
    rows = []
    n = len(comps)
    for Pt in np.atleast_1d(np.asarray(P_totals, dtype=float)):
        r = iast_point(Pt, y, comps)
        ratios = []
        for i in range(n):
            pm = getattr(comps[i], "P_exp_max", None)
            ratios.append(r["P0"][i] / pm if (pm and np.isfinite(r["P0"][i]))
                          else np.nan)
        rmax = np.nanmax(ratios) if np.any(np.isfinite(ratios)) else np.nan
        row = {"P_total (bar)": Pt, "pi* (mmol/g)": r["pi"],
               "q_total (mmol/g)": r["q_total"],
               "Convergence": bool(r["converged"]),
               "Extrapolation max (P0/P_exp)": rmax}
        for i, nm in enumerate(names):
            row["y_%s" % nm] = y[i]
            row["p_%s (bar)" % nm] = y[i] * Pt
            row["P0_%s (bar)" % nm] = r["P0"][i]
            row["P0/P_exp_%s" % nm] = ratios[i]
            row["x_%s" % nm] = r["x"][i]
            row["q_%s (mmol/g)" % nm] = r["q"][i]
            # quantite pure a la pression partielle (reference sans competition)
            try:
                row["q_%s pur (mmol/g)" % nm] = float(comps[i].q(y[i] * Pt)[0])
            except Exception:
                row["q_%s pur (mmol/g)" % nm] = np.nan
        for i in range(n):
            for j in range(n):
                if i >= j:
                    continue
                si = selectivity(r["x"], y, i, j)
                row["S_%s/%s" % (names[i], names[j])] = si
                row["S_%s/%s" % (names[j], names[i])] = (
                    1.0 / si if (np.isfinite(si) and abs(si) > 1e-30)
                    else (0.0 if si == np.inf else np.nan))
        rows.append(row)
    return pd.DataFrame(rows)


def iast_scan_composition(P_total, y1_values, comps, names, y_rest=None):
    """Balayage en composition a pression totale fixee (binaire ou ternaire).

    y_rest : pour un ternaire, rapport fixe entre les constituants 2 et 3.
    """
    rows = []
    n = len(comps)
    for y1 in np.atleast_1d(np.asarray(y1_values, dtype=float)):
        y = np.zeros(n)
        y[0] = y1
        if n == 2:
            y[1] = 1.0 - y1
        else:
            rest = 1.0 - y1
            if y_rest is None:
                y[1:] = rest / (n - 1)
            else:
                w = np.asarray(y_rest, dtype=float)
                w = w / w.sum()
                y[1:] = rest * w
        r = iast_point(P_total, y, comps)
        ratios = []
        for i in range(n):
            pm = getattr(comps[i], "P_exp_max", None)
            ratios.append(r["P0"][i] / pm if (pm and np.isfinite(r["P0"][i]))
                          else np.nan)
        row = {"P_total (bar)": P_total, "q_total (mmol/g)": r["q_total"],
               "pi* (mmol/g)": r["pi"], "Convergence": bool(r["converged"]),
               "Extrapolation max (P0/P_exp)":
                   (np.nanmax(ratios) if np.any(np.isfinite(ratios)) else np.nan)}
        for i, nm in enumerate(names):
            row["y_%s" % nm] = y[i]
            row["x_%s" % nm] = r["x"][i]
            row["q_%s (mmol/g)" % nm] = r["q"][i]
            row["P0/P_exp_%s" % nm] = ratios[i]
        for i in range(n):
            for j in range(i + 1, n):
                row["S_%s/%s" % (names[i], names[j])] = selectivity(r["x"], y,
                                                                    i, j)
        rows.append(row)
    return pd.DataFrame(rows)


def selectivity(x, y, i, j):
    """S_i/j = (x_i/x_j) / (y_i/y_j)."""
    try:
        if y[i] <= 0 or y[j] <= 0:
            return np.nan
        if x[j] <= 1e-15:
            return np.inf if x[i] > 1e-15 else np.nan
        return float((x[i] / y[i]) / (x[j] / y[j]))
    except Exception:
        return np.nan


# =============================================================================
# 5 bis. CHALEUR ISOSTERIQUE D'ADSORPTION
# =============================================================================
# Deux methodes (voir Nuhnen & Janiak, Dalton Trans. 2020, 49, 10295) :
#  * Clausius-Clapeyron a quantite adsorbee constante, a partir des modeles
#    ajustes a chaque temperature :  Qst(n) = -R d ln f / d(1/T) |n
#    avec f la fugacite du gaz (f = P pour un gaz parfait) ;
#  * equation du viriel ajustee sur tous les points mesures :
#    ln P = ln n + (1/T) sum_i a_i n^i + sum_j b_j n^j ,  Qst(n) = -R sum a_i n^i
# Qst est donne positif en kJ/mol ; l'enthalpie d'adsorption vaut -Qst.

QST_BASES = ["Fugacite (gaz reel)", "Pression (gaz parfait)"]


def ln_phi_curve(T, gas, eos, P_max, npts=240):
    """Table (ln P, ln phi) du gaz pur a T, de ~0 a P_max (bar).

    ln phi = integrale de 0 a P de (Z - 1) d ln p, avec Z tire de la densite
    donnee par l'equation d'etat choisie (meme source que la conversion)."""
    P_max = max(float(P_max), 1e-6)
    if eos == "Gaz parfait":
        lp = np.log(np.array([P_max * 1e-6, P_max]))
        return lp, np.zeros(2)
    ps = np.geomspace(P_max * 1e-6, P_max, npts)
    z1 = np.array([eos_z_effective(T, p, gas, eos) - 1.0 for p in ps])
    lp = np.log(ps)
    cum = np.concatenate([[0.0], np.cumsum(0.5 * (z1[1:] + z1[:-1])
                                           * np.diff(lp))])
    # de 0 a ps[0], Z - 1 est proportionnel a p : l'integrale vaut Z(ps[0]) - 1
    return lp, cum + z1[0]


def fugacity_coefficient(T, P_bar, gas, eos="Peng-Robinson"):
    """Coefficient de fugacite phi = f/P du gaz pur."""
    if P_bar <= 0 or eos == "Gaz parfait":
        return 1.0
    lp, lphi = ln_phi_curve(T, gas, eos, P_bar)
    return float(math.exp(lphi[-1]))


def isotherm_pressure_at(model, ctx, params, n_target, P_lo, P_hi):
    """Pression (bar) telle que q(P) = n_target, cherchee entre P_lo et P_hi."""
    def g(t):
        v = model.func(np.array([math.exp(t)]), ctx, *params)
        return float(np.asarray(v, dtype=float).ravel()[0]) - n_target
    a = math.log(max(float(P_lo), 1e-12))
    b = math.log(max(float(P_hi), float(P_lo) * 1.0001, 1e-12))
    try:
        ga, gb = g(a), g(b)
    except Exception:
        return np.nan
    if not (np.isfinite(ga) and np.isfinite(gb)) or ga * gb > 0:
        return np.nan
    try:
        return float(math.exp(brentq(g, a, b, xtol=1e-12, rtol=1e-12,
                                     maxiter=300)))
    except Exception:
        return np.nan


def qst_common_range(entries):
    """Plage de quantites adsorbees couverte par TOUTES les isothermes."""
    lo = max(float(e["q_min"]) for e in entries)
    hi = min(float(e["q_max"]) for e in entries)
    return lo, hi


def qst_tables(entries, gas, basis=QST_BASES[0], eos="Peng-Robinson"):
    """Tables ln phi(ln P) de chaque isotherme (None en base pression)."""
    if basis != QST_BASES[0]:
        return [None] * len(entries)
    return [ln_phi_curve(float(e["T"]), gas, eos, float(e["P_max"]) * 1.05)
            for e in entries]


def qst_isostere(entries, tables, n):
    """Isostere a la quantite n : listes (1/T, ln f) et pressions par isotherme.

    Une isotherme n'est utilisee que si n est dans sa plage mesuree."""
    invT, ys, Ps = [], [], []
    for e, tab in zip(entries, tables):
        P = np.nan
        if float(e["q_min"]) - 1e-12 <= n <= float(e["q_max"]) + 1e-12:
            P = isotherm_pressure_at(MODELS[e["model_key"]], e["ctx"],
                                     e["params"], n, float(e["P_min"]) * 0.2,
                                     float(e["P_max"]) * 1.0001)
        Ps.append(P)
        if np.isfinite(P) and P > 0:
            y = math.log(P)
            if tab is not None:
                y += float(np.interp(math.log(P), tab[0], tab[1]))
            invT.append(1.0 / float(e["T"]))
            ys.append(y)
    return invT, ys, Ps


def qst_clausius_clapeyron(entries, n_values, gas, basis=QST_BASES[0],
                           eos="Peng-Robinson", tables=None):
    """Qst par Clausius-Clapeyron a partir des modeles ajustes.

    entries : liste de dict(name, T, model_key, params, ctx, P_min, P_max,
              q_min, q_max) - une isotherme ajustee par temperature.
    Avec 3 temperatures ou plus, la regression de ln f contre 1/T donne une
    incertitude-type sur Qst (sinon : formule a deux points, sans incertitude).
    """
    entries = sorted(entries, key=lambda e: float(e["T"]))
    if tables is None:
        tables = qst_tables(entries, gas, basis, eos)
    rows = []
    for n in np.atleast_1d(np.asarray(n_values, dtype=float)):
        invT, ys, Ps = qst_isostere(entries, tables, float(n))
        Q = uQ = r2 = np.nan
        k = len(invT)
        if k >= 2 and np.ptp(invT) > 0:
            X = np.asarray(invT)
            Y = np.asarray(ys)
            xm = X.mean()
            Sxx = float(np.sum((X - xm) ** 2))
            slope = float(np.sum((X - xm) * (Y - Y.mean())) / Sxx)
            icpt = float(Y.mean() - slope * xm)
            Q = -R_J * slope / 1000.0
            if k >= 3:
                res = Y - (icpt + slope * X)
                ssr = float(np.sum(res ** 2))
                uQ = R_J * math.sqrt(ssr / (k - 2) / Sxx) / 1000.0
                sst = float(np.sum((Y - Y.mean()) ** 2))
                r2 = 1.0 - ssr / sst if sst > 0 else np.nan
        row = {"n (mmol/g)": float(n), "Qst CC (kJ/mol)": Q,
               "u(Qst CC) (kJ/mol)": uQ, "R2 isostere": r2,
               "Nb isothermes": k}
        for e, P in zip(entries, Ps):
            row["P a %.2f K (bar)" % float(e["T"])] = P
        rows.append(row)
    return pd.DataFrame(rows)


def _virial_X(n, T, m, k):
    cols = [n ** i / T for i in range(m + 1)] + [n ** j for j in range(k + 1)]
    return np.column_stack(cols)


def virial_fit(points, m=None, k=None, gas="", basis=QST_BASES[1],
               eos="Peng-Robinson", m_max=6, k_max=3):
    """Ajuste ln P = ln n + (1/T) sum a_i n^i + sum b_j n^j (moindres carres).

    points : liste de (T, P (bar), n (mmol/g)) - les points mesures.
    m, k   : degres des polynomes a et b ; None => choix par AICc.
    """
    Ts, Ps, ns, ys = [], [], [], []
    for T, P, n in points:
        T = float(T)
        P = np.asarray(P, dtype=float)
        n = np.asarray(n, dtype=float)
        ok = np.isfinite(P) & np.isfinite(n) & (P > 0) & (n > 0)
        P, n = P[ok], n[ok]
        if P.size == 0:
            continue
        y = np.log(P)
        if basis == QST_BASES[0]:
            lp, lphi = ln_phi_curve(T, gas, eos, float(P.max()) * 1.01)
            y = y + np.interp(np.log(P), lp, lphi)
        Ts.append(np.full(P.size, T))
        Ps.append(P)
        ns.append(n)
        ys.append(y)
    if not ns:
        raise ValueError(_("Aucun point exploitable pour le viriel."))
    T = np.concatenate(Ts)
    n = np.concatenate(ns)
    lnf = np.concatenate(ys)
    Y = lnf - np.log(n)
    N = Y.size
    if len(np.unique(T)) < 2:
        raise ValueError(_("Le viriel demande des isothermes a au moins deux "
                         "temperatures."))
    ms = [int(m)] if m is not None else list(range(1, m_max + 1))
    ks = [int(k)] if k is not None else list(range(0, k_max + 1))
    best = None
    for mi in ms:
        for ki in ks:
            p = mi + ki + 2
            if p > N - 2:
                continue
            X = _virial_X(n, T, mi, ki)
            beta, *_u = np.linalg.lstsq(X, Y, rcond=None)
            ssr = float(np.sum((Y - X @ beta) ** 2))
            aicc = (N * math.log(max(ssr, 1e-300) / N) + 2 * p
                    + 2.0 * p * (p + 1) / max(N - p - 1, 1))
            if best is None or aicc < best[0] - 1e-9:
                best = (aicc, mi, ki, beta, ssr, X)
    if best is None:
        raise ValueError(_("Trop peu de points pour l'equation du viriel "
                         "(%d points).") % N)
    aicc, mi, ki, beta, ssr, X = best
    p = mi + ki + 2
    s2 = ssr / max(N - p, 1)
    try:
        cov = s2 * np.linalg.inv(X.T @ X)
    except np.linalg.LinAlgError:
        cov = s2 * np.linalg.pinv(X.T @ X)
    a = beta[:mi + 1]
    b = beta[mi + 1:]
    pred = np.log(n) + X @ beta
    sst = float(np.sum((lnf - lnf.mean()) ** 2))
    r2 = 1.0 - float(np.sum((lnf - pred) ** 2)) / sst if sst > 0 else np.nan
    temps = sorted(set(float(t) for t in T))
    KH = {t: float(math.exp(-b[0] - a[0] / t)) for t in temps}
    n_hi = min(float(np.max(nn)) for nn in ns)
    return dict(m=mi, k=ki, a=a.tolist(), b=b.tolist(),
                cov_a=cov[:mi + 1, :mi + 1].tolist(), cov=cov.tolist(),
                N=N, SSR=ssr, RMSE=math.sqrt(ssr / N), R2=r2, AICc=aicc,
                Qst0=-R_J * a[0] / 1000.0,
                u_Qst0=R_J * math.sqrt(max(cov[0, 0], 0.0)) / 1000.0,
                temps=temps, K_H=KH, n_max_common=n_hi,
                n_max=float(np.max(n)), basis=basis)


def virial_qst(vf, n_values):
    """Qst(n) et son incertitude-type a partir d'un ajustement du viriel."""
    n = np.atleast_1d(np.asarray(n_values, dtype=float))
    A = np.column_stack([n ** i for i in range(vf["m"] + 1)])
    a = np.asarray(vf["a"], dtype=float)
    C = np.asarray(vf["cov_a"], dtype=float)
    Q = -R_J * (A @ a) / 1000.0
    u = R_J * np.sqrt(np.maximum(np.einsum("ij,jk,ik->i", A, C, A), 0.0)) / 1000.0
    return Q, u


def virial_pressure(vf, n, T):
    """P (bar) predite par le viriel a la quantite n et a la temperature T
    (fugacite si l'ajustement a ete fait en fugacite)."""
    n = np.atleast_1d(np.asarray(n, dtype=float))
    X = _virial_X(n, np.full(n.size, float(T)), vf["m"], vf["k"])
    beta = np.concatenate([vf["a"], vf["b"]])
    return n * np.exp(X @ beta)


# =============================================================================
# 6. UTILITAIRES D'INTERFACE
# =============================================================================

def to_float(s):
    """Conversion robuste texte -> float (accepte la virgule decimale)."""
    if s is None:
        return np.nan
    if isinstance(s, (int, float, np.floating, np.integer)):
        return float(s)
    t = str(s).strip().replace(" ", "").replace(" ", "")
    if not t:
        return np.nan
    if "," in t and "." in t:
        t = t.replace(",", "")           # virgule = separateur de milliers
    else:
        t = t.replace(",", ".")
    t = t.replace("−", "-")
    try:
        return float(t)
    except ValueError:
        return np.nan


def to_float_or(x, default):
    """to_float avec valeur de repli (NaN et texte invalide -> default)."""
    v = to_float(x)
    try:
        return default if (v is None or not np.isfinite(v)) else float(v)
    except (TypeError, ValueError):
        return default


def fmt(v, nd=5):
    if v is None:
        return ""
    try:
        v = float(v)
    except (TypeError, ValueError):
        return str(v)
    if not np.isfinite(v):
        return "inf" if v > 0 else ("-inf" if v < 0 else "nan")
    if v != 0 and (abs(v) < 1e-3 or abs(v) >= 1e5):
        return ("%%.%de" % nd) % v
    return ("%%.%df" % nd) % v


class EditableTable(ttk.Frame):
    """Grille editable facon tableur (double-clic, Ctrl+V, Ctrl+C, Suppr)."""

    def __init__(self, master, columns, height=14, widths=None, nrows=0):
        super().__init__(master)
        self.columns = list(columns)
        self._editor = None
        vsb = ttk.Scrollbar(self, orient="vertical")
        hsb = ttk.Scrollbar(self, orient="horizontal")
        self.tree = ttk.Treeview(self, columns=self.columns, show="headings",
                                 height=height, selectmode="extended",
                                 yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.config(command=self.tree.yview)
        hsb.config(command=self.tree.xview)
        for i, c in enumerate(self.columns):
            w = (widths[i] if widths and i < len(widths) else 110)
            self.tree.heading(c, text=tr_col(c, True))
            # minwidth : une colonne ne s'ecrase plus, la barre horizontale
            # prend le relais quand le panneau est trop etroit
            self.tree.column(c, width=w, minwidth=w, anchor="e", stretch=True)
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.tree.bind("<Double-1>", self._begin_edit)
        self.tree.bind("<Return>", self._begin_edit)
        self.tree.bind("<Control-v>", self._paste)
        self.tree.bind("<Control-V>", self._paste)
        self.tree.bind("<Control-c>", self._copy)
        self.tree.bind("<Control-C>", self._copy)
        self.tree.bind("<Delete>", lambda e: self.delete_selected())
        for _u in range(nrows):
            self.add_row()

    # ------------------------------------------------------------ edition --
    def _begin_edit(self, event=None):
        self._close_editor()
        if event is not None and getattr(event, "x", None) is not None:
            row = self.tree.identify_row(event.y)
            col = self.tree.identify_column(event.x)
        else:
            sel = self.tree.selection()
            row = sel[0] if sel else None
            col = "#1"
        if not row or not col:
            return "break"
        try:
            cidx = int(col.replace("#", "")) - 1
        except ValueError:
            return "break"
        if cidx < 0 or cidx >= len(self.columns):
            return "break"
        bbox = self.tree.bbox(row, col)
        if not bbox:
            return "break"
        x, y, w, h = bbox
        val = self.tree.set(row, self.columns[cidx])
        ed = tk.Entry(self.tree, justify="right")
        ed.insert(0, val)
        ed.select_range(0, "end")
        ed.place(x=x, y=y, width=w, height=h)
        ed.focus_set()
        self._editor = (ed, row, cidx)
        ed.bind("<Return>", lambda e: self._commit(move=1))
        ed.bind("<Tab>", lambda e: self._commit(move=2))
        ed.bind("<Escape>", lambda e: self._close_editor())
        ed.bind("<FocusOut>", lambda e: self._commit(move=0))
        return "break"

    def _fire_change(self):
        cb = getattr(self, "on_change", None)
        if callable(cb):
            try:
                cb()
            except Exception:
                pass

    def _commit(self, move=0):
        if not self._editor:
            return "break"
        ed, row, cidx = self._editor
        try:
            value = ed.get()
        except Exception:
            value = ""
        self._editor = None
        try:
            ed.destroy()
        except Exception:
            pass
        try:
            old = self.tree.set(row, self.columns[cidx])
            self.tree.set(row, self.columns[cidx], value)
        except Exception:
            return "break"
        if value != old:
            self._fire_change()
        if move == 1:
            nxt = self.tree.next(row)
            if not nxt:
                nxt = self.add_row()
            self.tree.selection_set(nxt)
            self.tree.focus(nxt)
            self.tree.see(nxt)
        elif move == 2 and cidx + 1 < len(self.columns):
            self.tree.selection_set(row)
        return "break"

    def _close_editor(self):
        if self._editor:
            try:
                self._editor[0].destroy()
            except Exception:
                pass
            self._editor = None
        return "break"

    # ------------------------------------------------- copier / coller -----
    def _copy(self, event=None):
        rows = self.tree.selection() or self.tree.get_children()
        txt = "\n".join("\t".join(self.tree.set(r, c) for c in self.columns)
                        for r in rows)
        self.clipboard_clear()
        self.clipboard_append(txt)
        return "break"

    def _paste(self, event=None):
        try:
            data = self.clipboard_get()
        except Exception:
            return "break"
        block = parse_clipboard_block(data)
        if not block:
            return "break"
        sel = self.tree.selection()
        items = list(self.tree.get_children())
        start = items.index(sel[0]) if sel and sel[0] in items else len(items)
        for r, vals in enumerate(block):
            idx = start + r
            while idx >= len(self.tree.get_children()):
                self.add_row()
            item = self.tree.get_children()[idx]
            for c, v in enumerate(vals[:len(self.columns)]):
                self.tree.set(item, self.columns[c], v)
        self._fire_change()
        return "break"

    # ------------------------------------------------------------ donnees --
    def add_row(self, values=None):
        vals = list(values) if values else [""] * len(self.columns)
        vals = (vals + [""] * len(self.columns))[:len(self.columns)]
        return self.tree.insert("", "end", values=vals)

    def delete_selected(self):
        for r in self.tree.selection():
            self.tree.delete(r)
        self._fire_change()

    def clear(self):
        for r in self.tree.get_children():
            self.tree.delete(r)
        self._fire_change()

    def get_rows(self):
        return [[self.tree.set(r, c) for c in self.columns]
                for r in self.tree.get_children()]

    def set_rows(self, rows):
        self.clear()
        for r in rows:
            self.add_row(["" if v is None else
                          (fmt(v, 6) if isinstance(v, float) else str(v))
                          for v in r])
        self._fire_change()

    def get_numeric(self, ncols=None):
        ncols = ncols or len(self.columns)
        out = []
        for row in self.get_rows():
            vals = [to_float(row[i]) for i in range(ncols)]
            if all(np.isnan(v) for v in vals):
                continue
            out.append(vals)
        return np.array(out, dtype=float) if out else np.zeros((0, ncols))

    def sort_by(self, col_index=0):
        rows = self.get_rows()
        rows.sort(key=lambda r: (np.isnan(to_float(r[col_index])),
                                 to_float(r[col_index])))
        self.set_rows(rows)
        self._fire_change()

def parse_clipboard_block(data):
    """Decoupe un bloc colle depuis Excel/texte en liste de listes."""
    lines = [l for l in str(data).replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    block = []
    for line in lines:
        if not line.strip():
            continue
        if "\t" in line:
            cells = line.split("\t")
        elif ";" in line:
            cells = line.split(";")
        elif "," in line and line.count(",") > 1:
            cells = line.split(",")
        else:
            cells = line.split()
        block.append([c.strip() for c in cells])
    return block


class ScrollFrame(ttk.Frame):
    """Cadre defilant vertical et horizontal, avec molette de souris.

    Le contenu n'est jamais tronque : si le panneau est plus etroit que les
    widgets, une barre de defilement horizontale apparait.
    """

    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        canvas = tk.Canvas(self, highlightthickness=0, borderwidth=0)
        try:
            canvas.configure(background=UI["bg"])
        except Exception:
            pass
        vsb = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        hsb = ttk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        self.inner = ttk.Frame(canvas)
        self._win = canvas.create_window((0, 0), window=self.inner, anchor="nw")

        def _region():
            try:
                canvas.configure(scrollregion=canvas.bbox("all"))
            except Exception:
                pass

        def _content(_e=None):
            # une fois les enfants places : mesuree trop tot, la zone
            # defilante garde l'ancienne hauteur et le bas reste inaccessible
            _region()
            canvas.after_idle(_region)

        def _resize(e):
            try:
                canvas.itemconfigure(self._win,
                                     width=max(e.width,
                                               self.inner.winfo_reqwidth()))
            except Exception:
                pass
            _content()

        self.inner.bind("<Configure>", _content)
        canvas.bind("<Configure>", _resize)
        canvas.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        canvas.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        def _wheel(e):
            try:
                d = -1 if getattr(e, "delta", 0) > 0 else 1
                canvas.yview_scroll(d, "units")
            except Exception:
                pass
            return "break"

        def _bind(_=None):
            canvas.bind_all("<MouseWheel>", _wheel)

        def _unbind(_=None):
            try:
                canvas.unbind_all("<MouseWheel>")
            except Exception:
                pass

        canvas.bind("<Enter>", _bind)
        canvas.bind("<Leave>", _unbind)
        self.canvas = canvas


def set_sash(pan, index, pos):
    """Fixe la position d'un separateur une fois le panneau reellement affiche.

    Un onglet non visible n'a pas encore de largeur : y fixer le separateur
    est sans effet et le panneau s'ouvre replie. On applique donc la position
    au premier affichage du panneau (evenement <Map>), une seule fois, pour ne
    jamais ecraser un separateur que l'utilisateur a deplace ensuite.
    pos < 1 : fraction de la taille ; sinon pixels, plafonnes a la moitie
    pour qu'un panneau ne mange pas l'autre dans une petite fenetre.
    """
    state = {"done": False}

    def _do(_e=None):
        if state["done"]:
            return
        try:
            if not pan.winfo_ismapped():
                return
            size = (pan.winfo_width() if str(pan.cget("orient")) == "horizontal"
                    else pan.winfo_height())
            if size < 200:
                return
            pan.sashpos(index, int(pos * size) if pos < 1
                        else min(int(pos), size // 2))
            state["done"] = True
        except Exception:
            pass
    try:
        pan.after(150, _do)
        pan.after(600, _do)
        pan.bind("<Map>", lambda e: (pan.after(60, _do), pan.after(400, _do)),
                 add="+")
    except Exception:
        pass


def place_window(win, w=None, h=None):
    """Centre une fenetre secondaire sur la fenetre principale, sans sortir
    de l'ecran (taille demandee par son contenu si w et h sont omis)."""
    try:
        win.update_idletasks()
        top = win.master.winfo_toplevel()
        sw, sh = win.winfo_screenwidth(), win.winfo_screenheight() - 80
        w = min(w or win.winfo_reqwidth(), sw)
        h = min(h or win.winfo_reqheight(), sh)
        x = top.winfo_rootx() + (top.winfo_width() - w) // 2
        y = top.winfo_rooty() + (top.winfo_height() - h) // 2
        win.geometry("%dx%d+%d+%d" % (w, h, max(0, min(x, sw - w)),
                                      max(0, min(y, sh - h))))
    except Exception:
        pass


def make_canvas(parent, fig, zoom=None):
    """Canevas matplotlib, sa barre d'outils et le lien 'Agrandir'
    (zoom = (fonction de trace, titre, app)). La barre est placee avant le
    canevas : quand la place manque, c'est le graphique qui retrecit."""
    canvas = FigureCanvasTkAgg(fig, master=parent)
    row = ttk.Frame(parent, style="Card.TFrame")
    row.pack(side="bottom", fill="x")
    if zoom:
        zoom_button(row, *zoom).pack(side="right")
    if NavigationToolbar2Tk is not None:
        tb = NavigationToolbar2Tk(canvas, row, pack_toolbar=False)
        tb.update()
        # matplotlib reserve 50 px (deux lignes de texte) : une ligne suffit,
        # et le graphique y gagne en hauteur. Hauteur fixe pour les versions
        # recentes, texte de reserve raccourci pour les plus anciennes.
        tb.config(height=tb.winfo_pixels("26p"))
        for w in tb.winfo_children():
            if isinstance(w, tk.Label) and "\n" in str(w.cget("text")):
                w.config(text=" ")
        tb.pack(side="left", fill="x", expand=True)
    canvas.get_tk_widget().pack(fill="both", expand=True)
    return canvas


def panel_axes(fig, n, ratios=None, sharex=False):
    """n panneaux sur la figure : empiles si elle est assez haute (1,8 pouce
    par panneau), cote a cote sinon, pour rester lisibles en petite fenetre."""
    stacked = fig.get_size_inches()[1] >= 1.8 * n
    kw = ({"height_ratios" if stacked else "width_ratios": ratios}
          if ratios else None)
    return fig.subplots(n if stacked else 1, 1 if stacked else n,
                        sharex=sharex, squeeze=False, gridspec_kw=kw).ravel()


class FigureWindow(tk.Toplevel):
    """Fenetre independante et redimensionnable pour agrandir un graphique."""

    def __init__(self, master, title, render, size=(12.0, 7.5), app=None):
        super().__init__(master)
        self.title(title)
        place_window(self, 1250, 820)
        self.app = app
        self.render = render
        try:
            self.configure(bg=UI["bg"])
        except Exception:
            pass
        bar = ttk.Frame(self, style="Bar.TFrame", padding=(10, 6))
        bar.pack(fill="x")
        ttk.Label(bar, text=title, style="Head.TLabel").pack(side="left")
        ttk.Button(bar, text=_("Actualiser"), style="Ghost.TButton",
                   command=self.redraw).pack(side="right", padx=4)
        ttk.Button(bar, text=_("Enregistrer l'image..."), style="Primary.TButton",
                   command=self.save).pack(side="right")
        body = ttk.Frame(self, padding=8)
        body.pack(fill="both", expand=True)
        holder = ttk.Frame(body, style="Card.TFrame", padding=8)
        holder.pack(fill="both", expand=True)
        self.fig = Figure(figsize=size, dpi=100, facecolor=UI["card"])
        self.canvas = make_canvas(holder, self.fig)
        self.redraw()

    def redraw(self):
        try:
            self.render(self.fig)
            self.canvas.draw_idle()
        except Exception as e:
            messagebox.showerror(_("Graphique"), str(e), parent=self)

    def save(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".png", initialfile=_("figure.png"),
            filetypes=[("PNG", "*.png"), (_("PDF vectoriel"), "*.pdf"),
                       (_("SVG vectoriel"), "*.svg"), ("TIFF", "*.tif"),
                       ("JPEG", "*.jpg")])
        if not path:
            return
        try:
            self.fig.savefig(path, dpi=300, bbox_inches="tight",
                             facecolor="white")
        except Exception as e:
            messagebox.showerror(_("Export"), str(e), parent=self)
            return
        if self.app:
            self.app.log(_("Figure exportee : %s") % path)
        messagebox.showinfo(_("Export"), _("Figure enregistree :\n%s") % path,
                            parent=self)


def popup_menu(button, items):
    """Petit menu deroule sous un bouton ; items : (libelle, commande)."""
    m = tk.Menu(button, tearoff=0)
    for lab, cmd in items:
        m.add_command(label=lab, command=cmd)
    m.tk_popup(button.winfo_rootx(),
               button.winfo_rooty() + button.winfo_height())


def wrap_to_width(label):
    """Le texte du label passe a la ligne selon la largeur disponible."""
    label.bind("<Configure>", lambda e: label.config(
        wraplength=max(120, e.width - 8)), add="+")
    return label


def zoom_button(parent, render, title, app=None):
    """Bouton normalise 'Agrandir le graphique'."""
    b = ttk.Button(parent, text=_("Agrandir le graphique"),
                   style="Ghost.TButton",
                   command=lambda: FigureWindow(parent.winfo_toplevel(), title,
                                                render, app=app))
    tip(b, _("Ouvre le graphique dans une fenetre separee et redimensionnable, "
           "avec zoom, deplacement et export haute resolution"))
    return b


MARKERS = ["o", "s", "^", "v", "D", "<", ">", "p", "*", "h", "x", "+", "None"]
LINESTYLES = ["-", "--", "-.", ":", "None"]
PALETTE = ["#1f77b4", "#d62728", "#2ca02c", "#ff7f0e", "#9467bd", "#8c564b",
           "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "#000000"]
LEGEND_LOCS = ["best", "upper right", "upper left", "lower left",
               "lower right", "center right", "center left",
               "upper center", "lower center", "center"]


# =============================================================================
# 6bis. THEME, WIDGETS ET GESTION DE SESSION  (v2)
# =============================================================================

UI = dict(
    bg="#eef2f6", card="#ffffff", ink="#1b2733", muted="#63707e",
    accent="#0f6fa8", accent_hi="#1583c4", accent_lo="#0b5580",
    ok="#1c8b5a", ok_hi="#22a86d", warn="#b06a00", danger="#b3261e",
    danger_hi="#cf3a31", line="#cfd8e0", zebra="#f7fafc", sel="#d6e9f7",
)
FONT = "Segoe UI"


def apply_theme(root):
    """Theme clair moderne, coherent sur l'ensemble de l'application."""
    st = ttk.Style(root)
    try:
        st.theme_use("clam")
    except Exception:
        pass
    try:
        root.configure(bg=UI["bg"])
    except Exception:
        pass
    base = (FONT, 10)
    st.configure(".", font=base, background=UI["bg"], foreground=UI["ink"])
    st.configure("TFrame", background=UI["bg"])
    st.configure("Card.TFrame", background=UI["card"], relief="flat")
    st.configure("Bar.TFrame", background=UI["card"])
    st.configure("TLabel", background=UI["bg"], foreground=UI["ink"])
    st.configure("Card.TLabel", background=UI["card"], foreground=UI["ink"])
    st.configure("Title.TLabel", font=(FONT, 15, "bold"), background=UI["card"],
                 foreground=UI["ink"])
    st.configure("Head.TLabel", font=(FONT, 10, "bold"), background=UI["card"],
                 foreground=UI["accent_lo"])
    st.configure("Muted.TLabel", font=(FONT, 9), background=UI["card"],
                 foreground=UI["muted"])
    st.configure("MutedBg.TLabel", font=(FONT, 9), background=UI["bg"],
                 foreground=UI["muted"])
    st.configure("Status.TLabel", font=(FONT, 9), background=UI["card"],
                 foreground=UI["muted"])
    st.configure("TLabelframe", background=UI["card"], borderwidth=1,
                 relief="solid", bordercolor=UI["line"])
    st.configure("TLabelframe.Label", font=(FONT, 10, "bold"),
                 background=UI["card"], foreground=UI["accent_lo"])
    st.configure("TButton", padding=(10, 6), relief="flat",
                 background="#e3eaf1", foreground=UI["ink"], borderwidth=0)
    st.map("TButton", background=[("active", "#d2dde7"),
                                  ("pressed", "#c2d0dd"),
                                  ("disabled", "#eceff2")])
    for name, col, hi in (("Primary", UI["accent"], UI["accent_hi"]),
                          ("Success", UI["ok"], UI["ok_hi"]),
                          ("Danger", UI["danger"], UI["danger_hi"])):
        st.configure("%s.TButton" % name, background=col, foreground="white",
                     padding=(14, 7), font=(FONT, 10, "bold"), borderwidth=0,
                     relief="flat")
        st.map("%s.TButton" % name,
               background=[("active", hi), ("pressed", hi),
                           ("disabled", "#b9c4cf")],
               foreground=[("disabled", "#eef2f6")])
    st.configure("Ghost.TButton", background=UI["card"], foreground=UI["accent"],
                 padding=(9, 5), borderwidth=0, relief="flat")
    st.map("Ghost.TButton", background=[("active", UI["sel"])])
    st.configure("Tool.TButton", background=UI["card"], foreground=UI["ink"],
                 padding=(11, 7), borderwidth=0, relief="flat",
                 font=(FONT, 10))
    st.map("Tool.TButton", background=[("active", UI["sel"]),
                                       ("pressed", UI["sel"])])
    st.configure("Step.TLabel", background=UI["card"], foreground=UI["muted"],
                 font=(FONT, 10), padding=(14, 7))
    st.configure("StepOn.TLabel", background=UI["accent"], foreground="white",
                 font=(FONT, 10, "bold"), padding=(14, 7))
    st.configure("StepDone.TLabel", background="#dceaf5",
                 foreground=UI["accent_lo"], font=(FONT, 10), padding=(14, 7))
    st.configure("Treeview", background="white", fieldbackground="white",
                 foreground=UI["ink"], rowheight=25, borderwidth=0,
                 font=(FONT, 9))
    st.configure("Treeview.Heading", font=(FONT, 9, "bold"), padding=(6, 5),
                 background="#e3eaf1", foreground=UI["ink"], relief="flat")
    st.map("Treeview", background=[("selected", UI["accent"])],
           foreground=[("selected", "white")])
    st.configure("TNotebook", background=UI["bg"], borderwidth=0, tabmargins=0)
    st.configure("TNotebook.Tab", padding=(0, 0), background=UI["bg"],
                 borderwidth=0)
    try:
        st.layout("Hidden.TNotebook.Tab", [])   # onglets masques : navigation
    except Exception:                            # par la barre d'etapes
        pass
    st.configure("TCombobox", padding=4)
    st.configure("TEntry", padding=4, fieldbackground="white")
    st.configure("TCheckbutton", background=UI["card"], foreground=UI["ink"])
    st.configure("CheckBg.TCheckbutton", background=UI["bg"])
    st.configure("TRadiobutton", background=UI["card"])
    st.configure("Horizontal.TProgressbar", background=UI["accent"],
                 troughcolor="#e3eaf1", borderwidth=0)
    st.configure("TPanedwindow", background=UI["bg"])
    st.configure("Sash", sashthickness=8)
    return st


class Tooltip:
    """Info-bulle legere pour n'importe quel widget."""

    def __init__(self, widget, text, delay=450):
        self.widget = widget
        self.text = text
        self.delay = delay
        self.tip = None
        self._id = None
        try:
            widget.bind("<Enter>", self._enter, add="+")
            widget.bind("<Leave>", self._leave, add="+")
            widget.bind("<ButtonPress>", self._leave, add="+")
        except Exception:
            pass

    def _enter(self, _=None):
        self._cancel()
        try:
            self._id = self.widget.after(self.delay, self._show)
        except Exception:
            pass

    def _cancel(self):
        if self._id:
            try:
                self.widget.after_cancel(self._id)
            except Exception:
                pass
            self._id = None

    def _show(self):
        if self.tip or not self.text:
            return
        try:
            x = self.widget.winfo_rootx() + 18
            y = self.widget.winfo_rooty() + self.widget.winfo_height() + 6
            self.tip = tk.Toplevel(self.widget)
            self.tip.wm_overrideredirect(True)
            self.tip.wm_geometry("+%d+%d" % (x, y))
            tk.Label(self.tip, text=self.text, justify="left",
                     background="#2b3a47", foreground="white",
                     font=(FONT, 9), padx=9, pady=6, wraplength=380).pack()
        except Exception:
            self.tip = None

    def _leave(self, _=None):
        self._cancel()
        if self.tip:
            try:
                self.tip.destroy()
            except Exception:
                pass
            self.tip = None


def tip(widget, text):
    Tooltip(widget, text)
    return widget


def card(parent, title=None, subtitle=None, **kw):
    """Bloc blanc avec titre : unite visuelle de base de l'interface."""
    outer = ttk.Frame(parent, style="Card.TFrame", padding=kw.pop("padding", 12))
    if title:
        head = ttk.Frame(outer, style="Card.TFrame")
        head.pack(fill="x", pady=(0, 8))
        ttk.Label(head, text=title, style="Head.TLabel").pack(side="left")
        if subtitle:
            ttk.Label(head, text="  " + subtitle,
                      style="Muted.TLabel").pack(side="left")
        sep = tk.Frame(outer, height=1, bg=UI["line"])
        sep.pack(fill="x", pady=(0, 10))
    body = ttk.Frame(outer, style="Card.TFrame")
    body.pack(fill="both", expand=True)
    outer.body = body
    return outer


def field(parent, label, widget_cls=None, width=14, row=0, col=0, hint=None,
          **kw):
    """Etiquette + champ alignes dans une grille."""
    ttk.Label(parent, text=label, style="Card.TLabel").grid(
        row=row, column=col, sticky="w", padx=(0, 6), pady=3)
    w = (widget_cls or ttk.Entry)(parent, width=width, **kw)
    w.grid(row=row, column=col + 1, sticky="w", pady=3)
    if hint:
        tip(w, hint)
    return w


class StepBar(ttk.Frame):
    """Barre d'etapes cliquable indiquant la progression du flux de travail."""

    def __init__(self, master, steps, command=None):
        super().__init__(master, style="Bar.TFrame", padding=(10, 6))
        self.command = command
        self.labels = []
        for i, txt in enumerate(steps):
            if i:
                ttk.Label(self, text="\u203a", style="Muted.TLabel").pack(
                    side="left", padx=2)
            lb = ttk.Label(self, text=" %d. %s " % (i + 1, _(txt)),
                           style="Step.TLabel", cursor="hand2")
            lb.pack(side="left")
            lb.bind("<Button-1>", lambda e, k=i: self._click(k))
            self.labels.append(lb)

    def _click(self, i):
        if self.command:
            self.command(i)

    def set_active(self, idx):
        for i, lb in enumerate(self.labels):
            lb.configure(style="StepOn.TLabel" if i == idx else
                         ("StepDone.TLabel" if i < idx else "Step.TLabel"))


# ----------------------------------------------------------------------------
# Preferences persistantes et fichiers recents
# ----------------------------------------------------------------------------

def resource_path(name):
    """Chemin d'une ressource, y compris depuis un executable PyInstaller."""
    base = getattr(sys, "_MEIPASS", None) or os.path.dirname(
        os.path.abspath(__file__))
    return os.path.join(base, name)


def config_dir():
    """Dossier de configuration selon le systeme."""
    if sys.platform.startswith("win"):
        base = os.environ.get("APPDATA") or os.path.expanduser("~")
    elif sys.platform == "darwin":
        base = os.path.expanduser("~/Library/Application Support")
    else:
        base = os.environ.get("XDG_CONFIG_HOME") or os.path.expanduser("~/.config")
    d = os.path.join(base, APP_NAME)
    try:
        os.makedirs(d, exist_ok=True)
    except Exception:
        d = os.path.expanduser("~")
    return d


SETTINGS_FILE = "settings.json"


def load_settings():
    try:
        with open(os.path.join(config_dir(), SETTINGS_FILE), "r",
                  encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return {}


def save_settings(d):
    try:
        with open(os.path.join(config_dir(), SETTINGS_FILE), "w",
                  encoding="utf-8") as fh:
            json.dump(d, fh, indent=1, ensure_ascii=False)
    except Exception:
        pass


# ----------------------------------------------------------------------------
# Fichier de session complet (.adsp)
# ----------------------------------------------------------------------------

SESSION_EXT = ".adsp"


def collect_session(app):
    """Rassemble la totalite de l'etat de travail dans un dictionnaire."""
    iast = None
    df = getattr(app.tab_iast, "df", None)
    if df is not None:
        iast = dict(columns=list(df.columns),
                    rows=df.astype(object).where(pd.notnull(df), None
                                                 ).values.tolist(),
                    names=list(getattr(app.tab_iast, "names", [])),
                    specs=copy.deepcopy(getattr(app.tab_iast, "specs", [])),
                    mode=getattr(app.tab_iast, "mode", "P"))
    tp = app.tab_plot
    plot = {}
    try:
        plot = dict(title=tp.v_title.get(), xlab=tp.v_xlab.get(),
                    ylab=tp.v_ylab.get(), y2lab=tp.v_y2lab.get(),
                    xmin=tp.v_xmin.get(), xmax=tp.v_xmax.get(),
                    ymin=tp.v_ymin.get(), ymax=tp.v_ymax.get(),
                    logx=bool(tp.v_logx.get()), logy=bool(tp.v_logy.get()),
                    grid=bool(tp.v_grid.get()), leg=bool(tp.v_leg.get()),
                    loc=tp.cb_loc.get(), fs=tp.v_fs.get(), w=tp.v_w.get(),
                    h=tp.v_h.get(), dpi=tp.v_dpi.get(),
                    annotations=tp.tbl_ann.get_rows())
    except Exception:
        pass
    iast_rows = []
    try:
        for r in app.tab_iast.rows:
            iast_rows.append(dict(name=r.e_name.get(), y=r.e_y.get(),
                                  spec=copy.deepcopy(r.spec),
                                  fit=list(r.fit) if r.fit else None))
    except Exception:
        pass
    return dict(
        format="%s session" % APP_NAME, version=APP_VERSION,
        saved=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        datasets=copy.deepcopy(app.datasets),
        fits=copy.deepcopy(app.fits),
        series=[{k: (list(map(float, v)) if k in ("x", "y") else v)
                 for k, v in s.items()} for s in app.series],
        iast=iast, iast_rows=iast_rows, plot=plot,
        iast_n=int(app.tab_iast.var_n.get()),
        qst=(app.tab_qst.to_session() if hasattr(app, "tab_qst") else None),
        notes=getattr(app, "notes", ""),
        active_tab=int(getattr(app, "_last_tab", 0)))


def write_session(app, path):
    """Ecrit la session ; conserve une copie .bak de la version precedente."""
    data = collect_session(app)
    # le nouveau fichier d'abord : si l'ecriture echoue, l'ancien reste en place
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=1, ensure_ascii=False, default=float)
    if os.path.exists(path):
        try:
            os.replace(path, path + ".bak")
        except Exception:
            pass
    os.replace(tmp, path)
    return data


def read_session(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def restore_session(app, data):
    """Restaure integralement l'etat de travail depuis un dictionnaire."""
    app.datasets = data.get("datasets", []) or []
    app.fits = data.get("fits", []) or []
    app.series = [{k: (np.asarray(v, float) if k in ("x", "y") else v)
                   for k, v in s.items()} for s in data.get("series", []) or []]
    app.notes = data.get("notes", "")
    # IAST
    it = app.tab_iast
    it.reset()
    d = data.get("iast")
    if d and d.get("columns"):
        try:
            it.df = pd.DataFrame(d["rows"], columns=d["columns"])
            it.names = d.get("names", [])
            it.specs = d.get("specs", [])
            it.mode = d.get("mode", "P")
            it.fill_table(it.df)
            if it.names:
                it.draw(it.df, it.names)
        except Exception:
            it.df = None
    # nombre de constituants : enregistre depuis la 3.2, sinon celui du
    # dernier calcul
    n = data.get("iast_n") or len(it.names)
    if n in (2, 3):
        it.var_n.set(n)
        it._n_changed()
    for row, r in zip(it.rows, data.get("iast_rows", []) or []):
        try:
            row.e_name.delete(0, "end")
            row.e_name.insert(0, r.get("name", ""))
            row.e_y.delete(0, "end")
            row.e_y.insert(0, r.get("y", ""))
            row.spec = r.get("spec")
            row.fit = tuple(r["fit"]) if r.get("fit") else None
            if row.spec and not row.fit:
                # session d'avant la 3.2 : retrouver l'ajustement d'origine
                for f in app.fits:
                    if (f["model_key"] == row.spec["model_key"]
                            and np.allclose(f["params"], row.spec["params"])):
                        row.fit = (f["dataset"], f["model_key"])
                        break
            row._update_label()
        except Exception:
            pass
    # chaleur isosterique
    try:
        app.tab_qst.from_session(data.get("qst"))
    except Exception:
        pass
    # graphique
    p = data.get("plot") or {}
    tp = app.tab_plot
    try:
        for key, var in (("title", tp.v_title), ("xlab", tp.v_xlab),
                         ("ylab", tp.v_ylab), ("y2lab", tp.v_y2lab),
                         ("xmin", tp.v_xmin), ("xmax", tp.v_xmax),
                         ("ymin", tp.v_ymin), ("ymax", tp.v_ymax),
                         ("fs", tp.v_fs), ("w", tp.v_w), ("h", tp.v_h),
                         ("dpi", tp.v_dpi)):
            if key in p:
                var.set(p[key])
        for key, var in (("logx", tp.v_logx), ("logy", tp.v_logy),
                         ("grid", tp.v_grid), ("leg", tp.v_leg)):
            if key in p:
                var.set(bool(p[key]))
        if p.get("loc"):
            tp.cb_loc.set(p["loc"])
        if p.get("annotations"):
            tp.tbl_ann.set_rows(p["annotations"])
    except Exception:
        pass
    return dict(datasets=len(app.datasets), fits=len(app.fits),
                series=len(app.series),
                iast=(len(app.tab_iast.df) if getattr(app.tab_iast, "df", None)
                      is not None else 0))


# =============================================================================
# 7. ONGLET 1 : DONNEES
# =============================================================================

class ImportDialog(tk.Toplevel):
    """Selection de feuille, colonnes et unites lors d'un import."""

    def __init__(self, master, path):
        super().__init__(master)
        self.title(_("Import de donnees - %s") % os.path.basename(path))
        self.transient(master)
        self.grab_set()
        self.result = None
        self.path = path
        self.sheets = {}

        ext = os.path.splitext(path)[1].lower()
        try:
            if ext in (".csv", ".txt", ".dat"):
                try:
                    df = pd.read_csv(path, sep=None, engine="python",
                                     decimal=".")
                    if df.shape[1] < 2:
                        raise ValueError
                except Exception:
                    df = pd.read_csv(path, sep=None, engine="python",
                                     decimal=",")
                self.sheets = {"CSV": df}
            else:
                self.sheets = pd.read_excel(path, sheet_name=None)
        except Exception as e:
            messagebox.showerror(_("Import"), _("Lecture impossible :\n%s") % e,
                                 parent=master)
            self.destroy()
            return

        frm = ttk.Frame(self, padding=10)
        frm.pack(fill="both", expand=True)
        r = 0
        ttk.Label(frm, text=_("Feuille :")).grid(row=r, column=0, sticky="w")
        self.cb_sheet = TCombobox(frm, values=list(self.sheets.keys()),
                                     state="readonly", width=28)
        self.cb_sheet.grid(row=r, column=1, sticky="w", padx=4, pady=2)
        self.cb_sheet.current(0)
        self.cb_sheet.bind("<<ComboboxSelected>>", lambda e: self._sheet_changed())
        r += 1
        ttk.Label(frm, text=_("Colonne pression :")).grid(row=r, column=0, sticky="w")
        self.cb_p = TCombobox(frm, state="readonly", width=28)
        self.cb_p.grid(row=r, column=1, sticky="w", padx=4, pady=2)
        ttk.Label(frm, text=_("Unite :")).grid(row=r, column=2, sticky="e")
        self.cb_up = TCombobox(frm, values=list(P_UNITS.keys()),
                                  state="readonly", width=10)
        self.cb_up.grid(row=r, column=3, sticky="w", padx=4)
        self.cb_up.set("bar")
        r += 1
        ttk.Label(frm, text=_("Colonne quantite :")).grid(row=r, column=0, sticky="w")
        self.cb_q = TCombobox(frm, state="readonly", width=28)
        self.cb_q.grid(row=r, column=1, sticky="w", padx=4, pady=2)
        ttk.Label(frm, text=_("Unite :")).grid(row=r, column=2, sticky="e")
        self.cb_uq = TCombobox(frm, values=Q_UNITS, state="readonly", width=12)
        self.cb_uq.grid(row=r, column=3, sticky="w", padx=4)
        self.cb_uq.set("mmol/g")
        r += 1
        ttk.Label(frm, text=_("Gaz :")).grid(row=r, column=0, sticky="w")
        gas = guess_gas_from_name(path)
        self.cb_gas = TCombobox(frm, values=GAS_LIST, width=12)
        self.cb_gas.grid(row=r, column=1, sticky="w", padx=4, pady=2)
        self.cb_gas.set(gas or "CO2")
        ttk.Label(frm, text="T (K) :").grid(row=r, column=2, sticky="e")
        self.e_T = ttk.Entry(frm, width=12)
        self.e_T.insert(0, fmt(guess_temperature_from_name(path) or 298.15, 2))
        self.e_T.grid(row=r, column=3, sticky="w", padx=4)
        r += 1
        ttk.Label(frm, text=_("Nom du jeu :")).grid(row=r, column=0, sticky="w")
        self.e_name = ttk.Entry(frm, width=30)
        self.e_name.insert(0, dataset_name_from_file(path, gas))
        self.e_name.grid(row=r, column=1, sticky="w", padx=4, pady=2)
        ttk.Label(frm, text=_("Type :")).grid(row=r, column=2, sticky="e")
        self.cb_kind = TCombobox(frm, values=["Exces", "Total"],
                                    state="readonly", width=10)
        self.cb_kind.set("Exces")
        self.cb_kind.grid(row=r, column=3, sticky="w", padx=4)
        r += 1
        self.txt = tk.Text(frm, height=10, width=90, font=("Consolas", 8))
        self.txt.grid(row=r, column=0, columnspan=4, sticky="nsew", pady=6)
        frm.rowconfigure(r, weight=1)
        r += 1
        bar = ttk.Frame(frm)
        bar.grid(row=r, column=0, columnspan=4, sticky="e")
        ttk.Button(bar, text=_("Annuler"), command=self.destroy).pack(side="right",
                                                                   padx=4)
        ttk.Button(bar, text=_("Importer"), style="Primary.TButton",
                   command=self._ok).pack(side="right")
        self._sheet_changed()
        place_window(self)
        self.wait_window(self)

    def _sheet_changed(self):
        df = self.sheets[self.cb_sheet.get()]
        cols = [str(c) for c in df.columns]
        self.cb_p["values"] = cols
        self.cb_q["values"] = cols
        gp = [c for c in cols if any(k in c.lower()
                                     for k in ("press", "p ", "p(", "bar"))]
        gq = [c for c in cols if any(k in c.lower()
                                     for k in ("adsorb", "quant", "n_", "uptake",
                                               "mmol", "excess", "exces"))]
        self.cb_p.set(gp[0] if gp else (cols[0] if cols else ""))
        self.cb_q.set(gq[0] if gq else (cols[1] if len(cols) > 1 else ""))
        self.txt.delete("1.0", "end")
        self.txt.insert("1.0", df.head(12).to_string())

    def _ok(self):
        df = self.sheets[self.cb_sheet.get()]
        try:
            P = pd.to_numeric(df[self.cb_p.get()], errors="coerce").values
            q = pd.to_numeric(df[self.cb_q.get()], errors="coerce").values
        except Exception as e:
            messagebox.showerror(_("Import"), str(e), parent=self)
            return
        m = np.isfinite(P) & np.isfinite(q)
        self.result = dict(name=self.e_name.get().strip() or _("Jeu importe"),
                           gas=self.cb_gas.get().strip() or "CO2",
                           T=to_float_or(self.e_T.get(), 298.15),
                           kind=self.cb_kind.get(),
                           unit_p=self.cb_up.get(), unit_q=self.cb_uq.get(),
                           P_raw=P[m].tolist(), q_raw=q[m].tolist(),
                           note=_("Importe de %s") % os.path.basename(self.path))
        self.destroy()


def make_dataset(name, gas, T, kind, unit_p, unit_q, P_raw, q_raw, note=""):
    M = GAS_DB.get(gas, {}).get("M", 44.01)
    P_bar = np.asarray(P_raw, float) * P_UNITS.get(unit_p, 1.0)
    q_mm = q_to_mmol_g(np.asarray(q_raw, float), unit_q, M)
    return dict(name=name, gas=gas, T=float(T), kind=kind, note=note,
                unit_p=unit_p, unit_q=unit_q,
                P_raw=list(map(float, np.asarray(P_raw, float))),
                q_raw=list(map(float, np.asarray(q_raw, float))),
                P=list(map(float, P_bar)), q=list(map(float, q_mm)))



# -----------------------------------------------------------------------------
# Import en lot : deduction du gaz / de l'echantillon a partir du nom de fichier
# -----------------------------------------------------------------------------

_B = r"(?<![a-z0-9])%s(?![a-z0-9])"      # mot isole (ni lettre ni chiffre autour)
_GAS_PATTERNS = [
    ("CO2", (r"co2", r"co_2", r"carbon.?diox")),
    ("CH4", (r"ch4", r"ch_4", r"methan")),
    ("C2H2", (r"c2h2", r"acetyl", r"ethyne")),
    ("C2H4", (r"c2h4", r"ethylen", r"ethene")),
    ("C2H6", (r"c2h6", r"(?<!m)ethane")),
    ("C3H6", (r"c3h6", r"propylen", r"propene")),
    ("C3H8", (r"c3h8", r"propane")),
    ("i-C4H10", (r"i-?c4h10", r"iso.?butan")),
    ("n-C4H10", (r"n-?c4h10", r"(?<!iso)(?<!iso-)(?<!iso )butan")),
    ("SF6", (r"sf6",)),
    ("N2O", (r"n2o", r"nitrous")),
    ("NH3", (r"nh3", r"ammoni")),
    ("H2S", (r"h2s",)),
    ("SO2", (r"so2",)),
    ("H2O", (r"h2o", r"water", r"vapeur.?d.?eau")),
    ("D2",  (_B % "d2", r"deuter")),
    ("H2",  (_B % "h2", r"hydrog")),
    ("N2",  (_B % "n2", r"azote", r"nitrog")),
    ("CO",  (_B % "co",)),
    ("Ar",  (_B % "ar", r"argon")),
    ("O2",  (_B % "o2", r"oxyg")),
    ("Kr",  (_B % "kr", r"krypton")),
    ("Xe",  (_B % "xe", r"xenon")),
    ("He",  (_B % "he", r"helium")),
    ("Ne",  (_B % "ne", r"neon")),
]


def _gas_match(name):
    """(gaz, debut, fin) du premier motif reconnu dans le nom de fichier."""
    low = os.path.splitext(os.path.basename(name))[0].lower()
    import re as _re
    for gas, pats in _GAS_PATTERNS:
        for pat in pats:
            m = _re.search(pat, low)
            if m:
                return gas, m.start(), m.end()
    return None, -1, -1


def guess_gas_from_name(name):
    return _gas_match(name)[0]


def guess_sample_from_name(name):
    """Renvoie la partie du nom de fichier qui n'est pas le gaz (ex. ZTC850)."""
    import re as _re
    base = os.path.splitext(os.path.basename(name))[0]
    g, i0, i1 = _gas_match(name)
    if g:
        # retire le mot reconnu en entier (ex. 'ethylene', 'CO2')
        while i1 < len(base) and base[i1].isalpha():
            i1 += 1
        while i0 > 0 and base[i0 - 1].isalpha():
            i0 -= 1
        if i0 >= 2 and base[i0 - 2:i0].lower() in ("n-", "i-"):
            i0 -= 2                      # prefixe n- / i- des butanes
        base = base[:i0] + " " + base[i1:]
    base = _re.sub(r"[-_ ]+", " ", base).strip()
    return base or os.path.splitext(os.path.basename(name))[0]


def guess_temperature_from_name(name):
    """Temperature (K) ecrite dans un nom de fichier ('ZTC-CO2_303K.xlsx' ->
    303.0), None si absente. Seuls les kelvins sont lus : un '800C' designe
    le plus souvent la temperature de synthese du materiau."""
    import re as _re
    m = _re.search(r"(?<![A-Za-z0-9.])(\d{2,3}(?:[.,]\d+)?)\s*K(?![A-Za-z0-9])",
                   os.path.splitext(os.path.basename(str(name)))[0])
    T = float(m.group(1).replace(",", ".")) if m else 0.0
    return T if 50.0 <= T <= 700.0 else None


def dataset_name_from_file(path, gas):
    """Nom de jeu propose pour un fichier : 'echantillon gaz' si le gaz a ete
    reconnu dans le nom, sinon le nom du fichier."""
    stem = os.path.splitext(os.path.basename(path))[0]
    samp = guess_sample_from_name(path)
    return "%s %s" % (samp, gas) if gas and samp != stem else stem


def unique_name(name, taken):
    """'X', ou 'X (2)', 'X (3)'... si le nom est deja pris : les ajustements
    et les jeux 'total' retrouvent leur jeu d'origine par son nom."""
    out, i = name, 1
    while out in taken:
        i += 1
        out = "%s (%d)" % (name, i)
    return out


def sample_label(name, gas=None):
    """Echantillon deduit d'un nom de jeu : sans le gaz, la temperature ni
    '(total)'. Ex. 'ZTC850 CO2 (total)' -> 'ZTC850', 'DEMO CO2 273K' -> 'DEMO'."""
    import re as _re
    s = " %s " % str(name)
    s = _re.sub(r"(?i)\(total\)", " ", s)
    s = _re.sub(r"(?i)(?<![A-Za-z0-9.])\d+(?:[.,]\d+)?\s*K(?![A-Za-z0-9])", " ", s)
    pats = [p for g, ps in _GAS_PATTERNS if (gas is None or g == gas) for p in ps]
    low = s.lower()
    for pat in pats:
        m = _re.search(pat, low)
        if m:
            i0, i1 = m.start(), m.end()
            while i1 < len(low) and low[i1].isalpha():
                i1 += 1
            while i0 > 0 and low[i0 - 1].isalpha():
                i0 -= 1
            if i0 >= 2 and low[i0 - 2:i0] in ("n-", "i-"):
                i0 -= 2
            s = s[:i0] + " " + s[i1:]
            break
    s = _re.sub(r"[-_\s]+", " ", s).strip()
    return s or str(name).strip()


class SampleVporeDialog(tk.Toplevel):
    """Conversion en lot : un volume poreux par echantillon."""

    def __init__(self, master, groups, defaults, meth, eos):
        super().__init__(master)
        self.title(_("Conversion en lot - volume poreux par echantillon"))
        self.transient(master)
        self.grab_set()
        self.result = None
        frm = ttk.Frame(self, padding=14)
        frm.pack(fill="both", expand=True)
        n = sum(len(v) for v in groups.values())
        ttk.Label(frm, text=_("%d jeu(x) en exces, %d echantillons. Indiquez le "
                            "volume poreux de chaque echantillon :")
                  % (n, len(groups))).grid(row=0, column=0, columnspan=3,
                                            sticky="w", pady=(0, 10))
        for j, h in enumerate((_("Echantillon"), _("Jeux"), "V_pore (cm3/g)")):
            ttk.Label(frm, text=h, style="Muted.TLabel").grid(
                row=1, column=j, sticky="w", padx=(0, 16))
        self.entries = {}
        for i, (key, ds) in enumerate(groups.items()):
            ttk.Label(frm, text=key).grid(row=2 + i, column=0, sticky="w",
                                         padx=(0, 16), pady=2)
            names = ", ".join(d["name"] for d in ds)
            ttk.Label(frm, text=names if len(names) < 70 else names[:67] + "...",
                      style="Muted.TLabel").grid(row=2 + i, column=1, sticky="w",
                                                 padx=(0, 16))
            e = ttk.Entry(frm, width=10)
            v = defaults.get(key, np.nan)
            if np.isfinite(v):
                e.insert(0, fmt(v, 4))
            e.grid(row=2 + i, column=2, sticky="w", pady=2)
            self.entries[key] = e
        r = 2 + len(groups)
        ttk.Label(frm, text=_("Methode : %s    EOS : %s") % (_(meth), _(eos)),
                  style="Muted.TLabel").grid(row=r, column=0, columnspan=3,
                                             sticky="w", pady=(10, 0))
        bar = ttk.Frame(frm)
        bar.grid(row=r + 1, column=0, columnspan=3, sticky="e", pady=(12, 0))
        ttk.Button(bar, text=_("Annuler"), command=self.destroy
                   ).pack(side="right", padx=4)
        ttk.Button(bar, text=_("Convertir"), style="Primary.TButton",
                   command=self._ok).pack(side="right")
        place_window(self)
        self.wait_window(self)

    def _ok(self):
        out = {}
        for key, e in self.entries.items():
            v = to_float_or(e.get(), np.nan)
            if not (np.isfinite(v) and v > 0):
                messagebox.showwarning(_("Conversion en lot"),
                                       _("Volume poreux invalide pour %s.") % key,
                                       parent=self)
                return
            out[key] = v
        self.result = out
        self.destroy()


def read_two_columns(path, sheet=None):
    """Lit le premier bloc de deux colonnes numeriques d'un fichier.
    Renvoie (P, q, nom_feuille, entetes, nombre de colonnes numeriques) ou
    leve une exception."""
    ext = os.path.splitext(path)[1].lower()
    if ext in (".xlsx", ".xls", ".xlsm"):
        xl = pd.ExcelFile(path)
        sheets = [sheet] if sheet else xl.sheet_names
        last = None
        for sh in sheets:
            df = pd.read_excel(xl, sheet_name=sh, header=0)
            num = df.apply(pd.to_numeric, errors="coerce")
            good = [c for c in num.columns if num[c].notna().sum() >= 3]
            if len(good) >= 2:
                sub = num[good[:2]].dropna()
                if len(sub) >= 3:
                    return (sub.iloc[:, 0].to_numpy(float),
                            sub.iloc[:, 1].to_numpy(float), sh,
                            [str(good[0]), str(good[1])], len(good))
            last = sh
        raise ValueError(_("aucune paire de colonnes numeriques (feuille %s)")
                         % last)
    df = pd.read_csv(path, sep=None, engine="python")
    num = df.apply(pd.to_numeric, errors="coerce")
    good = [c for c in num.columns if num[c].notna().sum() >= 3]
    if len(good) < 2:
        raise ValueError(_("aucune paire de colonnes numeriques"))
    sub = num[good[:2]].dropna()
    return (sub.iloc[:, 0].to_numpy(float), sub.iloc[:, 1].to_numpy(float),
            "-", [str(good[0]), str(good[1])], len(good))


class BatchImportDialog(tk.Toplevel):
    """Recapitulatif modifiable avant import en lot."""

    def __init__(self, master, rows, T_default=303.0, taken=()):
        super().__init__(master)
        self.title(_("Import en lot - verifier avant de valider"))
        self.transient(master)
        self.grab_set()
        self.result = None
        self.rows = rows
        self.taken = set(taken)         # noms de jeux deja dans la session
        frm = ttk.Frame(self, padding=12)
        frm.pack(fill="both", expand=True)

        ttk.Label(frm, text=_("%d fichier(s) lu(s). Verifiez le gaz, la "
                            "temperature et les unites, puis validez.")
                  % len(rows)).pack(anchor="w", pady=(0, 8))

        top = ttk.Frame(frm)
        top.pack(fill="x", pady=(0, 8))
        ttk.Label(top, text=_("Appliquer a tous  -  T (K) :")).pack(side="left")
        self.e_T = ttk.Entry(top, width=9)
        self.e_T.insert(0, fmt(T_default, 2))
        self.e_T.pack(side="left", padx=4)
        ttk.Label(top, text=_("Unite P :")).pack(side="left", padx=(10, 2))
        self.cb_up = TCombobox(top, state="readonly", width=10,
                                  values=list(P_UNITS.keys()))
        self.cb_up.set("bar")
        self.cb_up.pack(side="left")
        ttk.Label(top, text=_("Unite q :")).pack(side="left", padx=(10, 2))
        self.cb_uq = TCombobox(top, state="readonly", width=12,
                                  values=Q_UNITS)
        self.cb_uq.set("mmol/g")
        self.cb_uq.pack(side="left")
        ttk.Label(top, text=_("Type :")).pack(side="left", padx=(10, 2))
        self.cb_kind = TCombobox(top, state="readonly", width=8,
                                    values=["Exces", "Total"])
        self.cb_kind.set("Exces")
        self.cb_kind.pack(side="left")
        ttk.Button(top, text=_("Appliquer"), command=self._apply_all
                   ).pack(side="left", padx=8)

        cols = ("Fichier", "Feuille", "Nom du jeu", "Gaz", "T (K)",
                "Points", "P min", "P max", "q max", "Remarque")
        self.tv = ttk.Treeview(frm, columns=cols, show="headings", height=12)
        for c, w in zip(cols, (190, 70, 170, 55, 65, 55, 65, 65, 65, 250)):
            self.tv.heading(c, text=tr_col(c, True))
            self.tv.column(c, width=w, anchor="w")
        self.tv.tag_configure("warn", background="#fff2cc")
        self.tv.pack(fill="both", expand=True)
        self.tv.bind("<Double-1>", self._edit_cell)
        ttk.Label(frm, style="Muted.TLabel",
                  text=_("Double-clic sur 'Nom du jeu', 'Gaz' ou 'T (K)' pour "
                       "corriger une ligne. En jaune : a verifier (colonne "
                       "Remarque).")).pack(anchor="w", pady=(4, 0))
        self._fill()

        bar = ttk.Frame(frm)
        bar.pack(fill="x", pady=(10, 0))
        ttk.Button(bar, text=_("Annuler"), command=self.destroy
                   ).pack(side="right", padx=4)
        ttk.Button(bar, text=_("Importer"), style="Primary.TButton",
                   command=self._ok).pack(side="right")
        ttk.Button(bar, text=_("Retirer la ligne"), style="Ghost.TButton",
                   command=self._drop).pack(side="left")
        place_window(self, 1100, 520)
        self.wait_window(self)

    def _remark(self, i):
        """Ce qui merite un coup d'oeil avant de valider la ligne i."""
        r, out = self.rows[i], []
        if not r.get("t_ok"):
            out.append(_("T par defaut"))
        if r["name"] in self.taken | {x["name"] for x in self.rows[:i]}:
            out.append(_("nom deja pris : (2) sera ajoute"))
        if r.get("ncols", 2) > 2:
            out.append(_("%d colonnes, 2 lues") % r["ncols"])
        return " ; ".join(out)

    def _fill(self):
        self.tv.delete(*self.tv.get_children())
        for i, r in enumerate(self.rows):
            rem = self._remark(i)
            self.tv.insert("", "end", iid=str(i),
                           tags=(("warn",) if rem else ()), values=(
                os.path.basename(r["path"]), r["sheet"], r["name"], r["gas"],
                fmt(r["T"], 2), len(r["P"]), fmt(np.min(r["P"]), 4),
                fmt(np.max(r["P"]), 4), fmt(np.max(r["q"]), 4), rem))

    def _apply_all(self):
        T = to_float_or(self.e_T.get(), 303.0)
        for r in self.rows:
            r["T"] = T
            r["t_ok"] = True
            r["unit_p"] = self.cb_up.get()
            r["unit_q"] = self.cb_uq.get()
            r["kind"] = self.cb_kind.get()
        self._fill()

    def _drop(self):
        sel = self.tv.selection()
        if not sel:
            return
        for i in sorted((int(x) for x in sel), reverse=True):
            self.rows.pop(i)
        self._fill()

    def _edit_cell(self, event):
        item = self.tv.identify_row(event.y)
        col = self.tv.identify_column(event.x)
        if not item or col not in ("#3", "#4", "#5"):
            return
        i = int(item)
        key = {"#3": "name", "#4": "gas", "#5": "T"}[col]
        x, y, w, h = self.tv.bbox(item, col)
        if key == "gas":
            ed = TCombobox(self.tv, values=GAS_LIST, state="readonly")
            ed.set(self.rows[i]["gas"])
        else:
            ed = ttk.Entry(self.tv)
            ed.insert(0, str(self.rows[i][key]) if key == "name"
                      else fmt(self.rows[i]["T"], 2))
        ed.place(x=x, y=y, width=w, height=h)
        ed.focus_set()

        def done(_=None):
            v = ed.get()
            if key == "T":
                self.rows[i]["T"] = to_float_or(v, self.rows[i]["T"])
                self.rows[i]["t_ok"] = True
            else:
                self.rows[i][key] = v
            ed.destroy()
            self._fill()
        ed.bind("<Return>", done)
        ed.bind("<FocusOut>", done)
        ed.bind("<<ComboboxSelected>>", done)

    def _ok(self):
        if not self.rows:
            self.destroy()
            return
        self.result = self.rows
        self.destroy()


class TabData(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master, padding=10)
        self.app = app
        self._dirty = False
        self._loading = False
        self._loaded_index = None
        pan = ttk.PanedWindow(self, orient="horizontal")
        pan.pack(fill="both", expand=True)
        left = ttk.Frame(pan)
        right = ttk.Frame(pan)
        pan.add(left, weight=0)
        pan.add(right, weight=3)

        # ------------------------------------------------ liste des jeux ---
        c = card(left, _("Jeux de donnees"), _("selectionnez pour ouvrir"))
        c.pack(fill="both", expand=True)
        b = c.body
        ff = ttk.Frame(b, style="Card.TFrame")
        ff.pack(fill="x", pady=(0, 6))
        ttk.Label(ff, text=_("Filtrer :"), style="Card.TLabel").pack(side="left")
        self.var_filter = tk.StringVar()
        ent = ttk.Entry(ff, textvariable=self.var_filter, width=18)
        ent.pack(side="left", fill="x", expand=True, padx=4)
        # enregistrer d'abord : refresh_list remet le temoin "modifie" a zero
        self.var_filter.trace_add(
            "write", lambda *a: (self._autosave(), self.refresh_list()))
        tip(ttk.Button(ff, text="x", width=3, style="Ghost.TButton",
                       command=lambda: self.var_filter.set("")),
            _("Effacer le filtre")).pack(side="left")
        tvf = ttk.Frame(b, style="Card.TFrame")
        tvf.pack(fill="both", expand=True)
        self.lst = ttk.Treeview(tvf, show="tree", height=8, selectmode="browse")
        self.lst.column("#0", width=270)
        sc = ttk.Scrollbar(tvf, orient="vertical", command=self.lst.yview)
        self.lst.configure(yscrollcommand=sc.set)
        self.lst.pack(side="left", fill="both", expand=True)
        sc.pack(side="right", fill="y")
        self.lst.bind("<<TreeviewSelect>>", lambda e: self.on_select())

        bb = ttk.Frame(b, style="Card.TFrame")
        # boutons places avant la liste : dans une petite fenetre c'est la
        # liste qui raccourcit, les boutons restent visibles
        bb.pack(fill="x", pady=(12, 0), side="bottom", before=tvf)
        tip(ttk.Button(bb, text=_("Importer des fichiers..."),
                       style="Primary.TButton", command=self.import_many),
            _("Un ou plusieurs fichiers .xlsx, .xls ou .csv. Le gaz, la "
            "temperature et l'echantillon sont lus dans le nom du fichier "
            "(ex. ZTC850-CO2_303K.xlsx) ; un recapitulatif modifiable est "
            "affiche avant l'import.")
            ).grid(row=0, column=0, columnspan=2, sticky="ew", pady=2)
        tip(ttk.Button(bb, text=_("Importer en choisissant les colonnes..."),
                       command=self.import_file),
            _("Pour un fichier a plusieurs feuilles ou plusieurs colonnes : "
            "choisir soi-meme la feuille, les colonnes et les unites")
            ).grid(row=1, column=0, columnspan=2, sticky="ew", pady=2)
        tip(ttk.Button(bb, text=_("Nouveau jeu vide"), command=self.new_dataset),
            _("Creer un jeu vide et saisir ou coller les valeurs a la main")
            ).grid(row=2, column=0, columnspan=2, sticky="ew", pady=2)
        tip(ttk.Button(bb, text=_("Dupliquer"), command=self.duplicate),
            _("Copier le jeu selectionne")).grid(row=3, column=0, sticky="ew",
                                              padx=(0, 3), pady=2)
        tip(ttk.Button(bb, text=_("Supprimer"), style="Danger.TButton",
                       command=self.delete),
            _("Supprimer definitivement le jeu selectionne")).grid(
            row=3, column=1, sticky="ew", padx=(3, 0), pady=2)
        bb.columnconfigure(0, weight=1)
        bb.columnconfigure(1, weight=1)

        # -------------------------------------------------- metadonnees ----
        head = card(right, _("Metadonnees"),
                    _("gaz et temperature servent aux modeles D-R / D-A et a l'IAST"))
        head.pack(fill="x")
        g = head.body
        self.e_name = field(g, _("Nom :"), ttk.Entry, 18, 0, 0,
                            _("Nom affiche dans tous les onglets"))
        self.cb_gas = field(g, _("Gaz :"), TCombobox, 12, 0, 2,
                            _("Determine la masse molaire, Tc, Pc et l'acentricite"),
                            values=GAS_LIST)
        self.cb_gas.set("CO2")
        self.e_T = field(g, "T (K) :", ttk.Entry, 12, 0, 4,
                         _("Temperature de la mesure, en kelvin"))
        self.e_T.insert(0, "298.15")
        self.cb_kind = field(g, _("Type :"), TCombobox, 8, 0, 6,
                             _("Quantite en exces (mesure brute) ou totale "
                             "(absolue)"), values=["Exces", "Total"],
                             state="readonly")
        self.cb_kind.set("Exces")
        self.cb_up = field(g, _("Unite P :"), TCombobox, 12, 1, 0,
                           _("Unite de la colonne pression du tableau"),
                           values=list(P_UNITS.keys()), state="readonly")
        self.cb_up.set("bar")
        self.cb_up.bind("<<ComboboxSelected>>", lambda e: self._update_headers())
        self.cb_uq = field(g, _("Unite q :"), TCombobox, 12, 1, 2,
                           _("Unite de la colonne quantite adsorbee"),
                           values=Q_UNITS, state="readonly")
        self.cb_uq.set("mmol/g")
        self.cb_uq.bind("<<ComboboxSelected>>", lambda e: self._update_headers())
        self.e_note = field(g, _("Commentaire :"), ttk.Entry, 20, 1, 4,
                            _("Note libre : origine de l'echantillon, appareil..."))
        self.e_note.grid(columnspan=3, sticky="we")

        # -------------------------------------------- tableau et apercu ----
        mid = ttk.PanedWindow(right, orient="horizontal")
        mid.pack(fill="both", expand=True, pady=(10, 0))
        cl = ttk.Frame(mid)
        cr = ttk.Frame(mid)
        mid.add(cl, weight=0)       # le tableau garde sa largeur, l'apercu
        mid.add(cr, weight=1)       # absorbe les changements de taille

        ct = card(cl, _("Donnees experimentales"),
                  _("double-clic pour editer  -  Ctrl+V pour coller depuis Excel"))
        ct.pack(fill="both", expand=True)
        self.tbl = EditableTable(ct.body, ["P (bar)", "q (mmol/g)"], height=8,
                                 widths=[150, 150], nrows=12)
        tb = ttk.Frame(ct.body, style="Card.TFrame")
        for txt, cmd, hint in (
                (_("+ Ligne"), lambda: self.tbl.add_row(), _("Ajouter une ligne vide")),
                (_("- Ligne"), self.tbl.delete_selected,
                 _("Supprimer les lignes selectionnees (touche Suppr)")),
                (_("Trier"), lambda: self.tbl.sort_by(0),
                 _("Trier par pression croissante")),
                (_("Coller"), lambda: self.tbl._paste(),
                 _("Coller deux colonnes depuis le presse-papiers")),
                (_("Vider"), self.tbl.clear, _("Effacer tout le tableau"))):
            tip(ttk.Button(tb, text=txt, width=0, command=cmd),
                hint).pack(side="left", padx=2, fill="x", expand=True)
        sv = ttk.Frame(ct.body, style="Card.TFrame")
        # boutons places avant le tableau : dans une petite fenetre c'est le
        # tableau qui raccourcit, les boutons restent visibles
        sv.pack(side="bottom", fill="x", pady=(10, 0))
        tb.pack(side="bottom", fill="x", pady=(8, 0))
        self.tbl.pack(fill="both", expand=True)
        self.lbl_dirty = ttk.Label(sv, style="Card.TLabel", text="")
        self.lbl_dirty.pack(side="left")
        self.btn_save = ttk.Button(sv, text=_("Enregistrer le jeu de donnees"),
                                   style="Success.TButton",
                                   command=self.save_current)
        self.btn_save.pack(side="right")
        tip(self.btn_save,
            _("Valide le tableau et les metadonnees. L'enregistrement est aussi "
            "automatique quand vous changez de jeu, lancez un ajustement ou "
            "quittez l'onglet - vos saisies ne sont plus perdues."))
        for _w in (self.e_name, self.e_T, self.e_note):
            _w.bind("<KeyRelease>", self._touch)
        for _w in (self.cb_gas, self.cb_kind, self.cb_up, self.cb_uq):
            _w.bind("<<ComboboxSelected>>", self._touch, add="+")
        self.tbl.on_change = self._touch

        cp = card(cr, _("Apercu"))
        cp.pack(fill="both", expand=True)
        self.fig = Figure(figsize=(4, 3), dpi=100, facecolor=UI["card"])
        self.ax = self.fig.add_subplot(111)
        self.canvas = make_canvas(cp.body, self.fig)
        set_sash(pan, 0, 330)
        set_sash(mid, 0, 470)
        self.refresh_list()

    def _update_headers(self):
        cols = ["P (%s)" % self.cb_up.get(), "q (%s)" % self.cb_uq.get()]
        for old, new in zip(self.tbl.columns, cols):
            self.tbl.tree.heading(old, text=tr_col(new, True))

    def refresh_list(self, select=None):
        if select is None:
            select = self.current_index()          # conserve la selection
        try:
            flt = self.var_filter.get().strip().lower()
        except Exception:
            flt = ""
        self._loading = True
        self.lst.delete(*self.lst.get_children())
        shown = []
        for i, d in enumerate(self.app.datasets):
            txt = "%s  [%s, %.1f K, %s]" % (d["name"], d["gas"], d["T"],
                                            _(d["kind"]))
            if flt and flt not in txt.lower():
                continue
            self.lst.insert("", "end", iid=str(i), text=txt)
            shown.append(i)
        if select is not None and select in shown:
            self.lst.selection_set(str(select))
            self.lst.see(str(select))
        elif shown:
            self.lst.selection_set(str(shown[0]))
        elif not self.app.datasets:
            self.plot_preview(None)
        self._loading = False
        self._update_dirty(False)

    def current_index(self):
        sel = self.lst.selection()
        return int(sel[0]) if sel else None

    # ---------------------------------------------------------- enregistrement
    def _update_dirty(self, state=True):
        """Indicateur visuel : le jeu affiche differe-t-il du jeu memorise ?"""
        self._dirty = bool(state) and not getattr(self, "_loading", False)
        if not hasattr(self, "lbl_dirty"):
            return
        if self._dirty:
            self.lbl_dirty.config(
                text=_("\u25cf  modifications non enregistrees"),
                foreground="#B26B00")
            self.btn_save.config(text=_("Enregistrer le jeu de donnees  (Ctrl+S)"))
        else:
            self.lbl_dirty.config(text=_("\u2713  a jour"), foreground="#2E7D32")
            self.btn_save.config(text=_("Enregistrer le jeu de donnees"))

    def _touch(self, *_a):
        self._update_dirty(True)

    def _autosave(self):
        """Enregistre silencieusement le jeu courant s'il a ete modifie."""
        if getattr(self, "_dirty", False) and self._loaded_index is not None:
            try:
                self.save_current(silent=True, index=self._loaded_index)
                return True
            except Exception:
                return False
        return False

    def on_select(self):
        """Change de jeu SANS perdre les modifications en cours."""
        if getattr(self, "_loading", False):
            return
        new = self.current_index()
        if new == self._loaded_index:
            return
        if self._autosave() and new is not None:
            # l'enregistrement a reselectionne le jeu enregistre : revenir a
            # celui que l'utilisateur vient de choisir
            self.lst.selection_set(str(new))
        self.load_selected()

    def load_selected(self):
        i = self.current_index()
        if i is None:
            return
        self._loading = True
        self._loaded_index = i
        d = self.app.datasets[i]
        self.e_name.delete(0, "end")
        self.e_name.insert(0, d["name"])
        self.cb_gas.set(d["gas"])
        self.e_T.delete(0, "end")
        self.e_T.insert(0, fmt(d["T"], 2))
        self.cb_kind.set(d["kind"])
        self.cb_up.set(d.get("unit_p", "bar"))
        self.cb_uq.set(d.get("unit_q", "mmol/g"))
        self.e_note.delete(0, "end")
        self.e_note.insert(0, d.get("note", ""))
        self._update_headers()
        self.tbl.set_rows(list(zip(d["P_raw"], d["q_raw"])))
        self.plot_preview(d)
        self._loading = False
        self._update_dirty(False)

    def plot_preview(self, d=None):
        self.ax.clear()
        if d:
            self.ax.plot(d["P"], d["q"], "o-", color=PALETTE[0], ms=5)
            self.ax.set_xlabel(_("P (bar)"))
            self.ax.set_ylabel(_("q (mmol/g)"))
            self.ax.set_title(d["name"], fontsize=9)
            self.ax.grid(True, ls="--", alpha=0.5)
        else:
            self.ax.axis("off")
            self.ax.text(0.5, 0.5, _("Aucun jeu de donnees.\n\nImportez vos "
                         "fichiers d'isothermes\n(bouton bleu a gauche), ou "
                         "collez deux\ncolonnes depuis Excel dans le tableau."),
                         ha="center", va="center", color=UI["muted"])
        self.fig.tight_layout()
        self.canvas.draw_idle()

    def _collect(self):
        arr = self.tbl.get_numeric(2)
        arr = arr[np.isfinite(arr).all(axis=1)]
        if arr.shape[0] == 0:
            raise ValueError(_("Aucune donnee numerique valide dans le tableau."))
        return make_dataset(self.e_name.get().strip() or _("Jeu %d") % (len(self.app.datasets) + 1),
                            self.cb_gas.get().strip() or "CO2",
                            to_float_or(self.e_T.get(), 298.15),
                            self.cb_kind.get(), self.cb_up.get(),
                            self.cb_uq.get(), arr[:, 0], arr[:, 1],
                            self.e_note.get())

    def save_current(self, silent=False, index=None):
        try:
            d = self._collect()
        except Exception as e:
            if not silent:
                messagebox.showerror(_("Donnees"), str(e), parent=self)
            return
        i = index if index is not None else self.current_index()
        new = i is None or not (0 <= i < len(self.app.datasets))
        d["name"] = unique_name(d["name"], {
            x["name"] for j, x in enumerate(self.app.datasets) if new or j != i})
        if new:
            self.app.datasets.append(d)
            i = len(self.app.datasets) - 1
        else:
            self.app.datasets[i] = d
        self._loaded_index = i
        self.e_name.delete(0, "end")        # nom reellement enregistre
        self.e_name.insert(0, d["name"])
        self.refresh_list(select=i)
        self.plot_preview(d)
        self.app.notify_datasets()
        self._update_dirty(False)
        self.app.log(_("Jeu de donnees enregistre : %s (%d points)")
                     % (d["name"], len(d["P"])))

    def new_dataset(self):
        self._autosave()
        self.lst.selection_remove(self.lst.selection())
        # -1 : jeu pas encore dans la liste. Sans cela l'enregistrement
        # automatique ecrivait la nouvelle saisie par-dessus le jeu ouvert avant.
        self._loaded_index = -1
        self.e_name.delete(0, "end")
        self.e_name.insert(0, _("Jeu %d") % (len(self.app.datasets) + 1))
        self.e_note.delete(0, "end")
        self.tbl.clear()
        for _u in range(12):
            self.tbl.add_row()
        self.plot_preview(None)
        self._update_dirty(False)

    def duplicate(self):
        self._autosave()
        i = self.current_index()
        if i is None:
            return
        d = copy.deepcopy(self.app.datasets[i])
        d["name"] = unique_name(d["name"] + _(" (copie)"),
                                {x["name"] for x in self.app.datasets})
        self.app.datasets.append(d)
        self.refresh_list(select=len(self.app.datasets) - 1)
        self.app.notify_datasets()

    def delete(self):
        i = self.current_index()
        if i is None:
            return
        if messagebox.askyesno(_("Supprimer"), _("Supprimer '%s' ?")
                               % self.app.datasets[i]["name"], parent=self):
            self.app.datasets.pop(i)
            # le formulaire montre un jeu qui n'existe plus : ne rien
            # enregistrer a sa place, recharger celui qui sera selectionne
            self._loaded_index = None
            self.refresh_list()
            self.app.notify_datasets()

    def import_many(self):
        self._autosave()
        paths = filedialog.askopenfilenames(
            title=_("Importer plusieurs isothermes"),
            filetypes=[("Excel / CSV", "*.xlsx *.xls *.xlsm *.csv *.txt *.dat"),
                       (_("Tous les fichiers"), "*.*")])
        if not paths:
            return
        rows, errs = [], []
        Tdef = to_float_or(self.e_T.get(), 303.0)
        for path in paths:
            try:
                P, q, sh, hdr, ncols = read_two_columns(path)
            except Exception as e:
                errs.append("%s : %s" % (os.path.basename(path), e))
                continue
            gas = guess_gas_from_name(path)
            T = guess_temperature_from_name(path)
            rows.append(dict(path=path, sheet=sh, gas=gas or "CO2",
                             name=dataset_name_from_file(path, gas),
                             T=T or Tdef, t_ok=bool(T), ncols=ncols,
                             kind="Exces", unit_p="bar",
                             unit_q="mmol/g", P=P, q=q,
                             note=_("importe de %s (feuille %s, colonnes %s)")
                                  % (os.path.basename(path), sh, " / ".join(hdr))))
        if errs:
            messagebox.showwarning(
                _("Import en lot"),
                _("Fichier(s) ignore(s) :\n  - ") + "\n  - ".join(errs[:12]),
                parent=self)
        if not rows:
            return
        taken = {d["name"] for d in self.app.datasets}
        dlg = BatchImportDialog(self, rows, T_default=Tdef, taken=taken)
        if not dlg.result:
            return
        first = len(self.app.datasets)
        for r in dlg.result:
            d = make_dataset(unique_name(r["name"], taken), r["gas"], r["T"],
                             r["kind"], r["unit_p"], r["unit_q"], r["P"],
                             r["q"], r["note"])
            taken.add(d["name"])
            self.app.datasets.append(d)
        self.refresh_list(select=first)
        self.load_selected()
        self.app.notify_datasets()
        self.app.log(_("Import en lot : %d jeu(x) ajoute(s).") % len(dlg.result))
        self.app.set_status(_("%d isotherme(s) importee(s).") % len(dlg.result))

    def import_file(self):
        self._autosave()
        path = filedialog.askopenfilename(
            title=_("Importer des donnees d'isotherme"),
            filetypes=[("Excel / CSV", "*.xlsx *.xls *.xlsm *.csv *.txt *.dat"),
                       (_("Tous les fichiers"), "*.*")])
        if not path:
            return
        dlg = ImportDialog(self, path)
        if not dlg.result:
            return
        r = dlg.result
        d = make_dataset(unique_name(r["name"],
                                     {x["name"] for x in self.app.datasets}),
                         r["gas"], r["T"], r["kind"], r["unit_p"],
                         r["unit_q"], r["P_raw"], r["q_raw"], r["note"])
        self.app.datasets.append(d)
        self.refresh_list(select=len(self.app.datasets) - 1)
        self.load_selected()
        self.app.notify_datasets()
        self.app.log(_("Import : %s (%d points)") % (d["name"], len(d["P"])))


# =============================================================================
# 8. ONGLET 2 : CONVERSION EXCES -> TOTAL
# =============================================================================

# Densites typiques de phase adsorbee (g/cm3) : liquide au point d'ebullition
# normal ou densite de van der Waals, valeurs indicatives de la litterature.
RHO_ADS_TYPICAL = {
    "CO2": 1.023, "CH4": 0.4224, "H2": 0.0708, "N2": 0.8067, "O2": 1.141,
    "Ar": 1.3954, "CO": 0.789, "C2H6": 0.5446, "C2H4": 0.5678,
    "C3H8": 0.5808, "n-C4H10": 0.6011, "Kr": 2.413, "Xe": 2.942,
}


def saturation_pressure(gas, T):
    """Pression de saturation (bar) ou pseudo-saturation si T > Tc.

    T < Tc : correlation de Lee-Kesler.
    T >= Tc: regle de Dubinin  P0 = Pc (T/Tc)^2.
    """
    if gas not in GAS_DB:
        return np.nan, _("gaz inconnu")
    g = GAS_DB[gas]
    Tr = T / g["Tc"]
    if Tr >= 1.0:
        return g["Pc"] * Tr ** 2, _("pseudo-saturation de Dubinin  Pc(T/Tc)^2")
    if Tr < 0.25:
        return np.nan, _("hors domaine de la correlation")
    f0 = (5.92714 - 6.09648 / Tr - 1.28862 * math.log(Tr) + 0.169347 * Tr ** 6)
    f1 = (15.2518 - 15.6875 / Tr - 13.4721 * math.log(Tr) + 0.43577 * Tr ** 6)
    return g["Pc"] * math.exp(f0 + g["w"] * f1), _("correlation de Lee-Kesler")


def saturation_check(gas, T, P):
    """Points mesures au-dessus de la pression de vapeur saturante (T < Tc).

    Renvoie (Psat en bar ou nan, masque des points P > Psat, source de Psat).
    Au-dela de Psat le fluide est liquide : densite du gaz libre, conversion
    exces -> total et isosteres n'y ont plus de sens. Psat vient de CoolProp
    si possible, sinon de Lee-Kesler (marge de 3 % pour son incertitude).
    """
    P = np.asarray(P, float)
    none = (float("nan"), np.zeros(P.shape, bool), "")
    if gas not in GAS_DB or P.size == 0:
        return none
    T = float(T)
    if HAS_COOLPROP and gas in COOLPROP_NAMES:
        try:
            name = COOLPROP_NAMES[gas]
            if T >= PropsSI("Tcrit", name):
                return none
            psat = PropsSI("P", "T", T, "Q", 0, name) / 1e5
            if np.isfinite(psat) and psat > 0:
                return float(psat), P > psat * (1.0 + 1e-6), "CoolProp"
        except Exception:
            pass
    if T >= GAS_DB[gas]["Tc"]:
        return none
    psat = saturation_pressure(gas, T)[0]
    if not (np.isfinite(psat) and psat > 0):
        return none
    return float(psat), P > psat * 1.03, "Lee-Kesler"


def saturation_warning(gas, T, P):
    """Message d'alerte si des points depassent Psat ; chaine vide sinon."""
    psat, above, src = saturation_check(gas, T, P)
    n = int(np.count_nonzero(above))
    if not n:
        return ""
    return (_("%d point(s) au-dessus de la pression de vapeur saturante de %s "
              "a %.2f K (Psat = %.2f bar, %s) : le fluide y est liquide et "
              "ces points ne decrivent plus l'adsorption d'un gaz.")
            % (n, gas, float(T), psat, src))


class TabConversion(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master, padding=10)
        self.app = app
        self.result = None
        self._vp_mem = {}          # volume poreux deja utilise, par echantillon

        # meme disposition que les onglets IAST et Chaleur isosterique :
        # reglages a gauche, graphique et tableau a droite sur toute la hauteur
        pan = ttk.PanedWindow(self, orient="horizontal")
        pan.pack(fill="both", expand=True)
        lcol = ttk.Frame(pan)
        right = ttk.Frame(pan)
        pan.add(lcol, weight=0)
        pan.add(right, weight=1)
        bar = ttk.Frame(lcol, style="Card.TFrame", padding=10)
        bar.pack(side="bottom", fill="x", pady=(8, 0))
        tip(ttk.Button(bar, text=_("Calculer la conversion"),
                       style="Primary.TButton", command=self.compute),
            _("Calcule rho_gaz(T,P) et n_total pour chaque point")).pack(fill="x")
        b2 = ttk.Frame(bar, style="Card.TFrame")
        b2.pack(fill="x", pady=(6, 0))
        tip(ttk.Button(b2, text=_("Creer un jeu 'total'"),
                       style="Success.TButton", command=self.create_dataset),
            _("Ajoute le resultat comme nouveau jeu de donnees, utilisable pour "
            "l'ajustement")).pack(side="left", fill="x", expand=True,
                                  padx=(0, 3))
        tip(ttk.Button(b2, text=_("Exporter en Excel"), command=self.export),
            _("Enregistre le tableau de conversion")).pack(
            side="left", fill="x", expand=True, padx=(3, 0))
        tip(ttk.Button(bar, text=_("Convertir TOUS les jeux en exces"),
                       style="Success.TButton", command=self.convert_all),
            _("Applique la meme methode et les memes parametres a chaque jeu de "
            "type 'Exces' et cree en une fois tous les jeux 'total' "
            "correspondants.")).pack(fill="x", pady=(6, 0))
        lwrap = ScrollFrame(lcol)
        lwrap.pack(fill="both", expand=True)

        c1 = card(lwrap.inner, _("1. Jeu de donnees et methode"))
        c1.pack(fill="x", pady=(0, 8))
        g = c1.body
        ttk.Label(g, text=_("Jeu de donnees :"), style="Card.TLabel").grid(
            row=0, column=0, sticky="w", pady=3)
        self.cb_ds = TCombobox(g, state="readonly", width=20)
        self.cb_ds.grid(row=0, column=1, sticky="we", padx=(6, 0))
        self.cb_ds.bind("<<ComboboxSelected>>", lambda e: self._ds_changed())
        ttk.Label(g, text=_("Methode :"), style="Card.TLabel").grid(
            row=1, column=0, sticky="w", pady=3)
        self.cb_meth = TCombobox(g, state="readonly", width=20,
                                    values=["Volume poreux", "Densite adsorbee",
                                            "Densite fournie"])
        self.cb_meth.set("Volume poreux")
        self.cb_meth.grid(row=1, column=1, sticky="we", padx=(6, 0))
        self.cb_meth.bind("<<ComboboxSelected>>", lambda e: self._meth_changed())
        wrap_to_width(ttk.Label(g, style="Muted.TLabel", justify="left", text=(
            _("Volume poreux      n_tot = n_exc + V_pore x rho_gaz(T,P)\n"
            "Densite adsorbee   n_tot = n_exc / (1 - rho_gaz/rho_ads)\n"
            "Densite fournie    vous saisissez rho_gaz dans la colonne 2 du "
            "tableau (valeurs NIST par exemple)")))).grid(
            row=2, column=0, columnspan=2, sticky="we", pady=(8, 0))
        g.columnconfigure(1, weight=1)

        c2 = card(lwrap.inner, _("2. Parametres"))
        c2.pack(fill="x")
        h = c2.body
        self.cb_eos = field(h, _("Equation d'etat :"), TCombobox, 18, 0, 0,
                            _("Table NIST : densites de reference tabulees "
                            "(CO2, CH4, H2 a 303 K) - le plus exact, repli "
                            "automatique sur Peng-Robinson hors table. "
                            "Peng-Robinson : EOS cubique translatee Peneloux, "
                            "1 a 3 % d'ecart pres du point critique."),
                            values=(["Table NIST", "Peng-Robinson",
                                     "Gaz parfait"]
                                    + (["CoolProp"] if HAS_COOLPROP else [])),
                            state="readonly")
        self.cb_eos.set("Table NIST")
        self.e_vp = field(h, _("V_pore (cm3/g) :"), ttk.Entry, 12, 1, 0,
                          _("Volume poreux total accessible, mesure par DFT, "
                          "D-R ou pycnometrie helium"))
        ttk.Label(h, text=_("rho phase adsorbee :"), style="Card.TLabel").grid(
            row=2, column=0, sticky="w", pady=3)
        rw = ttk.Frame(h, style="Card.TFrame")
        rw.grid(row=2, column=1, sticky="w")
        self.e_rho = ttk.Entry(rw, width=10)
        self.e_rho.pack(side="left")
        self.cb_rho_u = TCombobox(rw, state="readonly", width=9,
                                     values=["g/cm3", "mmol/cm3"])
        self.cb_rho_u.set("g/cm3")
        self.cb_rho_u.pack(side="left", padx=4)
        tip(ttk.Button(rw, text=_("Typique"), style="Ghost.TButton", width=8,
                       command=self._fill_typical),
            _("Densite du liquide au point d'ebullition normal pour ce gaz")
            ).pack(side="left")

        self.lbl_conv = wrap_to_width(ttk.Label(
            right, text="", style="MutedBg.TLabel", justify="left"))
        self.lbl_conv.pack(fill="x", pady=(0, 6))
        mid = ttk.PanedWindow(right, orient="vertical")
        mid.pack(fill="both", expand=True)
        cg = card(mid, _("Comparaison exces / total"))
        ct = card(mid, _("Resultats"))
        mid.add(cg, weight=3)
        mid.add(ct, weight=1)
        self.fig = Figure(figsize=(4.5, 3.2), dpi=100, facecolor=UI["card"])
        self.ax = self.fig.add_subplot(111)
        self.canvas = make_canvas(cg.body, self.fig,
                                  (self._render, _("Conversion"), app))
        cols = ["P (bar)", "rho_gaz (mmol/cm3)", "Z", "n_exces (mmol/g)",
                "n_total (mmol/g)", "Ecart (%)"]
        self.tbl = EditableTable(ct.body, cols, height=4,
                                 widths=[80, 135, 70, 125, 125, 80])
        self.tbl.pack(fill="both", expand=True)
        set_sash(pan, 0, 450)
        set_sash(mid, 0, 0.6)
        self._meth_changed()

    def refresh(self):
        vals = ["%d. %s [%s, %.1f K, %s]" % (i + 1, d["name"], d["gas"],
                                             d["T"], _(d["kind"]))
                for i, d in enumerate(self.app.datasets)]
        cur = self.cb_ds.get()
        self.cb_ds["values"] = vals
        if cur in vals:
            self.cb_ds.set(cur)
        elif vals:
            self.cb_ds.current(0)
            self._ds_changed()
        else:
            self.cb_ds.set("")

    def _ds_changed(self):
        d = self.selected_dataset()
        if d and not self.e_rho.get():
            self._fill_typical()
        if d:
            v = self._vp_mem.get(sample_label(d["name"], d.get("gas")).lower())
            if v:
                self.e_vp.config(state="normal")
                self.e_vp.delete(0, "end")
                self.e_vp.insert(0, fmt(v, 4))
                self._meth_changed()

    def _meth_changed(self):
        m = self.cb_meth.get()
        self.e_vp.config(state="normal" if m in ("Volume poreux",
                                                 "Densite fournie") else "disabled")
        self.e_rho.config(state="normal" if m == "Densite adsorbee" else "disabled")

    def _fill_typical(self):
        d = self.selected_dataset()
        gas = d["gas"] if d else "CO2"
        v = RHO_ADS_TYPICAL.get(gas)
        self.e_rho.config(state="normal")
        self.e_rho.delete(0, "end")
        if v:
            if self.cb_rho_u.get() == "g/cm3":
                self.e_rho.insert(0, "%.4f" % v)
            else:
                self.e_rho.insert(0, "%.4f" % (v * 1000.0 / GAS_DB[gas]["M"]))
        self._meth_changed()

    def selected_dataset(self):
        s = self.cb_ds.get()
        if not s:
            return None
        try:
            i = int(s.split(".")[0]) - 1
            return self.app.datasets[i]
        except Exception:
            return None

    # ------------------------------------------------------------------
    def convert_all(self):
        """Convertit d'un coup tous les jeux 'Exces' avec les parametres courants."""
        src = [d for d in self.app.datasets if d.get("kind") == "Exces"]
        if not src:
            messagebox.showinfo(_("Conversion en lot"),
                                _("Aucun jeu de type 'Exces' a convertir."),
                                parent=self)
            return
        meth = self.cb_meth.get()
        eos = self.cb_eos.get()
        Vp = to_float_or(self.e_vp.get(), 0.0)
        vp_of = None
        if meth == "Volume poreux":
            groups = {}
            for d in src:
                groups.setdefault(sample_label(d["name"], d.get("gas")),
                                  []).append(d)
            if len(groups) > 1:
                # plusieurs echantillons : un volume poreux chacun
                defaults = {k: self._vp_mem.get(k.lower(), Vp if Vp > 0 else np.nan)
                            for k in groups}
                dlg = SampleVporeDialog(self, groups, defaults, meth, eos)
                if not dlg.result:
                    return
                vp_of = {id(d): dlg.result[k] for k, ds in groups.items()
                         for d in ds}
                for k, v in dlg.result.items():
                    self._vp_mem[k.lower()] = v
        if vp_of is None and meth == "Volume poreux" and not (Vp > 0):
            messagebox.showwarning(_("Conversion en lot"),
                                   _("Renseignez un volume poreux > 0."),
                                   parent=self)
            return
        if vp_of is None and not messagebox.askyesno(
                _("Conversion en lot"),
                _("Convertir %d jeu(x) en quantite totale ?\n\n"
                "  methode  : %s\n  EOS      : %s\n  V_pore   : %s cm3/g\n\n"
                "Les jeux 'total' deja presents portant le meme nom seront "
                "remplaces.") % (len(src), _(meth), _(eos), fmt(Vp, 4)),
                parent=self):
            return
        made, fail, sat = 0, [], []
        for d in src:
            psat, above, _src = saturation_check(d["gas"], d["T"], d["P"])
            if above.any():
                sat.append(_("%s (%d point(s) > Psat = %.2f bar)")
                           % (d["name"], int(above.sum()), psat))
            try:
                rho_ads = None
                if meth == "Densite adsorbee":
                    v = to_float_or(self.e_rho.get(), np.nan)
                    if self.cb_rho_u.get() == "g/cm3" and np.isfinite(v):
                        v = v * 1000.0 / GAS_DB[d["gas"]]["M"]
                    rho_ads = v
                Vd = vp_of[id(d)] if vp_of else Vp
                n_tot, rho = excess_to_total(
                    np.asarray(d["P"], float), np.asarray(d["q"], float),
                    d["T"], d["gas"], method=meth, V_pore=Vd,
                    rho_ads=rho_ads, eos=eos)
                if not np.all(np.isfinite(n_tot)):
                    raise ValueError(_("valeurs non finies (hors table ?)"))
                name = d["name"] + " (total)"
                nd_ = make_dataset(name, d["gas"], d["T"], "Total", "bar",
                                   "mmol/g", np.asarray(d["P"], float), n_tot,
                                   _("converti de '%s' : %s, V_pore=%s cm3/g, "
                                   "EOS=%s") % (d["name"], _(meth), fmt(Vd, 4), _(eos)))
                self.app.datasets = [x for x in self.app.datasets
                                     if x["name"] != name]
                self.app.datasets.append(nd_)
                made += 1
            except Exception as e:
                fail.append("%s : %s" % (d["name"], e))
        self.app.notify_datasets()
        self.refresh()
        self.app.log(_("Conversion en lot : %d jeu(x) cree(s), %d echec(s).")
                     % (made, len(fail)))
        msg = _("%d jeu(x) 'total' cree(s).") % made
        if fail:
            msg += _("\n\nEchecs :\n  - ") + "\n  - ".join(fail[:10])
        if sat:
            head = _("Points au-dessus de la pression de vapeur saturante "
                     "(fluide liquide, conversion sans objet) :")
            msg += "\n\n" + head + "\n  - " + "\n  - ".join(sat[:10])
            self.app.log(_("ATTENTION : ") + head + " " + "; ".join(sat))
        messagebox.showinfo(_("Conversion en lot"), msg, parent=self)

    def _vpore(self):
        """Volume poreux saisi. Pas de valeur par defaut : elle fausserait la
        conversion sans prevenir."""
        v = to_float_or(self.e_vp.get(), np.nan)
        if not (np.isfinite(v) and v > 0):
            self.e_vp.focus_set()
            raise ValueError(_("Renseignez le volume poreux de l'echantillon "
                             "(V_pore, en cm3/g)."))
        return v

    def compute(self):
        d = self.selected_dataset()
        if d is None:
            messagebox.showwarning(_("Conversion"), _("Selectionnez un jeu de donnees."),
                                   parent=self)
            return
        P = np.asarray(d["P"], float)
        n_exc = np.asarray(d["q"], float)
        meth = self.cb_meth.get()
        eos = self.cb_eos.get()
        gas, T = d["gas"], d["T"]
        try:
            if meth == "Densite fournie":
                rows = self.tbl.get_numeric(3)
                if rows.shape[0] != len(P):
                    raise ValueError(_("Saisissez une colonne rho_gaz de meme "
                                     "longueur que les donnees (colonne 2 du "
                                     "tableau), puis relancez le calcul."))
                rho_user = rows[:, 1]
                V_pore = self._vpore()
                n_tot, rho = excess_to_total(P, n_exc, T, gas, "Densite fournie",
                                             V_pore=V_pore,
                                             rho_gas_user=rho_user)
            elif meth == "Densite adsorbee":
                rho_ads = to_float_or(self.e_rho.get(), np.nan)
                if self.cb_rho_u.get() == "g/cm3":
                    rho_ads = rho_ads * 1000.0 / GAS_DB.get(gas, {"M": 44.01})["M"]
                n_tot, rho = excess_to_total(P, n_exc, T, gas, meth,
                                             rho_ads=rho_ads, eos=eos)
            else:
                V_pore = self._vpore()
                n_tot, rho = excess_to_total(P, n_exc, T, gas, meth,
                                             V_pore=V_pore, eos=eos)
                self._vp_mem[sample_label(d["name"], gas).lower()] = V_pore
        except Exception as e:
            messagebox.showerror(_("Conversion"), str(e), parent=self)
            return

        Z = [eos_z_effective(T, p, gas, eos) for p in P]
        crit, msg = near_critical(gas, T, float(np.max(P)))
        ref = density_is_reference(gas, T, float(np.max(P)), eos)
        if crit and not ref:
            self.app.log(_("ATTENTION : ") + msg)
        with np.errstate(divide="ignore", invalid="ignore"):
            ecart = 100.0 * (n_tot - n_exc) / np.where(np.abs(n_exc) > 1e-12,
                                                       n_exc, np.nan)
        rows = [[fmt(P[i], 5), fmt(rho[i], 6), fmt(Z[i], 4), fmt(n_exc[i], 5),
                 fmt(n_tot[i], 5), fmt(ecart[i], 2)] for i in range(len(P))]
        self.tbl.set_rows(rows)
        self.result = dict(dataset=d["name"], gas=gas, T=T, method=meth,
                           eos=eos, P=P, n_exc=n_exc, n_tot=n_tot, rho=rho, Z=Z)

        self._render(self.fig)
        self.canvas.draw_idle()
        self.app.log(_("Conversion effectuee (%s, %s) sur '%s'.")
                     % (_(meth), _(eos), d["name"]))
        try:
            dq = float(np.nanmax(n_tot - n_exc))
            crit, msg = near_critical(gas, T, float(np.max(P)))
            ref = density_is_reference(gas, T, float(np.max(P)), eos)
            if ref:
                note = (_("densites de reference %s")
                        % ("NIST" if eos == "Table NIST" else "CoolProp"))
            else:
                note = msg if crit else _("domaine sur")
            warn = crit and not ref
            txt = (_("Ecart maximal exces/total : %s mmol/g  -  %s")
                   % (fmt(dq, 4), note))
            sat = saturation_warning(gas, T, P)
            if sat:
                warn = True
                txt = sat + " " + _("Retirez-les avant la conversion.")
                self.app.log(_("ATTENTION : ") + txt)
            self.lbl_conv.config(text=txt,
                                 foreground=(UI["danger"] if warn else UI["ok"]))
        except Exception:
            pass

    def _render(self, fig):
        fig.clear()
        ax, ax2 = panel_axes(fig, 2, sharex=True)
        self.ax = ax
        r = self.result
        if not r:
            return
        ax.plot(r["P"], r["n_exc"], "o-", color=PALETTE[0], ms=5,
                label=_("Quantite en exces"))
        ax.plot(r["P"], r["n_tot"], "s--", color=PALETTE[1], ms=5,
                label=_("Quantite totale"))
        ax.set_ylabel(_("q (mmol/g)"))
        ax.set_title("%s  -  %s (%s)" % (r["dataset"], _(r["method"]),
                                         _(r["eos"])), fontsize=9)
        ax.legend(fontsize=8)
        ax.grid(True, ls="--", alpha=0.5)
        ax2.plot(r["P"], np.asarray(r["n_tot"]) - np.asarray(r["n_exc"]), "^-",
                 color=PALETTE[2], ms=5, label=_("Correction appliquee"))
        for a in (ax, ax2):
            if a.get_subplotspec().is_last_row():
                a.set_xlabel(_("Pression (bar)"))
        ax2.set_ylabel(_("n_tot - n_exc"))
        ax2.grid(True, ls="--", alpha=0.5)
        ax2.legend(fontsize=8)
        try:
            fig.tight_layout()
        except Exception:
            pass

    def create_dataset(self):
        if not self.result:
            messagebox.showwarning(_("Conversion"), _("Lancez d'abord le calcul."),
                                   parent=self)
            return
        r = self.result
        # meme suffixe que la conversion en lot : l'ajustement en lot et le
        # nom d'echantillon reconnaissent ainsi le jeu converti
        d = make_dataset(unique_name("%s (total)" % r["dataset"],
                                     {x["name"] for x in self.app.datasets}),
                         r["gas"], r["T"], "Total",
                         "bar", "mmol/g", r["P"], r["n_tot"],
                         _("Converti par '%s' (%s)") % (r["method"], r["eos"]))
        self.app.datasets.append(d)
        i = len(self.app.datasets) - 1
        self.app.notify_datasets()
        try:
            self.app.tab_data.refresh_list(select=i)
            self.app.tab_data.load_selected()
        except Exception:
            pass
        self.app.log(_("Nouveau jeu cree : %s (%d points)") % (d["name"],
                                                            len(d["P"])))
        if messagebox.askyesno(_("Conversion"),
                               _("Jeu '%s' ajoute (%d points).\n\n"
                               "Aller a l'onglet Donnees pour le voir ?")
                               % (d["name"], len(d["P"])), parent=self):
            try:
                self.app.nb.select(0)
            except Exception:
                pass

    def export(self):
        if not self.result:
            messagebox.showwarning(_("Conversion"), _("Lancez d'abord le calcul."),
                                   parent=self)
            return
        path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                            filetypes=[("Excel", "*.xlsx")],
                                            initialfile=_("conversion_ntot.xlsx"))
        if not path:
            return
        r = self.result
        df = pd.DataFrame({"P (bar)": r["P"], "Z": r["Z"],
                           "rho_gaz (mmol/cm3)": r["rho"],
                           "n_exces (mmol/g)": r["n_exc"],
                           "n_total (mmol/g)": r["n_tot"]})
        with pd.ExcelWriter(path, engine="openpyxl") as w:
            df.to_excel(w, sheet_name=tr_col("Conversion"), index=False)
            pd.DataFrame([{"Jeu": r["dataset"], "Gaz": r["gas"], "T (K)": r["T"],
                           "Methode": _(r["method"]), "EOS": _(r["eos"])}]
                         ).to_excel(w, sheet_name=tr_col("Parametres"), index=False)
        self.app.log(_("Export : %s") % path)
        messagebox.showinfo(_("Export"), _("Fichier enregistre :\n%s") % path,
                            parent=self)


# =============================================================================
# 9. ONGLET 3 : AJUSTEMENT DES MODELES
# =============================================================================

class TabFit(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master, padding=10)
        self.app = app
        self._auto_ds = True    # jeu choisi par le programme, pas par l'utilisateur
        self.checked = {k: (k in ("langmuir", "sips", "toth"))
                        for k in MODEL_ORDER}
        pan = ttk.PanedWindow(self, orient="horizontal")
        pan.pack(fill="both", expand=True)
        lcol = ttk.Frame(pan)
        right = ttk.Frame(pan)
        pan.add(lcol, weight=0)
        pan.add(right, weight=1)
        # boutons d'action hors de la zone defilante : toujours visibles
        act = ttk.Frame(lcol, style="Card.TFrame", padding=10)
        act.pack(side="bottom", fill="x", pady=(8, 0))
        lwrap = ScrollFrame(lcol)
        lwrap.pack(fill="both", expand=True)
        left = lwrap.inner

        # ---------------------------------------------- jeu et contexte ----
        c1 = card(left, _("1. Jeu de donnees et contexte"))
        c1.pack(fill="x", pady=(0, 8))
        g = c1.body
        self.cb_ds = TCombobox(g, state="readonly", width=42)
        self.cb_ds.grid(row=0, column=0, columnspan=4, sticky="ew", pady=(0, 6))
        self.cb_ds.bind("<<ComboboxSelected>>", lambda e: self.on_dataset())
        self.e_T = field(g, "T (K) :", ttk.Entry, 12, 1, 0,
                         _("Temperature, utilisee par D-R et D-A"))
        self.e_T.insert(0, "298.15")
        self.e_P0 = field(g, _("P0 (bar) :"), ttk.Entry, 12, 1, 2,
                          _("Pression de saturation ou pseudo-saturation, "
                          "requise par D-R et D-A a P0 fixe"))
        tip(ttk.Button(g, text=_("Estimer P0 automatiquement"),
                       style="Ghost.TButton", command=self.estimate_p0),
            _("Lee-Kesler si T < Tc, regle de Dubinin Pc(T/Tc)^2 si T > Tc")).grid(
            row=2, column=0, columnspan=2, sticky="w", pady=(6, 0))
        self.lbl_p0 = ttk.Label(g, text="", style="Muted.TLabel")
        self.lbl_p0.grid(row=2, column=2, columnspan=2, sticky="w", pady=(6, 0))
        self.lbl_kind = wrap_to_width(ttk.Label(
            g, text="", style="Muted.TLabel", foreground=UI["warn"],
            justify="left"))
        self.lbl_kind.grid(row=3, column=0, columnspan=4, sticky="we")

        # ----------------------------------------------------- modeles -----
        c2 = card(left, _("2. Modeles a ajuster"), _("cochez dans la colonne de gauche"))
        c2.pack(fill="x", pady=(0, 8))
        self.tv_models = ttk.Treeview(c2.body, columns=("chk", "mod"),
                                      show="headings", height=9,
                                      selectmode="browse")
        self.tv_models.heading("chk", text="")
        self.tv_models.heading("mod", text=_("Modele"))
        self.tv_models.column("chk", width=36, anchor="center", stretch=False)
        self.tv_models.column("mod", width=310, anchor="w")
        self.tv_models.pack(fill="x")
        for k in MODEL_ORDER:
            self.tv_models.insert("", "end", iid=k,
                                  values=("X" if self.checked[k] else "",
                                          MODELS[k].label))
        self.tv_models.bind("<Button-1>", self._click_models)
        self.tv_models.bind("<<TreeviewSelect>>", lambda e: self.load_params())
        bm = ttk.Frame(c2.body, style="Card.TFrame")
        bm.pack(fill="x", pady=(8, 0))
        ttk.Button(bm, text=_("Tout cocher"), width=13,
                   command=lambda: self._check_all(True)).pack(side="left")
        ttk.Button(bm, text=_("Tout decocher"), width=13,
                   command=lambda: self._check_all(False)).pack(side="left",
                                                                padx=5)

        # ------------------------------------------------------ options ----
        c3 = card(left, _("3. Options d'ajustement"))
        c3.pack(fill="x", pady=(0, 8))
        f4 = c3.body
        ttk.Label(f4, text=_("Ponderation :"), style="Card.TLabel").grid(
            row=0, column=0, sticky="w", pady=3)
        self.cb_w = TCombobox(f4, values=WEIGHT_MODES, state="readonly",
                                 width=26)
        self.cb_w.set(WEIGHT_MODES[0])
        self.cb_w.grid(row=0, column=1, sticky="w", padx=6)
        tip(self.cb_w, _("1/q^2 donne le meme poids relatif a tous les points : "
                       "utile quand les faibles pressions comptent autant que "
                       "la saturation"))
        self.var_extrap = tk.DoubleVar(value=1.1)
        ttk.Label(f4, text=_("Extrapolation courbe (x P_max) :"),
                  style="Card.TLabel").grid(row=1, column=0, sticky="w", pady=3)
        ttk.Entry(f4, textvariable=self.var_extrap, width=10).grid(
            row=1, column=1, sticky="w", padx=6)
        self.var_ms = tk.BooleanVar(value=True)
        ttk.Checkbutton(f4, text=_("Multi-depart, essais :"), variable=self.var_ms
                        ).grid(row=2, column=0, sticky="w", pady=3)
        self.e_ms = ttk.Entry(f4, width=10)
        self.e_ms.insert(0, "12")
        self.e_ms.grid(row=2, column=1, sticky="w", padx=6)
        tip(self.e_ms, _("Relance l'ajustement depuis plusieurs points de depart "
                       "aleatoires et garde le meilleur. Recommande pour Toth, "
                       "Sips et D-A qui ont des minima locaux."))
        self.var_bs = tk.BooleanVar(value=False)
        ttk.Checkbutton(f4, text=_("Bootstrap IC 95 %, tirages :"),
                        variable=self.var_bs).grid(row=3, column=0, sticky="w",
                                                   pady=3)
        self.e_bs = ttk.Entry(f4, width=10)
        self.e_bs.insert(0, "200")
        self.e_bs.grid(row=3, column=1, sticky="w", padx=6)
        tip(self.e_bs, _("Reajuste le modele N fois sur des residus "
                       "reechantillonnes. Plus fiable que l'ecart-type "
                       "asymptotique quand les parametres sont correles. "
                       "Comptez quelques secondes par modele."))

        # -------------------------------------- valeurs initiales / bornes -
        c4 = card(left, _("4. Valeurs initiales et bornes"),
                  _("du modele surligne ci-dessus"))
        c4.pack(fill="x", pady=(0, 8))
        self.tbl_par = EditableTable(c4.body, ["Parametre", "p0", "min", "max"],
                                     height=6, widths=[120, 90, 90, 90])
        self.tbl_par.pack(fill="x")
        ttk.Button(c4.body, text=_("Reinitialiser (automatique)"),
                   style="Ghost.TButton", command=self.load_params).pack(
            anchor="w", pady=(6, 0))

        tip(ttk.Button(act, text=_("Ajuster les modeles coches"),
                       style="Primary.TButton", command=self.run_fit),
            _("Lance l'ajustement non lineaire sur le jeu selectionne (F5)")
            ).pack(fill="x")
        tip(ttk.Button(act, text=_("Ajuster TOUS les jeux x TOUS les modeles "
                                 "coches"), style="Primary.TButton",
                       command=self.run_fit_all),
            _("Boucle sur l'ensemble des jeux de donnees et lance les modeles "
            "coches sur chacun. Une barre de progression indique l'avancement "
            "(Maj+F5).")).pack(fill="x", pady=(6, 0))

        # ------------------------------------------------- panneau droit ---
        rpan = ttk.PanedWindow(right, orient="vertical")
        rpan.pack(fill="both", expand=True)
        rf = card(rpan, _("Resultats des ajustements"),
                  _("double-clic sur une ligne pour le detail complet"))
        cols = ("ds", "mod", "N", "R2", "R2a", "RMSE", "MSSR", "AIC", "rmax",
                "par")
        heads = ("Jeu", "Modele", "N", "R2", "R2 ajuste", "RMSE", "MSSR",
                 "AIC", "|r|max", "Parametres")
        widths = (140, 175, 40, 75, 75, 75, 100, 70, 65, 330)
        b2 = ttk.Frame(rf.body, style="Card.TFrame")
        b2.pack(side="bottom", fill="x", pady=(8, 0))
        tvf = ttk.Frame(rf.body, style="Card.TFrame")
        tvf.pack(fill="both", expand=True)
        self.tv_fits = ttk.Treeview(tvf, columns=cols, show="headings", height=5)
        for c, h, w in zip(cols, heads, widths):
            self.tv_fits.heading(c, text=tr_col(h, True))
            self.tv_fits.column(c, width=w, minwidth=w, anchor="w",
                                stretch=(c == "par"))
        vs = ttk.Scrollbar(tvf, orient="vertical", command=self.tv_fits.yview)
        hs = ttk.Scrollbar(tvf, orient="horizontal", command=self.tv_fits.xview)
        self.tv_fits.configure(yscrollcommand=vs.set, xscrollcommand=hs.set)
        self.tv_fits.grid(row=0, column=0, sticky="nsew")
        vs.grid(row=0, column=1, sticky="ns")
        hs.grid(row=1, column=0, sticky="ew")
        tvf.rowconfigure(0, weight=1)
        tvf.columnconfigure(0, weight=1)
        self.tv_fits.bind("<Double-1>", lambda e: self.show_details())
        for txt, cmd, sty, hint in (
                (_("Details"), self.show_details, "Primary.TButton",
                 _("Parametres, IC, matrice de correlation et statistiques")),
                (_("Comparer") + " ▾", [
                    (_("Classement des modeles (AIC)"), self.show_ranking),
                    (_("Matrice de comparaison des modeles"), self.show_matrix)],
                 "", _("Tableau croise jeu x modele : R2, RMSE et AIC cote a "
                 "cote, avec le meilleur modele signale par jeu.")),
                (_("Exporter") + " ▾", [
                    (_("Exporter les courbes (P, q)..."), self.export_curves),
                    (_("Exporter tout en Excel"), self.export_fits)],
                 "", _("Parametres, courbes et residus de tous les ajustements")),
                (_("Vers Graphiques"), self.send_to_plot, "",
                 _("Envoyer vers l'onglet Graphiques les lignes selectionnees "
                 "ou, sans selection, le jeu affiche et ses courbes")),
                (_("Supprimer"), self.delete_fit, "", _("Retirer l'ajustement "
                 "selectionne")),
                (_("Tout supprimer"), self.clear_fits, "Danger.TButton",
                 _("Effacer tous les ajustements"))):
            kw = {"style": sty} if sty else {}
            b = ttk.Button(b2, text=txt, width=0, **kw)
            b.config(command=cmd if callable(cmd)
                     else lambda b=b, items=cmd: popup_menu(b, items))
            tip(b, hint).pack(side="left", padx=(0, 5))

        cg = card(rpan, _("Isotherme et residus"))
        rpan.add(rf, weight=2)
        rpan.add(cg, weight=3)
        self.fig = Figure(figsize=(4.5, 3.2), dpi=100, facecolor=UI["card"])
        self.ax = self.fig.add_subplot(211)
        self.axr = self.fig.add_subplot(212)
        self.canvas = make_canvas(cg.body, self.fig,
                                  (self._render, _("Ajustement"), app))
        set_sash(pan, 0, 450)
        set_sash(rpan, 0, 0.45)
        self.load_params()

    def refresh(self):
        vals = ["%d. %s [%s, %.1f K, %s]" % (i + 1, d["name"], d["gas"],
                                             d["T"], _(d["kind"]))
                for i, d in enumerate(self.app.datasets)]
        cur = self.cb_ds.get()
        self.cb_ds["values"] = vals
        if cur in vals and not self._auto_ds:
            self.cb_ds.set(cur)
        elif vals:
            # tant que l'utilisateur n'a pas choisi lui-meme : un jeu 'Total'
            # des qu'il y en a un, c'est lui que l'IAST attend
            tot = [i for i, d in enumerate(self.app.datasets)
                   if d.get("kind") == "Total"]
            new = vals[tot[0] if tot else 0]
            self.cb_ds.set(new)
            if new != cur:
                self.on_dataset(auto=True)
        self.refresh_fits()

    def selected_dataset(self):
        s = self.cb_ds.get()
        if not s:
            return None
        try:
            return self.app.datasets[int(s.split(".")[0]) - 1]
        except Exception:
            return None

    def on_dataset(self, auto=False):
        self._auto_ds = auto
        d = self.selected_dataset()
        if not d:
            return
        self.lbl_kind.config(text=_(
            "Jeu en exces : a haute pression, ajustez plutot le jeu 'total' "
            "(onglet Conversion) pour l'IAST et la chaleur isosterique.")
            if d.get("kind") == "Exces" else "")
        self.e_T.delete(0, "end")
        self.e_T.insert(0, fmt(d["T"], 2))
        self.estimate_p0()
        self.load_params()
        self.draw()

    def estimate_p0(self):
        d = self.selected_dataset()
        if not d:
            return
        T = to_float_or(self.e_T.get(), d["T"])
        p0, meth = saturation_pressure(d["gas"], T)
        if not np.isfinite(p0):
            p0 = float(np.max(d["P"])) * 1.5
            meth = _("1.5 x P_max (par defaut)")
        self.e_P0.delete(0, "end")
        self.e_P0.insert(0, fmt(p0, 4))
        self.lbl_p0.config(text=meth)

    def ctx(self):
        d = self.selected_dataset()
        T = to_float_or(self.e_T.get(), d["T"] if d else 298.15)
        P0 = to_float_or(self.e_P0.get(), np.nan)
        if not np.isfinite(P0) or P0 <= 0:
            P0 = saturation_pressure(d["gas"], T)[0] if d else np.nan
            if not np.isfinite(P0) or P0 <= 0:
                P0 = (float(np.max(d["P"])) * 1.5) if d else 1.0
        return {"T": T, "P0": P0}

    def _click_models(self, event):
        if self.tv_models.identify_region(event.x, event.y) != "cell":
            return
        if self.tv_models.identify_column(event.x) != "#1":
            return
        iid = self.tv_models.identify_row(event.y)
        if not iid:
            return
        self.checked[iid] = not self.checked[iid]
        self.tv_models.set(iid, "chk", "X" if self.checked[iid] else "")
        return "break"

    def _check_all(self, state):
        for k in MODEL_ORDER:
            self.checked[k] = state
            self.tv_models.set(k, "chk", "X" if state else "")

    def load_params(self):
        sel = self.tv_models.selection()
        key = sel[0] if sel else MODEL_ORDER[0]
        m = MODELS[key]
        d = self.selected_dataset()
        rows = []
        if d:
            P = np.asarray(d["P"], float)
            q = np.asarray(d["q"], float)
            msk = P > 0
            try:
                g = m.guess(P[msk], q[msk], self.ctx())
                lb, ub = m.bounds(P[msk], q[msk], self.ctx())
            except Exception:
                g = [1.0] * m.nparam
                lb, ub = [0.0] * m.nparam, [np.inf] * m.nparam
        else:
            g = [1.0] * m.nparam
            lb, ub = [0.0] * m.nparam, [np.inf] * m.nparam
        for i, pn in enumerate(m.pnames):
            rows.append(["%s (%s)" % (pn, m.punits[i]), fmt(g[i], 6),
                         fmt(lb[i], 6), fmt(ub[i], 6) if np.isfinite(ub[i]) else "inf"])
        self.tbl_par.set_rows(rows)
        self._param_model = key

    def _read_params(self, m):
        if getattr(self, "_param_model", None) != m.key:
            return None, None, None
        rows = self.tbl_par.get_rows()
        if len(rows) != m.nparam:
            return None, None, None
        p0, lo, hi = [], [], []
        for r in rows:
            p0.append(to_float(r[1]))
            v = to_float(r[2])
            lo.append(None if np.isnan(v) else v)
            t = str(r[3]).strip().lower()
            hi.append(np.inf if t in ("inf", "+inf", "") else to_float(r[3]))
        if any(np.isnan(v) for v in p0):
            p0 = None
        return p0, lo, hi

    # ------------------------------------------------------------------
    def run_fit_all(self):
        """Ajuste tous les jeux avec les modeles coches."""
        keys = [k for k in MODEL_ORDER if self.checked[k]]
        if not keys:
            messagebox.showwarning(_("Ajustement"), _("Cochez au moins un modele."),
                                   parent=self)
            return
        # un jeu en exces deja converti n'est pas ajuste une seconde fois : son
        # jeu 'total' le remplace pour l'IAST et la chaleur isosterique
        names = {d["name"] for d in self.app.datasets}
        ds = [d for d in self.app.datasets
              if not (d.get("kind") == "Exces"
                      and d["name"] + " (total)" in names)]
        if not ds:
            messagebox.showwarning(_("Ajustement"), _("Aucun jeu de donnees."),
                                   parent=self)
            return
        skip = len(self.app.datasets) - len(ds)
        if not messagebox.askyesno(
                _("Ajustement en lot"),
                _("Lancer %d ajustement(s) (%d jeux x %d modeles) ?\n\n"
                "Les ajustements existants portant le meme couple "
                "jeu / modele seront remplaces.")
                % (len(ds) * len(keys), len(ds), len(keys))
                + (_("\n\n%d jeu(x) en exces deja converti(s) en 'total' : "
                     "non ajuste(s).") % skip if skip else ""), parent=self):
            return
        n_starts = (int(to_float_or(self.e_ms.get(), 12))
                    if self.var_ms.get() else 1)
        total = len(ds) * len(keys)
        done, nok, nfail, fails, sat = 0, 0, 0, [], []
        self.app.busy(True, 0)
        for d in ds:
            psat, above, _src = saturation_check(d["gas"], d["T"], d["P"])
            if above.any():
                sat.append(_("%s (%d point(s) > Psat = %.2f bar)")
                           % (d["name"], int(above.sum()), psat))
            P0b = saturation_pressure(d["gas"], float(d["T"]))[0]
            if not np.isfinite(P0b) or P0b <= 0:
                P0b = float(np.max(d["P"])) * 1.5
            ctx = {"T": float(d["T"]), "P0": P0b}
            P = np.asarray(d["P"], float)
            q = np.asarray(d["q"], float)
            for k in keys:
                m = MODELS[k]
                done += 1
                self.app.set_status(_("Ajustement %d / %d  -  %s / %s")
                                    % (done, total, d["name"], m.label))
                self.app.busy(True, 100.0 * done / total)
                try:
                    self.update_idletasks()
                except Exception:
                    pass
                try:
                    res = fit_isotherm(m, P, q, ctx, weights=self.cb_w.get(),
                                       n_starts=n_starts, n_boot=0)
                except Exception as e:
                    nfail += 1
                    fails.append("%s / %s : %s" % (d["name"], m.label, e))
                    continue
                res["dataset"] = d["name"]
                res["gas"] = d["gas"]
                res["label"] = "%s - %s" % (d["name"], m.label)
                self.app.fits = [f for f in self.app.fits
                                 if not (f["dataset"] == d["name"]
                                         and f["model_key"] == k)]
                self.app.fits.append(res)
                nok += 1
        self.app.busy(False)
        self.refresh_fits()
        self.draw()
        self.app.notify_fits()
        self.app.log(_("Ajustement en lot : %d reussi(s), %d echec(s).")
                     % (nok, nfail))
        msg = _("%d ajustement(s) reussi(s), %d echec(s).") % (nok, nfail)
        if fails:
            msg += _("\n\nEchecs :\n  - ") + "\n  - ".join(fails[:12])
        if sat:
            head = _("Points au-dessus de la pression de vapeur saturante "
                     "(fluide liquide) :")
            msg += "\n\n" + head + "\n  - " + "\n  - ".join(sat[:12])
            self.app.log(_("ATTENTION : ") + head + " " + "; ".join(sat))
        messagebox.showinfo(_("Ajustement en lot"), msg, parent=self)
        self.app.set_status(_("Ajustement en lot termine."))

    def show_matrix(self):
        """Tableau croise jeu x modele."""
        if not self.app.fits:
            messagebox.showinfo(_("Matrice"), _("Aucun ajustement disponible."),
                                parent=self)
            return
        dss, mods = [], []
        for f in self.app.fits:
            if f["dataset"] not in dss:
                dss.append(f["dataset"])
            if f["model_key"] not in mods:
                mods.append(f["model_key"])
        mods = [k for k in MODEL_ORDER if k in mods]
        lines = []
        lines.append(_("MATRICE DE COMPARAISON DES MODELES"))
        lines.append("=" * 108)
        lines.append(_("Un bloc par indicateur : R2, RMSE (mmol/g) puis AICc."))
        lines.append(_("Le modele retenu par jeu (AICc minimal) est marque <<."))
        lines.append("")
        for metric, lab in (("R2", "R2"), ("RMSE", "RMSE (mmol/g)"),
                            ("AICc", "AICc")):
            lines.append("-" * 108)
            lines.append("%-26s" % lab + "".join("%-20s" % MODELS[k].label[:19]
                                                 for k in mods))
            lines.append("-" * 108)
            for dname in dss:
                row = "%-26s" % dname[:25]
                best, bestv = None, np.inf
                for k in mods:
                    f = next((x for x in self.app.fits
                              if x["dataset"] == dname and x["model_key"] == k),
                             None)
                    if f and np.isfinite(f["stats"].get("AICc", np.nan)):
                        if f["stats"]["AICc"] < bestv:
                            bestv, best = f["stats"]["AICc"], k
                for k in mods:
                    f = next((x for x in self.app.fits
                              if x["dataset"] == dname and x["model_key"] == k),
                             None)
                    if f is None:
                        row += "%-20s" % "-"
                    else:
                        v = f["stats"].get(metric, np.nan)
                        txt = fmt(v, 5)
                        if metric == "AICc" and k == best:
                            txt += " <<"
                        row += "%-20s" % txt
                lines.append(row)
            lines.append("")
        show_text_window(self, _("Matrice de comparaison des modeles"),
                         "\n".join(lines))

    def run_fit(self):
        d = self.selected_dataset()
        if d is None:
            messagebox.showwarning(_("Ajustement"), _("Selectionnez un jeu de donnees."),
                                   parent=self)
            return
        keys = [k for k in MODEL_ORDER if self.checked[k]]
        if not keys:
            messagebox.showwarning(_("Ajustement"), _("Cochez au moins un modele."),
                                   parent=self)
            return
        ctx = self.ctx()
        P = np.asarray(d["P"], float)
        q = np.asarray(d["q"], float)
        n_starts = (int(to_float_or(self.e_ms.get(), 12))
                    if self.var_ms.get() else 1)
        n_boot = (int(to_float_or(self.e_bs.get(), 200))
                  if self.var_bs.get() else 0)
        nok, nfail = 0, 0
        for k in keys:
            m = MODELS[k]
            p0, lo, hi = self._read_params(m)

            def prog(i, tot, lab=m.label):
                self.app.log(_("  bootstrap %s : %d / %d") % (lab, i, tot))
                try:
                    self.update_idletasks()
                except Exception:
                    pass
            try:
                if n_boot:
                    self.app.log(_("Ajustement %s (%d departs, %d tirages "
                                 "bootstrap)...") % (m.label, n_starts, n_boot))
                    try:
                        self.update_idletasks()
                    except Exception:
                        pass
                res = fit_isotherm(m, P, q, ctx, p0=p0, lower=lo, upper=hi,
                                   weights=self.cb_w.get(), n_starts=n_starts,
                                   n_boot=n_boot,
                                   progress=prog if n_boot else None)
            except Exception as e:
                nfail += 1
                self.app.log(_("[ECHEC] %s / %s : %s") % (d["name"], m.label, e))
                continue
            res["dataset"] = d["name"]
            res["gas"] = d["gas"]
            res["label"] = "%s - %s" % (d["name"], m.label)
            self.app.fits = [f for f in self.app.fits
                             if not (f["dataset"] == d["name"]
                                     and f["model_key"] == k)]
            self.app.fits.append(res)
            nok += 1
        self.refresh_fits()
        self.draw()
        self.app.notify_fits()
        self.app.log(_("Ajustement : %d reussi(s), %d echec(s) sur '%s'.")
                     % (nok, nfail, d["name"]))
        sat = saturation_warning(d["gas"], d["T"], d["P"])
        if sat:
            self.app.log(_("ATTENTION : ") + "%s : %s" % (d["name"], sat))

    def refresh_fits(self):
        self.tv_fits.delete(*self.tv_fits.get_children())
        self.tv_fits.tag_configure("corr_forte", background="#ffd6d6")
        self.tv_fits.tag_configure("corr_moyenne", background="#fff2cc")
        for i, f in enumerate(self.app.fits):
            m = MODELS[f["model_key"]]
            ps = ", ".join("%s=%s" % (m.pnames[j], fmt(f["params"][j], 4))
                           for j in range(m.nparam))
            s = f["stats"]
            rm = f.get("r_max", np.nan)
            tag = ("corr_forte" if (np.isfinite(rm) and rm > 0.99)
                   else ("corr_moyenne" if (np.isfinite(rm) and rm > 0.95)
                         else ""))
            self.tv_fits.insert("", "end", iid=str(i),
                                tags=((tag,) if tag else ()),
                                values=(f["dataset"], m.label, s["N"],
                                        fmt(s["R2"], 5), fmt(s["R2adj"], 5),
                                        fmt(s["RMSE"], 5), fmt(s["MSSR"], 6),
                                        fmt(s["AIC"], 2), fmt(rm, 4), ps))

    def _sel_fit(self):
        sel = self.tv_fits.selection()
        return int(sel[0]) if sel else None

    def delete_fit(self):
        i = self._sel_fit()
        if i is None:
            return
        self.app.fits.pop(i)
        self.refresh_fits()
        self.draw()
        self.app.notify_fits()

    def clear_fits(self):
        if messagebox.askyesno(_("Ajustements"), _("Supprimer tous les ajustements ?"),
                               parent=self):
            self.app.fits = []
            self.refresh_fits()
            self.draw()
            self.app.notify_fits()

    def show_details(self):
        i = self._sel_fit()
        if i is None:
            return
        f = self.app.fits[i]
        m = MODELS[f["model_key"]]
        s = f["stats"]
        lines = [_("Jeu de donnees : %s") % f["dataset"],
                 _("Modele         : %s") % m.label,
                 _("Equation       : %s") % m.formula,
                 _("Contexte       : T = %s K, P0 = %s bar")
                 % (fmt(f["ctx"].get("T"), 2), fmt(f["ctx"].get("P0"), 4)),
                 _("Ponderation    : %s") % _(f.get("weights", "-")), "",
                 "%-16s %14s %14s %10s" % (_("Parametre"), _("Valeur"), _("Ecart-type"),
                                           _("Unite"))]
        for j, pn in enumerate(m.pnames):
            lines.append("%-16s %14s %14s %10s"
                         % (pn, fmt(f["params"][j], 6), fmt(f["errors"][j], 6),
                            m.punits[j]))
        if f.get("n_starts", 1) > 1:
            lines.append("")
            lines.append(_("Multi-depart : %d essais, %d convergents.")
                         % (f.get("n_starts", 1), f.get("starts_ok", 1)))
        if f.get("ci_lo"):
            lines += ["", _("Intervalles de confiance a 95 %% par bootstrap "
                          "(%d tirages retenus) :") % f.get("n_boot", 0),
                      "%-16s %14s %14s %14s %14s"
                      % (_("Parametre"), _("Valeur"), "IC 2.5 %", "IC 97.5 %",
                         _("ecart-type"))]
            for j, pn in enumerate(m.pnames):
                eb = (f["err_boot"][j] if f.get("err_boot") else np.nan)
                lines.append("%-16s %14s %14s %14s %14s"
                             % (pn, fmt(f["params"][j], 6),
                                fmt(f["ci_lo"][j], 6), fmt(f["ci_hi"][j], 6),
                                fmt(eb, 6)))
            try:
                worst = max(range(m.nparam),
                            key=lambda j: (f["ci_hi"][j] - f["ci_lo"][j])
                            / max(abs(f["params"][j]), 1e-12))
                lg = ((f["ci_hi"][worst] - f["ci_lo"][worst])
                      / max(abs(f["params"][worst]), 1e-12) * 100.0)
                if lg > 50:
                    lines.append(_("  -> parametre le moins bien determine : %s "
                                 "(largeur de l'IC = %.0f %% de la valeur).")
                                 % (m.pnames[worst], lg))
            except Exception:
                pass
        corr = f.get("corr")
        if corr and m.nparam > 1:
            lines += ["", _("Matrice de correlation des parametres :"),
                      "%-14s%s" % ("", "".join("%12s" % pn
                                               for pn in m.pnames))]
            for i2, pn in enumerate(m.pnames):
                lines.append("%-14s%s" % (pn, "".join("%12s" % fmt(corr[i2][j2], 4)
                                                      for j2 in range(m.nparam))))
            rm = f.get("r_max", np.nan)
            if np.isfinite(rm):
                if rm > 0.99:
                    lines.append(_("  -> |r|max = %.4f : parametres quasi "
                                 "indissociables. q_max et b compensent "
                                 "mutuellement ; les valeurs individuelles ne "
                                 "sont pas identifiables de facon fiable, meme "
                                 "avec un R2 excellent.") % rm)
                elif rm > 0.95:
                    lines.append(_("  -> |r|max = %.4f : forte correlation, "
                                 "interpretez les parametres avec prudence.")
                                 % rm)
                else:
                    lines.append(_("  -> |r|max = %.4f : correlation acceptable.")
                                 % rm)
        der = m.derived(f["params"], f["ctx"])
        if der:
            lines.append("")
            lines.append(_("Grandeurs derivees :"))
            for k, (v, u) in der.items():
                lines.append("  %-28s %14s %s" % (_(k), fmt(v, 5), u))
        lines += ["", _("Statistiques :"),
                  "  N      = %d" % s["N"],
                  "  R2     = %s" % fmt(s["R2"], 6),
                  "  R2 adj = %s" % fmt(s["R2adj"], 6),
                  "  SSR    = %s" % fmt(s["SSR"], 6),
                  "  MSSR   = %s" % fmt(s["MSSR"], 8),
                  "  RMSE   = %s" % fmt(s["RMSE"], 6),
                  _("  ARE    = %s %%") % fmt(s["ARE"], 3),
                  "  chi2   = %s" % fmt(s["chi2"], 6),
                  "  AIC    = %s   AICc = %s   BIC = %s"
                  % (fmt(s["AIC"], 3), fmt(s["AICc"], 3), fmt(s["BIC"], 3))]
        if m.note:
            lines += ["", _("Remarque : %s") % m.note]
        show_text_window(self, _("Details de l'ajustement"), "\n".join(lines))

    def show_ranking(self):
        d = self.selected_dataset()
        if d is None:
            return
        fs = [f for f in self.app.fits if f["dataset"] == d["name"]]
        if not fs:
            messagebox.showinfo(_("Classement"), _("Aucun ajustement pour ce jeu."),
                                parent=self)
            return
        fs.sort(key=lambda f: f["stats"]["AIC"])
        best = fs[0]["stats"]["AIC"]
        lines = [_("Classement des modeles pour '%s'") % d["name"], "",
                 "%-32s %9s %9s %10s %8s %10s"
                 % (_("Modele"), "R2", "R2 adj", "RMSE", "k", "dAIC")]
        for f in fs:
            m = MODELS[f["model_key"]]
            s = f["stats"]
            lines.append("%-32s %9s %9s %10s %8d %10s"
                         % (m.label, fmt(s["R2"], 5), fmt(s["R2adj"], 5),
                            fmt(s["RMSE"], 5), m.nparam,
                            fmt(s["AIC"] - best, 2)))
        lines += ["", _("dAIC = 0 : meilleur compromis qualite / nombre de "
                      "parametres."), _("dAIC < 2 : modeles equivalents."),
                  _("dAIC > 10 : modele nettement moins bon.")]
        show_text_window(self, _("Classement des modeles"), "\n".join(lines))

    def _extrap(self):
        try:
            v = float(self.var_extrap.get())
        except Exception:
            v = 1.1
        return v if 0.1 <= v <= 100 else 1.1

    # ------------------------------------------------------------------
    def draw(self):
        self._render(self.fig)
        self.canvas.draw_idle()

    def _render(self, fig):
        """Trace donnees, courbes ajustees et residus sur la figure fournie."""
        fig.clear()
        ax, axr = panel_axes(fig, 2, ratios=(2, 1), sharex=True)
        self.ax, self.axr = ax, axr
        d = self.selected_dataset()
        if d is None:
            return
        P = np.asarray(d["P"], float)
        q = np.asarray(d["q"], float)
        ax.plot(P, q, "o", color="k", ms=6, zorder=5,
                label=_("Donnees : %s") % d["name"])
        fs = [f for f in self.app.fits if f["dataset"] == d["name"]]
        xmax = float(np.max(P)) * self._extrap()
        Pfit = np.linspace(max(1e-6, float(np.min(P)) * 0.01), xmax, 400)
        for i, f in enumerate(fs):
            m = MODELS[f["model_key"]]
            try:
                y = m.func(Pfit, f["ctx"], *f["params"])
            except Exception:
                continue
            c = PALETTE[i % len(PALETTE)]
            ax.plot(Pfit, y, "-", color=c, lw=1.8,
                    label="%s (R2=%s)" % (m.label, fmt(f["stats"]["R2"], 4)))
            axr.plot(f["P"], f["residuals"], "o", color=c, ms=4)
        axr.axhline(0, color="k", lw=0.8)
        ax.set_ylabel(_("q (mmol/g)"))
        ax.grid(True, ls="--", alpha=0.5)
        ax.legend(fontsize=8)
        for a in (ax, axr):
            if a.get_subplotspec().is_last_row():
                a.set_xlabel(_("Pression (bar)"))
        axr.set_ylabel(_("Residus"))
        axr.grid(True, ls="--", alpha=0.5)
        try:
            fig.tight_layout()
        except Exception:
            pass

    def send_to_plot(self):
        """Envoie les lignes selectionnees du tableau ou, sans selection, le
        jeu affiche et toutes ses courbes."""
        fs = [self.app.fits[int(i)] for i in self.tv_fits.selection()]
        d = self.selected_dataset()
        if fs:
            names = list(dict.fromkeys(f["dataset"] for f in fs))
        elif d is not None:
            names = [d["name"]]
            fs = [f for f in self.app.fits if f["dataset"] == d["name"]]
        else:
            return
        n0 = len(self.app.series)
        for d in self.app.datasets:
            if d["name"] in names:
                self.app.add_series(d["name"], np.asarray(d["P"]),
                                    np.asarray(d["q"]), kind="points")
        for f in fs:
            m = MODELS[f["model_key"]]
            xmax = float(np.max(f["P"])) * self._extrap()
            x = np.linspace(max(1e-6, float(np.min(f["P"])) * 0.01), xmax, 400)
            y = m.func(x, f["ctx"], *f["params"])
            self.app.add_series("%s - %s" % (f["dataset"], m.label), x, y,
                                kind="ligne")
        self.app.tab_plot.refresh_series()
        self.app.log(_("%d serie(s) envoyee(s) vers l'onglet Graphiques.")
                     % (len(self.app.series) - n0))

    def export_fits(self):
        if not self.app.fits:
            messagebox.showwarning(_("Export"), _("Aucun ajustement a exporter."),
                                   parent=self)
            return
        path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                            filetypes=[("Excel", "*.xlsx")],
                                            initialfile=_("ajustements.xlsx"))
        if not path:
            return
        try:
            export_fits_excel(self.app, path)
        except Exception as e:
            messagebox.showerror(_("Export"), "%s\n\n%s"
                                 % (e, traceback.format_exc()), parent=self)
            return
        self.app.log(_("Export des ajustements : %s") % path)
        messagebox.showinfo(_("Export"),
                            _("Fichier enregistre :\n%s\n\nFeuilles : "
                            "Parametres / Courbes ajustees / Residus") % path,
                            parent=self)

    def export_curves(self):
        """Export des donnees d'ajustement : P et q calculee (+ points exp.)."""
        if not self.app.fits:
            messagebox.showwarning(_("Export"), _("Aucun ajustement a exporter."),
                                   parent=self)
            return
        d = self.selected_dataset()
        i = self._sel_fit()
        sel = [self.app.fits[i]] if i is not None else []
        of_ds = [f for f in self.app.fits
                 if d is not None and f["dataset"] == d["name"]]
        ref = sel or of_ds or self.app.fits
        P = np.asarray(ref[0]["P"], dtype=float)
        dlg = CurveExportDialog(self, len(sel), len(of_ds), len(self.app.fits),
                                max(1e-9, float(P.min()) * 0.01),
                                float(P.max()) * self._extrap())
        if not dlg.result:
            return
        o = dlg.result
        fits = [sel, of_ds, self.app.fits][o["scope"]]
        if not fits:
            messagebox.showwarning(_("Export"), _("Aucun ajustement dans cette "
                                             "selection."), parent=self)
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".xlsx", initialfile=_("courbes_ajustement.xlsx"),
            filetypes=[("Excel", "*.xlsx"), ("CSV", "*.csv")])
        if not path:
            return
        try:
            df_c, df_e = build_curve_frames(fits, o["pmin"], o["pmax"],
                                            o["npts"], o["exp"])
            if path.lower().endswith(".csv"):
                base = os.path.splitext(path)[0]
                df_c.to_csv(base + "_courbes.csv", index=False)
                written = [base + _("_courbes.csv")]
                if o["exp"] and not df_e.empty:
                    df_e.to_csv(base + "_points.csv", index=False)
                    written.append(base + "_points.csv")
                msg = "\n".join(written)
            else:
                sub = fits_summary_frame(self.app)
                keys = {(f["dataset"], MODELS[f["model_key"]].label)
                        for f in fits}
                if not sub.empty:
                    sub = sub[[(r["Jeu de donnees"], r["Modele"]) in keys
                               for _u, r in sub.iterrows()]]
                with pd.ExcelWriter(path, engine="openpyxl") as w:
                    df_c.to_excel(w, sheet_name=tr_col("Courbes ajustees"), index=False)
                    if o["exp"] and not df_e.empty:
                        df_e.to_excel(w, sheet_name=tr_col("Points et residus"),
                                      index=False)
                    if o["par"] and not sub.empty:
                        sub.to_excel(w, sheet_name=tr_col("Parametres"), index=False)
                msg = path
        except Exception as e:
            messagebox.showerror(_("Export"), "%s\n\n%s"
                                 % (e, traceback.format_exc()), parent=self)
            return
        self.app.log(_("Export des courbes ajustees (%d ajustement(s)) : %s")
                     % (len(fits), path))
        messagebox.showinfo(_("Export"), _("Donnees enregistrees :\n%s") % msg,
                            parent=self)


def build_curve_frames(fits, pmin=np.nan, pmax=np.nan, npts=300,
                       include_exp=True):
    """Construit (courbes lissees, points experimentaux) pour une liste de fits."""
    curves, exp = {}, {}
    for f in fits:
        m = MODELS[f["model_key"]]
        P = np.asarray(f["P"], dtype=float)
        a = pmin if np.isfinite(pmin) else max(1e-9, float(P.min()) * 0.01)
        b = pmax if np.isfinite(pmax) else float(P.max()) * 1.1
        if b <= a:
            b = a * 1.1 + 1e-9
        x = np.linspace(a, b, int(max(2, npts)))
        y = np.asarray(m.func(x, f["ctx"], *f["params"]), dtype=float).ravel()
        key = "%s - %s" % (f["dataset"], m.label)
        curves["%s | P (bar)" % key] = x
        curves["%s | q calcule (mmol/g)" % key] = y
        if include_exp:
            exp["%s | P (bar)" % key] = list(f["P"])
            exp["%s | q experimental (mmol/g)" % key] = list(f["q"])
            exp["%s | q calcule (mmol/g)" % key] = list(f["qpred"])
            exp["%s | residu (mmol/g)" % key] = list(f["residuals"])
    df_c = pd.DataFrame(curves) if curves else pd.DataFrame()
    if exp:
        n = max(len(v) for v in exp.values())
        for k in exp:
            exp[k] = list(exp[k]) + [np.nan] * (n - len(exp[k]))
    df_e = pd.DataFrame(exp) if exp else pd.DataFrame()
    return df_c, df_e


class CurveExportDialog(tk.Toplevel):
    """Options d'export des donnees d'ajustement."""

    def __init__(self, master, n_sel, n_ds, n_all, pmin, pmax):
        super().__init__(master)
        self.title(_("Exporter les donnees d'ajustement"))
        self.transient(master)
        self.grab_set()
        self.result = None
        f = ttk.Frame(self, padding=12)
        f.pack(fill="both", expand=True)
        ttk.Label(f, text=_("Que faut-il exporter ?")).grid(row=0, column=0,
                                                          columnspan=4,
                                                          sticky="w")
        self.cb_scope = TCombobox(f, state="readonly", width=52, values=[
            _("Ajustement selectionne (%d)") % n_sel,
            _("Tous les ajustements du jeu de donnees courant (%d)") % n_ds,
            _("Tous les ajustements (%d)") % n_all])
        self.cb_scope.current(0 if n_sel else 1)
        self.cb_scope.grid(row=1, column=0, columnspan=4, sticky="w", pady=4)

        ttk.Label(f, text=_("P min (bar) :")).grid(row=2, column=0, sticky="w")
        self.e_min = ttk.Entry(f, width=12)
        self.e_min.insert(0, fmt(pmin, 5))
        self.e_min.grid(row=2, column=1, sticky="w", padx=3)
        ttk.Label(f, text=_("P max (bar) :")).grid(row=2, column=2, sticky="e")
        self.e_max = ttk.Entry(f, width=12)
        self.e_max.insert(0, fmt(pmax, 5))
        self.e_max.grid(row=2, column=3, sticky="w", padx=3)
        ttk.Label(f, text=_("Nombre de points :")).grid(row=3, column=0, sticky="w")
        self.e_np = ttk.Entry(f, width=12)
        self.e_np.insert(0, "300")
        self.e_np.grid(row=3, column=1, sticky="w", padx=3)
        self.v_exp = tk.BooleanVar(value=True)
        ttk.Checkbutton(f, text=_("Inclure les points experimentaux, la valeur "
                               "calculee et le residu"),
                        variable=self.v_exp).grid(row=4, column=0, columnspan=4,
                                                  sticky="w", pady=3)
        self.v_par = tk.BooleanVar(value=True)
        ttk.Checkbutton(f, text=_("Inclure une feuille avec les parametres et "
                               "les statistiques"),
                        variable=self.v_par).grid(row=5, column=0, columnspan=4,
                                                  sticky="w")
        ttk.Label(f, foreground="#555", justify="left",
                  text=_("La courbe lissee est echantillonnee entre P min et "
                       "P max.\nLaisser vide pour utiliser la gamme des "
                       "donnees experimentales.")).grid(row=6, column=0,
                                                       columnspan=4, sticky="w",
                                                       pady=(6, 2))
        bar = ttk.Frame(f)
        bar.grid(row=7, column=0, columnspan=4, sticky="e", pady=(8, 0))
        ttk.Button(bar, text=_("Annuler"), command=self.destroy).pack(side="right",
                                                                   padx=4)
        ttk.Button(bar, text=_("Exporter..."), command=self._ok).pack(side="right")
        place_window(self)
        self.wait_window(self)

    def _ok(self):
        self.result = dict(scope=self.cb_scope.current(),
                           pmin=to_float_or(self.e_min.get(), np.nan),
                           pmax=to_float_or(self.e_max.get(), np.nan),
                           npts=int(to_float_or(self.e_np.get(), 300)),
                           exp=bool(self.v_exp.get()),
                           par=bool(self.v_par.get()))
        self.destroy()


def show_text_window(master, title, text):
    top = tk.Toplevel(master)
    top.title(title)
    place_window(top, 820, 560)
    txt = tk.Text(top, wrap="none", font=("Consolas", 10))
    vs = ttk.Scrollbar(top, orient="vertical", command=txt.yview)
    txt.configure(yscrollcommand=vs.set)
    txt.pack(side="left", fill="both", expand=True)
    vs.pack(side="right", fill="y")
    txt.insert("1.0", text)
    txt.config(state="disabled")
    return top


# =============================================================================
# 10. ONGLET 4 : IAST
# =============================================================================

class ParamDialog(tk.Toplevel):
    """Saisie manuelle d'un modele et de ses parametres."""

    def __init__(self, master, spec=None):
        super().__init__(master)
        self.title(_("Parametres du constituant"))
        self.transient(master)
        self.grab_set()
        self.result = None
        frm = ttk.Frame(self, padding=10)
        frm.pack(fill="both", expand=True)
        ttk.Label(frm, text=_("Modele :")).grid(row=0, column=0, sticky="w")
        self.cb = TCombobox(frm, state="readonly", width=34,
                               values=[MODELS[k].label for k in MODEL_ORDER])
        self.cb.grid(row=0, column=1, columnspan=3, sticky="w", pady=3)
        self.cb.bind("<<ComboboxSelected>>", lambda e: self._model_changed())
        ttk.Label(frm, text="T (K) :").grid(row=1, column=0, sticky="w")
        self.e_T = ttk.Entry(frm, width=12)
        self.e_T.grid(row=1, column=1, sticky="w")
        ttk.Label(frm, text=_("P0 (bar) :")).grid(row=1, column=2, sticky="e")
        self.e_P0 = ttk.Entry(frm, width=12)
        self.e_P0.grid(row=1, column=3, sticky="w")
        ttk.Label(frm, text=_("P experimentale max (bar) :")).grid(
            row=4, column=0, columnspan=2, sticky="w")
        self.e_pexp = ttk.Entry(frm, width=12)
        self.e_pexp.grid(row=4, column=2, sticky="w")
        ttk.Label(frm, foreground="#555", justify="left",
                  text=_("Sert uniquement a signaler l'extrapolation du modele "
                       "pendant le calcul IAST.")).grid(row=5, column=0,
                                                       columnspan=4, sticky="w")
        self.tbl = EditableTable(frm, ["Parametre", "Valeur"], height=6,
                                 widths=[160, 140])
        self.tbl.grid(row=2, column=0, columnspan=4, sticky="nsew", pady=6)
        frm.rowconfigure(2, weight=1)
        bar = ttk.Frame(frm)
        bar.grid(row=3, column=0, columnspan=4, sticky="e")
        ttk.Button(bar, text=_("Annuler"), command=self.destroy).pack(side="right",
                                                                   padx=4)
        ttk.Button(bar, text=_("Valider"), command=self._ok).pack(side="right")

        spec = spec or dict(model_key="langmuir", params=[10.0, 0.1],
                            ctx={"T": 298.15, "P0": 1.0})
        self.cb.set(MODELS[spec["model_key"]].label)
        self.e_T.insert(0, fmt(spec["ctx"].get("T", 298.15), 2))
        self.e_P0.insert(0, fmt(spec["ctx"].get("P0", 1.0), 4))
        if spec.get("P_exp_max"):
            self.e_pexp.insert(0, fmt(spec["P_exp_max"], 4))
        m = MODELS[spec["model_key"]]
        self.tbl.set_rows([["%s (%s)" % (m.pnames[i], m.punits[i]),
                            fmt(spec["params"][i], 6)] for i in range(m.nparam)])
        place_window(self)
        self.wait_window(self)

    def _key(self):
        lab = self.cb.get()
        for k in MODEL_ORDER:
            if MODELS[k].label == lab:
                return k
        return "langmuir"

    def _model_changed(self):
        m = MODELS[self._key()]
        self.tbl.set_rows([["%s (%s)" % (m.pnames[i], m.punits[i]), ""]
                           for i in range(m.nparam)])

    def _ok(self):
        k = self._key()
        m = MODELS[k]
        rows = self.tbl.get_rows()
        params = [to_float(r[1]) for r in rows[:m.nparam]]
        if any(np.isnan(v) for v in params):
            messagebox.showerror(_("Parametres"), _("Toutes les valeurs doivent etre "
                                               "renseignees."), parent=self)
            return
        pexp = to_float_or(self.e_pexp.get(), np.nan)
        self.result = dict(model_key=k, params=params,
                           ctx={"T": to_float_or(self.e_T.get(), 298.15),
                                "P0": to_float_or(self.e_P0.get(), 1.0)},
                           P_exp_max=(float(pexp) if np.isfinite(pexp)
                                      and pexp > 0 else None))
        self.destroy()


class CompRow(ttk.Frame):
    """Ligne de definition d'un constituant du melange."""

    def __init__(self, master, app, idx, default_name="CO2"):
        super().__init__(master)
        self.app = app
        self.idx = idx
        self.spec = None
        self.fit = None     # (jeu, modele) de l'ajustement choisi, None si saisie
        ttk.Label(self, text=_("Constituant %d :") % (idx + 1), width=13
                  ).grid(row=0, column=0, sticky="w")
        self.e_name = ttk.Entry(self, width=9)
        self.e_name.insert(0, default_name)
        self.e_name.grid(row=0, column=1, sticky="w", padx=2)
        ttk.Label(self, text="y =").grid(row=0, column=2, sticky="e", padx=(8, 0))
        self.e_y = ttk.Entry(self, width=8)
        self.e_y.insert(0, "0.5")
        self.e_y.grid(row=0, column=3, sticky="w", padx=2)
        ttk.Button(self, text=_("Editer..."), width=9,
                   command=self.edit).grid(row=0, column=4, padx=2, sticky="e")
        self.cb_src = TCombobox(self, state="readonly", width=44)
        self.cb_src.grid(row=1, column=0, columnspan=5, sticky="ew", padx=2,
                         pady=(3, 0))
        self.cb_src.bind("<<ComboboxSelected>>", lambda e: self._src_changed())
        self.lbl = wrap_to_width(ttk.Label(self, text="-", foreground="#333",
                                           justify="left"))
        self.lbl.grid(row=2, column=0, columnspan=5, sticky="ew", pady=(0, 4))
        self.columnconfigure(4, weight=1)

    def fit_index(self):
        """Position actuelle de l'ajustement choisi dans la liste, ou None."""
        for j, f in enumerate(self.app.fits):
            if (f.get("dataset"), f.get("model_key")) == self.fit:
                return j
        return None

    def refresh_sources(self):
        """Met la liste a jour. L'ajustement choisi est suivi par son jeu et
        son modele, pas par son rang : refaire ou supprimer un ajustement
        ne change plus le constituant sans prevenir."""
        vals = ["%d. %s" % (i + 1, f["label"]) for i, f in
                enumerate(self.app.fits)] + ["Saisie manuelle..."]
        self.cb_src["values"] = vals
        j = self.fit_index()
        if j is not None:
            self.use_fit(self.app.fits[j])
        self.cb_src.set(vals[j] if j is not None
                        else ("Saisie manuelle..." if self.spec else ""))

    def _src_changed(self):
        s = self.cb_src.get()
        if s == "Saisie manuelle...":
            self.edit()
            return
        try:
            self.use_fit(self.app.fits[int(s.split(".")[0]) - 1])
        except Exception:
            return
        self.app.tab_iast.auto_pmax()

    def use_fit(self, f):
        self.fit = (f.get("dataset"), f.get("model_key"))
        self.spec = dict(model_key=f["model_key"], params=list(f["params"]),
                         ctx=dict(f["ctx"]),
                         P_exp_max=f.get("P_exp_max",
                                         float(np.max(f["P"])) if f.get("P")
                                         else None))
        self._update_label()

    def edit(self):
        dlg = ParamDialog(self, self.spec)
        if dlg.result:
            self.spec, self.fit = dlg.result, None
            self.cb_src.set("Saisie manuelle...")
            self._update_label()

    def _update_label(self):
        if not self.spec:
            self.lbl.config(text="-")
            return
        m = MODELS[self.spec["model_key"]]
        txt = "%s : %s" % (m.label, ", ".join(
            "%s=%s" % (m.pnames[i], fmt(self.spec["params"][i], 4))
            for i in range(m.nparam)))
        if m.needs:
            txt += _("   [T=%s K, P0=%s bar]") % (fmt(self.spec["ctx"].get("T"), 1),
                                               fmt(self.spec["ctx"].get("P0"), 3))
        pm = self.spec.get("P_exp_max")
        txt += "   P_exp_max=%s bar" % (fmt(pm, 2) if pm else _("non renseignee"))
        self.lbl.config(text=txt)

    def y_value(self):
        return to_float(self.e_y.get())

    def name(self):
        return self.e_name.get().strip() or "C%d" % (self.idx + 1)


MIX_PRESETS = [
    ("CO2/CH4  50:50", [("CO2", 0.50), ("CH4", 0.50)]),
    ("CO2/CH4  25:75", [("CO2", 0.25), ("CH4", 0.75)]),
    ("CO2/CH4  75:25", [("CO2", 0.75), ("CH4", 0.25)]),
    ("CO2/N2  15:85", [("CO2", 0.15), ("N2", 0.85)]),
    ("CO2/H2  40:60", [("CO2", 0.40), ("H2", 0.60)]),
    ("CH4/N2  50:50", [("CH4", 0.50), ("N2", 0.50)]),
    ("CH4/H2   50:50", [("CH4", 0.50), ("H2", 0.50)]),
    ("C2H2/CO2  50:50", [("C2H2", 0.50), ("CO2", 0.50)]),
    ("C2H2/C2H4  1:99", [("C2H2", 0.01), ("C2H4", 0.99)]),
    ("C2H4/C2H6  50:50", [("C2H4", 0.50), ("C2H6", 0.50)]),
    ("C3H6/C3H8  50:50", [("C3H6", 0.50), ("C3H8", 0.50)]),
    ("Xe/Kr  20:80", [("Xe", 0.20), ("Kr", 0.80)]),
    ("CO2/CH4/H2 1:1:1", [("CO2", 1 / 3.), ("CH4", 1 / 3.), ("H2", 1 / 3.)]),
]
# usage courant de chaque melange (affiche en info-bulle)
MIX_USES = {
    "CO2/CH4": "biogaz, gaz naturel", "CO2/N2": "fumees de combustion",
    "CO2/H2": "precombustion (gaz de synthese)", "CH4/N2": "gaz naturel, grisou",
    "CH4/H2": "purification de l'hydrogene", "C2H2/CO2": "purification de l'acetylene",
    "C2H2/C2H4": "purification de l'ethylene", "C2H4/C2H6": "olefine / paraffine",
    "C3H6/C3H8": "olefine / paraffine", "Xe/Kr": "gaz rares (retraitement nucleaire)",
    "CO2/CH4/H2": "ternaire",
}


class TabIAST(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master, padding=10)
        self.app = app
        self.df = None

        self.names, self.specs, self._pb = [], [], []
        self._pmax = "60"       # derniere valeur de P max proposee (auto_pmax)

        # Reglages a gauche (colonne defilante), resultats a droite sur toute
        # la hauteur : empiles, les reglages ne laissaient aux graphiques
        # qu'une bande illisible, voire rien dans une petite fenetre.
        pan = ttk.PanedWindow(self, orient="horizontal")
        pan.pack(fill="both", expand=True)
        lcol = ttk.Frame(pan)
        right = ttk.Frame(pan)
        pan.add(lcol, weight=0)
        pan.add(right, weight=1)
        bar = ttk.Frame(lcol, style="Card.TFrame", padding=10)
        bar.pack(side="bottom", fill="x", pady=(8, 0))
        tip(ttk.Button(bar, text=_("Lancer le calcul IAST"),
                       style="Primary.TButton", command=self.run),
            _("Resolution sur la pression d'etalement (F5)")).pack(fill="x")
        b2 = ttk.Frame(bar, style="Card.TFrame")
        b2.pack(fill="x", pady=(6, 0))
        ttk.Button(b2, text=_("Exporter en Excel"), command=self.export
                   ).pack(side="left", fill="x", expand=True, padx=(0, 3))
        ttk.Button(b2, text=_("Vers Graphiques"), command=self.send_to_plot
                   ).pack(side="left", fill="x", expand=True, padx=(3, 0))
        lwrap = ScrollFrame(lcol)
        lwrap.pack(fill="both", expand=True)

        top = card(lwrap.inner, _("1. Constituants du melange"))
        top.pack(fill="x", pady=(0, 8))
        hdr = ttk.Frame(top.body, style="Card.TFrame")
        hdr.pack(fill="x", pady=(0, 6))
        ttk.Label(hdr, text=_("Nombre de constituants :"),
                  style="Card.TLabel").pack(side="left")
        self.var_n = tk.IntVar(value=2)
        for n in (2, 3):
            ttk.Radiobutton(hdr, text="  %d  " % n, value=n, variable=self.var_n,
                            command=self._n_changed).pack(side="left", padx=3)
        # sous l'en-tete, donc visible sans defiler : usage du melange type
        # ou, a l'arrivee dans l'onglet, mention "propose ..., a verifier"
        self.lbl_preset = wrap_to_width(ttk.Label(
            top.body, text="", style="Muted.TLabel", justify="left"))
        self.lbl_preset.pack(fill="x")
        self.rows = []
        for i, nm in enumerate(("CO2", "CH4", "H2")):
            r = CompRow(top.body, app, i, nm)
            r.pack(fill="x", pady=2)
            self.rows.append(r)
        # repere : les lignes de constituants se replacent avant ce bouton
        self._rows_end = tip(ttk.Button(
            top.body, text=_("Normaliser les fractions molaires"),
            style="Ghost.TButton", command=self.normalize),
            _("Ramene la somme des y a 1"))
        self._rows_end.pack(anchor="w")

        pre = ttk.Frame(top.body, style="Card.TFrame")
        pre.pack(fill="x", pady=(8, 0))
        ttk.Label(pre, text=_("Melanges types :"), style="Card.TLabel").pack(
            side="left", padx=(0, 6))
        self.cb_preset = TCombobox(pre, state="readonly", width=20,
                                      values=[lab for lab, _sp in MIX_PRESETS])
        self.cb_preset.pack(side="left", padx=2)
        self.cb_preset.bind("<<ComboboxSelected>>",
                            lambda e: self._preset_selected())
        tip(self.cb_preset, _("Configure les constituants et leurs fractions "
            "molaires, puis associe automatiquement l'ajustement disponible "
            "pour chaque gaz."))

        cfg = card(lwrap.inner, _("2. Conditions de calcul"))
        cfg.pack(fill="x")
        g = cfg.body
        ttk.Label(g, text=_("Mode :"), style="Card.TLabel").grid(row=0, column=0,
                                                              sticky="w", pady=3)
        self.cb_mode = TCombobox(g, state="readonly", width=30,
                                    values=["Balayage en pression totale",
                                            "Balayage en composition (y1)"])
        self.cb_mode.set("Balayage en pression totale")
        self.cb_mode.grid(row=0, column=1, columnspan=3, sticky="w", padx=(0, 6))
        self.e_pmin = field(g, _("P min (bar) :"), ttk.Entry, 9, 1, 0,
                            _("Borne basse du balayage en pression"))
        self.e_pmin.insert(0, "0.1")
        self.e_pmax = field(g, _("P max (bar) :"), ttk.Entry, 9, 1, 2,
                            _("Borne haute. Au-dela de la pression mesuree, "
                            "le calcul repose sur l'extrapolation du modele."))
        self.e_pmax.insert(0, self._pmax)
        self.e_np = field(g, _("Points :"), ttk.Entry, 9, 2, 0,
                          _("Nombre de points calcules"))
        self.e_np.insert(0, "40")
        self.var_log = tk.BooleanVar(value=False)
        ttk.Checkbutton(g, text=_("Echelle logarithmique en pression"),
                        variable=self.var_log).grid(row=3, column=0,
                                                    columnspan=4, sticky="w",
                                                    pady=3)
        ttk.Label(g, text=_("P fixe pour balayage en y (bar) :"),
                  style="Card.TLabel").grid(row=4, column=0, columnspan=3,
                                            sticky="w", pady=3)
        self.e_pfix = tip(ttk.Entry(g, width=9),
                          _("Pression totale imposee lors du balayage en "
                          "composition"))
        self.e_pfix.grid(row=4, column=3, sticky="w")
        self.e_pfix.insert(0, "1.0")

        self.lbl_warn = wrap_to_width(ttk.Label(
            right, text="", style="MutedBg.TLabel", justify="left",
            foreground=UI["warn"]))
        self.lbl_warn.pack(fill="x", pady=(0, 6))
        mid = ttk.PanedWindow(right, orient="vertical")
        mid.pack(fill="both", expand=True)
        self._pan = mid
        self._table_visible = True
        pf = ttk.Frame(mid)
        self._tf = ttk.Frame(mid)
        mid.add(pf, weight=3)
        mid.add(self._tf, weight=1)

        cg = card(pf)       # sans titre : la ligne "Afficher" en tient lieu
        cg.pack(fill="both", expand=True)
        opt = ttk.Frame(cg.body, style="Card.TFrame")
        opt.pack(fill="x", pady=(0, 6))
        ttk.Label(opt, text=_("Afficher :"), style="Card.TLabel").pack(side="left",
                                                                    padx=(0, 6))
        self.var_pq = tk.BooleanVar(value=True)
        self.var_ps = tk.BooleanVar(value=True)
        self.var_px = tk.BooleanVar(value=False)
        self.var_pp = tk.BooleanVar(value=False)
        for txt, var, hint in (
                (_("quantites"), self.var_pq, "q_i et q_total"),
                (_("selectivites"), self.var_ps, "S_i/j"),
                (_("fractions x"), self.var_px,
                 _("composition de la phase adsorbee")),
                ("P0", self.var_pp,
                 _("pressions de reference exigees par l'IAST"))):
            cb = ttk.Checkbutton(opt, text=txt, variable=var,
                                 command=lambda: self.draw())
            cb.pack(side="left", padx=4)
            tip(cb, hint)
        self.btn_table = ttk.Button(opt, text=_("Masquer le tableau"),
                                    style="Ghost.TButton",
                                    command=self.toggle_table)
        self.btn_table.pack(side="right")
        tip(self.btn_table, _("Donne toute la hauteur aux graphiques"))
        self.fig = Figure(figsize=(4.5, 3.2), dpi=100, facecolor=UI["card"])
        self.ax1 = None
        self.ax2 = None
        self.canvas = make_canvas(cg.body, self.fig, (self._render, "IAST", app))

        ct = card(self._tf, _("Resultats"),
                  _("orange : P0 au-dela du domaine mesure  -  rouge : au-dela "
                  "du double"))
        ct.pack(fill="both", expand=True, pady=(8, 0))
        tvf = ttk.Frame(ct.body, style="Card.TFrame")
        self.tv = ttk.Treeview(tvf, show="headings", height=4)
        vs = ttk.Scrollbar(tvf, orient="vertical", command=self.tv.yview)
        hs = ttk.Scrollbar(ct.body, orient="horizontal", command=self.tv.xview)
        self.tv.configure(yscrollcommand=vs.set, xscrollcommand=hs.set)
        hs.pack(side="bottom", fill="x")
        tvf.pack(fill="both", expand=True)
        self.tv.pack(side="left", fill="both", expand=True)
        vs.pack(side="right", fill="y")
        set_sash(pan, 0, 450)
        set_sash(mid, 0, 0.58)
        self._n_changed()

    def _preset_selected(self):
        lab = self.cb_preset.get()
        spec = dict(MIX_PRESETS).get(lab)
        if spec:
            self.apply_preset(spec, lab)
            use = MIX_USES.get("/".join(g for g, _y in spec), "")
            self.lbl_preset.config(text=_(use))

    # modeles sans constante de Henry finie (signales a l'IAST)
    _NO_HENRY = ("dr", "dr_p0", "da", "da_p0", "freundlich")

    def _fit_T(self, f):
        """Temperature du jeu ajuste (celle notee a l'ajustement a defaut)."""
        for d in self.app.datasets:
            if d["name"] == f.get("dataset"):
                return float(d["T"])
        return float(f.get("ctx", {}).get("T", np.nan))

    def _fit_score(self, jf, ref, common=()):
        """Classement des ajustements pour un melange type. 1er constituant :
        une temperature ou tous les gaz du melange ont un ajustement
        (common), jeu 'Total' le plus recent, puis modele avec constante de
        Henry finie et meilleur AICc. Constituants suivants : meme
        temperature, meme echantillon et meme modele que le premier."""
        j, f = jf
        names = [x["name"] for x in self.app.datasets]
        di = names.index(f.get("dataset")) if f.get("dataset") in names else -1
        total = int(di >= 0 and self.app.datasets[di].get("kind") == "Total")
        henry = int(f.get("model_key") not in self._NO_HENRY)
        aicc = f.get("stats", {}).get("AICc", np.inf)
        aicc = -aicc if np.isfinite(aicc) else -np.inf
        T = self._fit_T(f)
        if ref is None:
            return (int(np.isfinite(T) and round(T) in common), total, di,
                    henry, aicc, j)
        same_T = int(np.isfinite(T) and abs(T - ref["T"]) < 0.5)
        same_s = int(sample_label(f.get("dataset", ""), f.get("gas")).lower()
                     == ref["samp"])
        same_m = int(f.get("model_key") == ref["model"])
        return (same_T, same_s, total, same_m, henry, aicc, di, j)

    def apply_preset(self, spec, label=""):
        """Applique un melange type : noms, fractions et modeles associes."""
        self.var_n.set(len(spec))
        self._n_changed()
        missing = []
        ref = None
        # temperatures (arrondies) ou chaque gaz du melange a un ajustement :
        # sans cela le premier gaz pouvait etre pris a 273 K et le second a 303 K
        common = set.intersection(*[
            {round(t) for t in (self._fit_T(f) for f in self.app.fits
                                if str(f.get("gas", "")).upper() == gas.upper())
             if np.isfinite(t)} for gas, _y in spec])
        for i, (gas, y) in enumerate(spec):
            if i >= len(self.rows):
                break
            r = self.rows[i]
            r.e_name.delete(0, "end")
            r.e_name.insert(0, gas)
            r.e_y.delete(0, "end")
            r.e_y.insert(0, "%.6g" % y)
            r.spec = r.fit = None
            # ajustement du gaz : de preference a la meme temperature, sur le
            # meme echantillon et avec le meme modele que le premier constituant,
            # sur un jeu 'Total' ; a egalite, le plus recent
            cand = [(j, f) for j, f in enumerate(self.app.fits)
                    if str(f.get("gas", "")).upper() == gas.upper()]
            if cand:
                j, f = max(cand,
                           key=lambda jf: self._fit_score(jf, ref, common))
                if ref is None:
                    ref = dict(T=self._fit_T(f),
                               samp=sample_label(f.get("dataset", ""),
                                                 f.get("gas")).lower(),
                               model=f.get("model_key"))
                r.fit = (f.get("dataset"), f.get("model_key"))
            else:
                missing.append(gas)
            r.refresh_sources()
            r._update_label()
        self.auto_pmax()
        self.app.log(_("Melange type applique : %s") % (label or spec))
        if missing:
            messagebox.showinfo(
                _("Melange type"),
                _("Fractions molaires configurees.\n\n"
                "Aucun ajustement disponible pour : %s.\n"
                "Ajustez d'abord ces isothermes dans l'onglet Ajustement, "
                "ou saisissez les parametres a la main (bouton 'Editer...').")
                % ", ".join(missing), parent=self)
        else:
            self.app.set_status(_("Melange %s pret - lancez le calcul IAST.")
                                % (label or ""))

    def toggle_table(self):
        """Masque ou reaffiche le tableau pour agrandir les graphiques."""
        try:
            if self._table_visible:
                self._pan.forget(self._tf)
                self._table_visible = False
                self.btn_table.config(text=_("Afficher le tableau"))
            else:
                self._pan.add(self._tf, weight=1)
                self._table_visible = True
                self.btn_table.config(text=_("Masquer le tableau"))
                set_sash(self._pan, 0, 0.58)
        except Exception:
            pass

    def _n_changed(self):
        n = self.var_n.get()
        for i, r in enumerate(self.rows):
            if i < n:
                r.pack(fill="x", pady=1, before=self._rows_end)
            else:
                r.pack_forget()
        self.normalize()

    def reset(self):
        """Oublie constituants et resultats (nouvelle session, ouverture)."""
        self.df, self._df_plot = None, None
        self.names, self.specs, self._pb = [], [], []
        for r in self.rows:
            r.spec = r.fit = None
            r._update_label()
        self.cb_preset.set("")
        self.lbl_preset.config(text="")
        self.lbl_warn.config(text="")
        self.tv.delete(*self.tv.get_children())
        self.draw()

    def refresh(self):
        for r in self.rows:
            r.refresh_sources()
        if self.app.fits and not any(r.spec for r in
                                     self.rows[:self.var_n.get()]):
            self._propose()

    def _propose(self):
        """Premier passage dans l'onglet : un constituant par gaz ajuste,
        chacun avec l'ajustement de son gaz (et non les premiers de la
        liste). Ordre et fractions du melange type s'il en existe un."""
        gases = [g for g in dict.fromkeys(str(f.get("gas", ""))
                                          for f in self.app.fits) if g][:3]
        if len(gases) < 2:
            return
        for lab, spec in MIX_PRESETS:
            if {g for g, _y in spec} == set(gases):
                break
        else:
            lab, spec = "/".join(gases), [(g, 1.0 / len(gases)) for g in gases]
        lab = _(lab) + " " + _("(propose d'apres les ajustements, a verifier)")
        self.apply_preset(spec, lab)
        self.lbl_preset.config(text=lab)

    def auto_pmax(self):
        """Propose pour P max la plus petite pression mesuree des
        constituants, tant que l'utilisateur n'a pas saisi la sienne."""
        pm = [r.spec["P_exp_max"] for r in self.rows[:self.var_n.get()]
              if r.spec and r.spec.get("P_exp_max")]
        if pm and self.e_pmax.get().strip() == self._pmax:
            self._pmax = ("%.4f" % min(pm)).rstrip("0").rstrip(".")
            self.e_pmax.delete(0, "end")
            self.e_pmax.insert(0, self._pmax)

    def _check(self):
        """Incoherences entre constituants : gaz, isotherme en exces,
        ajustement pris deux fois, temperatures differentes."""
        pb, Ts, seen = [], [], set()
        kinds = {d["name"]: d.get("kind") for d in self.app.datasets}
        known = {g.upper() for g in GAS_DB}
        for r in self.rows[:self.var_n.get()]:
            j = r.fit_index()
            T = to_float_or(r.spec["ctx"].get("T"), np.nan)
            if j is not None:
                f = self.app.fits[j]
                T = self._fit_T(f)
                gas = str(f.get("gas", ""))
                if r.name().upper() in known and r.name().upper() != gas.upper():
                    pb.append(_("%s : l'ajustement choisi est celui de %s")
                              % (r.name(), gas))
                if kinds.get(f.get("dataset")) == "Exces":
                    pb.append(_("%s : isotherme en exces (%s)")
                              % (r.name(), f.get("dataset")))
                if r.fit in seen:
                    pb.append(_("%s : meme ajustement qu'un autre constituant")
                              % r.name())
                seen.add(r.fit)
            Ts.append(T)
        Ts = [t for t in Ts if np.isfinite(t)]
        if Ts and max(Ts) - min(Ts) > 0.5:
            pb.append(_("temperatures differentes : %s K")
                      % ", ".join(fmt(t, 2) for t in Ts))
        return pb

    def normalize(self):
        n = self.var_n.get()
        ys = [self.rows[i].y_value() for i in range(n)]
        ys = [0.0 if (v is None or np.isnan(v) or v < 0) else v for v in ys]
        s = sum(ys)
        if s <= 0:
            ys = [1.0 / n] * n
        else:
            ys = [v / s for v in ys]
        for i in range(n):
            self.rows[i].e_y.delete(0, "end")
            self.rows[i].e_y.insert(0, "%.4f" % ys[i])
        return ys

    def build_components(self):
        n = self.var_n.get()
        comps, names, specs = [], [], []
        warn = []
        for i in range(n):
            r = self.rows[i]
            if not r.spec:
                raise ValueError(_("Constituant %d : aucun modele defini "
                                 "(choisissez un ajustement ou saisissez les "
                                 "parametres).") % (i + 1))
            m = MODELS[r.spec["model_key"]]
            comps.append(SpreadingPressure(m, r.spec["ctx"], r.spec["params"],
                                           P_exp_max=r.spec.get("P_exp_max")))
            names.append(r.name())
            specs.append(r.spec)
            if m.key in ("dr", "dr_p0", "da", "da_p0"):
                warn.append(m.label)
            if m.key == "freundlich" and r.spec["params"][1] >= 1.0:
                warn.append("Freundlich n>=1")
        self._warn_models = (_("Modeles %s : constante de Henry nulle ou non "
                             "definie, IAST discutable a tres basse pression.")
                             % ", ".join(sorted(set(warn)))) if warn else ""
        self._no_pexp = [names[i] for i in range(n)
                         if not specs[i].get("P_exp_max")]
        self.lbl_warn.config(text=self._warn_models)
        return comps, names, specs

    def run(self):
        try:
            comps, names, specs = self.build_components()
        except Exception as e:
            messagebox.showerror("IAST", str(e), parent=self)
            return
        self._pb = self._check()
        if self._pb and not messagebox.askyesno(
                "IAST", _("Les constituants semblent incoherents :\n\n  - %s"
                          "\n\nLancer le calcul quand meme ?")
                % "\n  - ".join(self._pb), parent=self):
            return
        ys = self.normalize()
        try:
            npts = max(3, int(to_float_or(self.e_np.get(), 40)))
            if self.cb_mode.get().startswith("Balayage en pression"):
                pmin = to_float_or(self.e_pmin.get(), np.nan)
                pmax = to_float_or(self.e_pmax.get(), np.nan)
                if not (pmin > 0 and pmax > pmin):
                    raise ValueError(_("Gamme de pression invalide."))
                P = (np.logspace(math.log10(pmin), math.log10(pmax), npts)
                     if self.var_log.get() else np.linspace(pmin, pmax, npts))
                df = iast_scan(P, ys, comps, names)
                self.mode = "P"
            else:
                pfix = to_float_or(self.e_pfix.get(), 1.0)
                y1 = np.linspace(0.001, 0.999, npts)
                rest = None
                if len(comps) == 3:
                    rest = [max(ys[1], 1e-9), max(ys[2], 1e-9)]
                df = iast_scan_composition(pfix, y1, comps, names, rest)
                self.mode = "y"
        except Exception as e:
            messagebox.showerror("IAST", "%s\n\n%s" % (e, traceback.format_exc()),
                                 parent=self)
            return
        self.df = df
        self.names = names
        self.specs = specs
        self.fill_table(df)
        self.draw(df, names)
        nbad = int((~df["Convergence"]).sum())
        self.app.log(_("IAST : %d points calcules, %d non convergents.")
                     % (len(df), nbad))
        self._update_warning(df, names)
        self.app.mark_dirty()

    def _update_warning(self, df, names):
        """Signale l'extrapolation implicite des modeles de corps purs."""
        msgs = []
        if self._pb:
            msgs.append(_("A VERIFIER : ") + " ; ".join(self._pb))
        if getattr(self, "_warn_models", ""):
            msgs.append(self._warn_models)
        col = "Extrapolation max (P0/P_exp)"
        r = df[col].values if col in df else np.array([np.nan])
        if np.any(np.isfinite(r)):
            rmax = float(np.nanmax(r))
            nb = int(np.sum(r > 2.0))
            worst = {}
            for nm in names:
                c = "P0/P_exp_%s" % nm
                if c in df and np.any(np.isfinite(df[c].values)):
                    worst[nm] = float(np.nanmax(df[c].values))
            det = ", ".join("%s x%.1f" % (k, v) for k, v in
                            sorted(worst.items(), key=lambda kv: -kv[1]))
            if rmax > 2.0:
                msgs.append(_("EXTRAPOLATION : les P0 requis depassent jusqu'a "
                            "x%.1f la pression mesuree (%s) sur %d point(s). "
                            "Ces points reposent sur l'extrapolation des "
                            "isothermes de corps purs, pas sur des mesures.")
                            % (rmax, det, nb))
            elif rmax > 1.0:
                msgs.append(_("Extrapolation legere : P0 max = x%.1f la pression "
                            "mesuree (%s).") % (rmax, det))
            else:
                msgs.append(_("Domaine valide : tous les P0 restent dans la "
                            "gamme mesuree (max x%.2f).") % rmax)
        if getattr(self, "_no_pexp", None):
            msgs.append(_("P experimentale max non renseignee pour : %s "
                        "(extrapolation non controlee).")
                        % ", ".join(self._no_pexp))
        txt = "  |  ".join(msgs)
        self.lbl_warn.config(text=txt[:600])
        col_fg = ("#a00000" if self._pb or "EXTRAPOLATION" in txt
                  else "#a06000")
        try:
            self.lbl_warn.config(foreground=col_fg)
        except Exception:
            pass
        for m in msgs:
            self.app.log(_("IAST - ") + m)

    def fill_table(self, df):
        cols = list(df.columns)
        self.tv["columns"] = cols
        self.tv.delete(*self.tv.get_children())
        for c in cols:
            w = max(80, min(160, 9 * len(c)))
            self.tv.heading(c, text=tr_col(c, True))
            self.tv.column(c, width=w, minwidth=w, anchor="e", stretch=False)
        self.tv.tag_configure("extrap_fort", background="#ffd6d6")
        self.tv.tag_configure("extrap_leger", background="#fff2cc")
        self.tv.tag_configure("nonconv", background="#dddddd")
        rcol = "Extrapolation max (P0/P_exp)"
        for _u, row in df.iterrows():
            tag = ""
            if not bool(row.get("Convergence", True)):
                tag = "nonconv"
            else:
                r = row.get(rcol, np.nan)
                if np.isfinite(r):
                    if r > 2.0:
                        tag = "extrap_fort"
                    elif r > 1.0:
                        tag = "extrap_leger"
            self.tv.insert("", "end", tags=((tag,) if tag else ()),
                           values=[fmt(v, 5) if isinstance(v, (int, float,
                                                               np.floating))
                                   else str(v) for v in row.tolist()])

    def draw(self, df=None, names=None):
        if df is not None:
            self._df_plot, self._names_plot = df, list(names or [])
        self._render(self.fig)
        self.canvas.draw_idle()

    def _render(self, fig):
        """Trace les panneaux demandes sur la figure fournie."""
        fig.clear()
        df = getattr(self, "_df_plot", None)
        names = getattr(self, "_names_plot", None)
        if df is None or not names:
            return
        mode = getattr(self, "mode", "P")
        xcol = "P_total (bar)" if mode == "P" else "y_%s" % names[0]
        if xcol not in df:
            return
        x = df[xcol].values
        panels = [k for k, v in (("q", self.var_pq), ("S", self.var_ps),
                                 ("x", self.var_px), ("P0", self.var_pp))
                  if v.get()]
        if not panels:
            panels = ["q"]
        axes = panel_axes(fig, len(panels), sharex=True)

        # zone d'extrapolation
        col = "Extrapolation max (P0/P_exp)"
        x0 = None
        if col in df and mode == "P":
            v = df[col].values
            bad = np.isfinite(v) & (v > 2.0)
            if np.any(bad):
                x0 = float(np.min(x[bad]))

        for ax, kind in zip(axes, panels):
            if x0 is not None:
                ax.axvspan(x0, float(np.max(x)), color="#c00000", alpha=0.07,
                           zorder=0)
                ax.axvline(x0, color="#c00000", ls=":", lw=1.2)
            if kind == "q":
                for i, nm in enumerate(names):
                    c = "q_%s (mmol/g)" % nm
                    if c in df:
                        ax.plot(x, df[c].values, "-o", ms=3.5,
                                color=PALETTE[i % len(PALETTE)], label=nm)
                if "q_total (mmol/g)" in df:
                    ax.plot(x, df["q_total (mmol/g)"].values, "--k", lw=1.2,
                            label=_("total"))
                ax.set_ylabel(_("q adsorbee (mmol/g)"))
            elif kind == "S":
                k = 0
                for i in range(len(names)):
                    for j in range(i + 1, len(names)):
                        c = "S_%s/%s" % (names[i], names[j])
                        if c in df:
                            ax.plot(x, df[c].values, "-s", ms=3.5,
                                    color=PALETTE[k % len(PALETTE)], label=c)
                            k += 1
                ax.set_ylabel(_("Selectivite"))
            elif kind == "x":
                for i, nm in enumerate(names):
                    c = "x_%s" % nm
                    if c in df:
                        ax.plot(x, df[c].values, "-^", ms=3.5,
                                color=PALETTE[i % len(PALETTE)], label=nm)
                ax.set_ylabel(_("Fraction adsorbee x"))
                ax.set_ylim(0, 1)
            else:
                for i, nm in enumerate(names):
                    c = "P0_%s (bar)" % nm
                    if c in df:
                        ax.plot(x, df[c].values, "-v", ms=3.5,
                                color=PALETTE[i % len(PALETTE)],
                                label="P0 %s" % nm)
                    pm = None
                    if getattr(self, "specs", None) and i < len(self.specs):
                        pm = self.specs[i].get("P_exp_max")
                    if pm:
                        ax.axhline(pm, color=PALETTE[i % len(PALETTE)], ls=":",
                                   lw=1)
                ax.set_ylabel(_("P0 (bar)"))
                ax.set_yscale("log")
            ax.grid(True, ls="--", alpha=0.5)
            ax.legend(fontsize=8, ncol=2)
            if mode == "P" and self.var_log.get():
                ax.set_xscale("log")
            if ax.get_subplotspec().is_last_row():
                ax.set_xlabel(xcol if mode == "P" else
                              _("Fraction molaire gazeuse y_%s") % names[0])
        try:
            fig.tight_layout()
        except Exception:
            pass

    def export(self):
        if self.df is None:
            messagebox.showwarning("IAST", _("Lancez d'abord un calcul."), parent=self)
            return
        path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                            filetypes=[("Excel", "*.xlsx")],
                                            initialfile=_("resultats_IAST.xlsx"))
        if not path:
            return
        meta = []
        for i, nm in enumerate(self.names):
            m = MODELS[self.specs[i]["model_key"]]
            d = {"Constituant": nm, "Modele": m.label}
            for j, pn in enumerate(m.pnames):
                d[pn] = self.specs[i]["params"][j]
            d["T (K)"] = self.specs[i]["ctx"].get("T")
            d["P0 (bar)"] = self.specs[i]["ctx"].get("P0")
            meta.append(d)
        with pd.ExcelWriter(path, engine="openpyxl") as w:
            self.df.to_excel(w, sheet_name="IAST", index=False)
            pd.DataFrame(meta).to_excel(w, sheet_name=tr_col("Modeles"), index=False)
        self.app.log(_("Export IAST : %s") % path)
        messagebox.showinfo(_("Export"), _("Fichier enregistre :\n%s") % path,
                            parent=self)

    def send_to_plot(self):
        if self.df is None:
            return
        xcol = "P_total (bar)" if self.mode == "P" else "y_%s" % self.names[0]
        x = self.df[xcol].values
        for nm in self.names:
            self.app.add_series("IAST q %s" % nm, x,
                                self.df["q_%s (mmol/g)" % nm].values, kind="ligne")
        for i in range(len(self.names)):
            for j in range(i + 1, len(self.names)):
                c = "S_%s/%s" % (self.names[i], self.names[j])
                if c in self.df:
                    self.app.add_series("IAST %s" % c, x, self.df[c].values,
                                        kind="ligne")
        self.app.tab_plot.refresh_series()
        self.app.log(_("Series IAST envoyees vers l'onglet Graphiques."))


# =============================================================================
# 10 bis. ONGLET 5 : CHALEUR ISOSTERIQUE D'ADSORPTION
# =============================================================================

QST_METHODS = ["Clausius-Clapeyron (modeles ajustes)",
               "Viriel (points mesures)", "Les deux methodes"]
QST_BEST = "Meilleur AICc par isotherme"


class TabQst(ttk.Frame):
    """Chaleur isosterique a partir d'isothermes a plusieurs temperatures."""

    def __init__(self, master, app):
        super().__init__(master, padding=10)
        self.app = app
        self.df = None          # resultats (une ligne par quantite n)
        self.vf = None          # ajustement du viriel
        self.entries = []       # isothermes ajustees utilisees (Clausius-Clapeyron)
        self.tables = []
        self.config_used = {}
        self._items = []        # jeux affiches dans la liste

        # meme disposition que l'onglet IAST : reglages a gauche (colonne
        # defilante), resultats a droite sur toute la hauteur
        pan = ttk.PanedWindow(self, orient="horizontal")
        pan.pack(fill="both", expand=True)
        lcol = ttk.Frame(pan)
        right = ttk.Frame(pan)
        pan.add(lcol, weight=0)
        pan.add(right, weight=1)
        bar = ttk.Frame(lcol, style="Card.TFrame", padding=10)
        bar.pack(side="bottom", fill="x", pady=(8, 0))
        tip(ttk.Button(bar, text=_("Calculer la chaleur isosterique"),
                       style="Primary.TButton", command=self.run),
            _("Qst en fonction de la quantite adsorbee (F5)")).pack(fill="x")
        b2 = ttk.Frame(bar, style="Card.TFrame")
        b2.pack(fill="x", pady=(6, 0))
        ttk.Button(b2, text=_("Exporter en Excel"), command=self.export
                   ).pack(side="left", fill="x", expand=True, padx=(0, 3))
        ttk.Button(b2, text=_("Vers Graphiques"), command=self.send_to_plot
                   ).pack(side="left", fill="x", expand=True, padx=(3, 0))
        lwrap = ScrollFrame(lcol)
        lwrap.pack(fill="both", expand=True)

        top = card(lwrap.inner, _("1. Isothermes a combiner"))
        top.pack(fill="x", pady=(0, 8))
        g = top.body
        wrap_to_width(ttk.Label(
            g, style="Muted.TLabel", justify="left",
            text=_("un meme gaz sur un meme materiau, mesure a plusieurs "
                   "temperatures"))).grid(row=0, column=0, columnspan=2,
                                          sticky="we")
        self.cb_gas = field(g, _("Gaz :"), TCombobox, 12, 1, 0, None,
                            state="readonly")
        self.cb_gas.bind("<<ComboboxSelected>>", lambda e: self._fill_list())
        self.cb_method = field(
            g, _("Methode :"), TCombobox, 36, 2, 0,
            _("Clausius-Clapeyron : isosteres calculees avec les "
            "modeles ajustes, sans sortir des quantites mesurees.\n"
            "Viriel : une seule equation ajustee sur tous les points ; adaptee "
            "aux isothermes de basse pression, donne Qst a recouvrement nul."),
            state="readonly", values=QST_METHODS)
        self.cb_method.set(QST_METHODS[2])
        self.cb_model = field(
            g, _("Modele :"), TCombobox, 30, 3, 0,
            _("Modele utilise pour Clausius-Clapeyron. Le meme "
            "modele a toutes les temperatures est le choix le plus coherent."),
            state="readonly")
        self.cb_model.bind("<<ComboboxSelected>>", lambda e: self._fill_list())

        lf = ttk.Frame(g, style="Card.TFrame")
        lf.grid(row=4, column=0, columnspan=2, sticky="we", pady=(8, 0))
        self.lb = tk.Listbox(lf, selectmode="extended", height=6,
                             exportselection=False, font=("Consolas", 9),
                             relief="flat", borderwidth=1,
                             highlightthickness=1, activestyle="none")
        vs = ttk.Scrollbar(lf, orient="vertical", command=self.lb.yview)
        self.lb.configure(yscrollcommand=vs.set)
        self.lb.pack(side="left", fill="x", expand=True)
        vs.pack(side="right", fill="y")
        self.lb.bind("<<ListboxSelect>>", lambda e: self._sel_changed())
        bs = ttk.Frame(g, style="Card.TFrame")
        bs.grid(row=5, column=0, columnspan=2, sticky="w", pady=(4, 0))
        ttk.Button(bs, text=_("Tout selectionner"), style="Ghost.TButton",
                   command=lambda: (self.lb.select_set(0, "end"),
                                    self._sel_changed())).pack(side="left")
        ttk.Button(bs, text=_("Aucun"), style="Ghost.TButton",
                   command=lambda: (self.lb.select_clear(0, "end"),
                                    self._sel_changed())).pack(side="left",
                                                               padx=6)
        self.lbl_sel = wrap_to_width(ttk.Label(g, text="", style="Muted.TLabel",
                                               justify="left"))
        self.lbl_sel.grid(row=6, column=0, columnspan=2, sticky="we")
        g.columnconfigure(1, weight=1)

        cfg = card(lwrap.inner, _("2. Options de calcul"))
        cfg.pack(fill="x")
        g2 = cfg.body
        self.cb_basis = field(g2, _("Base :"), TCombobox, 24, 0, 0,
                              _("Fugacite : exacte a haute pression (gaz reel). "
                              "Pression : hypothese du gaz parfait, suffisante "
                              "a basse pression."), state="readonly",
                              values=QST_BASES)
        self.cb_basis.grid(columnspan=3)
        self.cb_basis.set(QST_BASES[0])
        eos = (["CoolProp"] if HAS_COOLPROP else []) + ["Peng-Robinson",
                                                         "Table NIST"]
        self.cb_eos = field(g2, _("Equation d'etat :"), TCombobox, 16, 1, 0,
                            _("Source du coefficient de fugacite (meme choix que "
                            "pour la conversion exces -> total)."),
                            state="readonly", values=eos)
        self.cb_eos.grid(columnspan=3)
        self.cb_eos.set(eos[0])
        self.e_npts = field(g2, _("Points en n :"), ttk.Entry, 7, 2, 0,
                            _("Nombre de quantites adsorbees calculees"))
        self.e_npts.insert(0, "40")
        self.e_pvir = field(g2, _("P max viriel (bar) :"), ttk.Entry, 7, 2, 2,
                            _("Points retenus pour le viriel (vide : tous). "
                            "L'equation du viriel est faite pour les "
                            "isothermes de basse pression."))
        self.e_m = field(g2, _("Degre a (viriel) :"), ttk.Entry, 7, 3, 0,
                         _("Vide : choix automatique par AICc (1 a 6)"))
        self.e_k = field(g2, _("Degre b (viriel) :"), ttk.Entry, 7, 3, 2,
                         _("Vide : choix automatique par AICc (0 a 3)"))

        self.lbl_warn = wrap_to_width(ttk.Label(
            right, text="", style="MutedBg.TLabel", justify="left",
            foreground=UI["warn"]))
        self.lbl_warn.pack(fill="x", pady=(0, 6))
        mid = ttk.PanedWindow(right, orient="vertical")
        mid.pack(fill="both", expand=True)
        pf = ttk.Frame(mid)
        tf = ttk.Frame(mid)
        mid.add(pf, weight=3)
        mid.add(tf, weight=1)

        cg = card(pf)       # sans titre : la ligne "Afficher" en tient lieu
        cg.pack(fill="both", expand=True)
        opt = ttk.Frame(cg.body, style="Card.TFrame")
        opt.pack(fill="x", pady=(0, 6))
        ttk.Label(opt, text=_("Afficher :"), style="Card.TLabel").pack(
            side="left", padx=(0, 6))
        self.var_pq = tk.BooleanVar(value=True)
        self.var_pi = tk.BooleanVar(value=True)
        self.var_pv = tk.BooleanVar(value=False)
        for txt, var, hint in (
                ("Qst(n)", self.var_pq, _("chaleur isosterique en fonction de "
                                        "la quantite adsorbee")),
                (_("isosteres"), self.var_pi, _("ln f contre 1/T a quantite "
                                           "constante : des droites attendues")),
                (_("ajustement du viriel"), self.var_pv,
                 _("points mesures et equation du viriel"))):
            cb = ttk.Checkbutton(opt, text=txt, variable=var,
                                 command=lambda: self.draw())
            cb.pack(side="left", padx=4)
            tip(cb, hint)
        self.fig = Figure(figsize=(4.5, 3.2), dpi=100, facecolor=UI["card"])
        self.canvas = make_canvas(cg.body, self.fig,
                                  (self._render, _("Chaleur isosterique"), app))

        ct = card(tf, _("Resultats"), _("Qst positif ; enthalpie d'adsorption = -Qst"))
        ct.pack(fill="both", expand=True, pady=(8, 0))
        self.lbl_sum = wrap_to_width(ttk.Label(ct.body, text="",
                                               style="Muted.TLabel",
                                               justify="left"))
        self.lbl_sum.pack(side="bottom", fill="x", pady=(6, 0))
        tvf = ttk.Frame(ct.body, style="Card.TFrame")
        self.tv = ttk.Treeview(tvf, show="headings", height=4)
        vs2 = ttk.Scrollbar(tvf, orient="vertical", command=self.tv.yview)
        hs2 = ttk.Scrollbar(ct.body, orient="horizontal", command=self.tv.xview)
        self.tv.configure(yscrollcommand=vs2.set, xscrollcommand=hs2.set)
        hs2.pack(side="bottom", fill="x")
        tvf.pack(fill="both", expand=True)
        self.tv.pack(side="left", fill="both", expand=True)
        vs2.pack(side="right", fill="y")
        set_sash(pan, 0, 450)
        set_sash(mid, 0, 0.58)

    # ------------------------------------------------------------- listes
    def refresh(self):
        gases = []
        for d in self.app.datasets:
            g = d.get("gas", "")
            if g and g not in gases:
                gases.append(g)
        cur = self.cb_gas.get()
        self.cb_gas["values"] = gases
        if cur not in gases:
            # par defaut : le gaz qui a le plus de temperatures differentes
            best, nb = (gases[0] if gases else ""), 0
            for g in gases:
                k = len({round(float(d["T"]), 1) for d in self.app.datasets
                         if d.get("gas") == g})
                if k > nb:
                    best, nb = g, k
            self.cb_gas.set(best)
        self._fill_models()
        self._fill_list()

    def _fill_models(self):
        keys = []
        for f in self.app.fits:
            if f.get("gas") == self.cb_gas.get() and f["model_key"] not in keys:
                keys.append(f["model_key"])
        vals = [QST_BEST] + [MODELS[k].label for k in MODEL_ORDER if k in keys]
        cur = self.cb_model.get()
        self.cb_model["values"] = vals
        self.cb_model.set(cur if cur in vals else vals[0])

    def _model_key(self):
        lab = self.cb_model.get()
        for k, m in MODELS.items():
            if m.label == lab:
                return k
        return None

    def _fit_for(self, d):
        """Ajustement retenu pour un jeu (modele choisi ou meilleur AICc)."""
        cands = [f for f in self.app.fits if f.get("dataset") == d["name"]]
        key = self._model_key()
        if key:
            cands = [f for f in cands if f["model_key"] == key]
            return cands[-1] if cands else None
        if not cands:
            return None
        return min(cands, key=lambda f: f.get("stats", {}).get("AICc", np.inf)
                   if np.isfinite(f.get("stats", {}).get("AICc", np.inf))
                   else np.inf)

    def _fill_list(self):
        self._fill_models_if_gas_changed()
        gas = self.cb_gas.get()
        prev = {it["name"] for i, it in enumerate(self._items)
                if i in self.lb.curselection()}
        self._items = [d for d in self.app.datasets if d.get("gas") == gas]
        self._items.sort(key=lambda d: (d.get("kind", ""), float(d["T"])))
        self.lb.delete(0, "end")
        for d in self._items:
            f = self._fit_for(d)
            # ligne courte : elle doit tenir dans la colonne de reglages
            self.lb.insert("end", "%-24s %6.2f K  %-5s  %s"
                           % (d["name"][:24], float(d["T"]), _(d.get("kind", "")),
                              (MODELS[f["model_key"]].label.split(" (")[0] if f
                               else _("pas d'ajustement"))))
        # selection : la precedente, sinon les jeux "Total" s'il y en a
        idx = [i for i, d in enumerate(self._items) if d["name"] in prev]
        if not idx:
            kinds = {d.get("kind") for d in self._items}
            want = "Total" if "Total" in kinds else None
            idx = [i for i, d in enumerate(self._items)
                   if want is None or d.get("kind") == want]
        for i in idx:
            self.lb.select_set(i)
        self._sel_changed()

    def _fill_models_if_gas_changed(self):
        g = self.cb_gas.get()
        if getattr(self, "_gas_models", None) != g:
            self._gas_models = g
            self._fill_models()

    def _selected(self):
        return [self._items[i] for i in self.lb.curselection()
                if i < len(self._items)]

    def _sel_changed(self):
        sel = self._selected()
        Ts = sorted({round(float(d["T"]), 2) for d in sel})
        self.lbl_sel.config(text=_("%d isotherme(s), %d temperature(s) : %s K")
                            % (len(sel), len(Ts),
                               ", ".join(fmt(t, 1) for t in Ts) or "-"))

    # ------------------------------------------------------------- calcul
    def run(self):
        sel = self._selected()
        gas = self.cb_gas.get()
        method = self.cb_method.get()
        do_cc = method in (QST_METHODS[0], QST_METHODS[2])
        do_vir = method in (QST_METHODS[1], QST_METHODS[2])
        basis = self.cb_basis.get()
        eos = self.cb_eos.get()
        if len({round(float(d["T"]), 2) for d in sel}) < 2:
            messagebox.showwarning(
                _("Chaleur isosterique"), _("Selectionnez des isothermes du meme "
                "gaz a au moins deux temperatures differentes."), parent=self)
            return
        warns = []
        Ts = [float(d["T"]) for d in sel]
        if len(set(round(t, 2) for t in Ts)) < len(Ts):
            warns.append(_("Plusieurs isothermes a la meme temperature : "
                         "verifiez qu'elles decrivent bien le meme materiau."))
        if max(Ts) - min(Ts) < 10.0:
            warns.append(_("Ecart de temperature inferieur a 10 K : Qst sera "
                         "tres sensible au bruit de mesure."))
        kinds = {d.get("kind") for d in sel}
        if len(kinds) > 1:
            warns.append(_("Melange d'isothermes en exces et totales : "
                         "selectionnez un seul type."))
        pmax_all = max(float(np.nanmax(d["P"])) for d in sel)
        if "Exces" in kinds and pmax_all > 10.0:
            warns.append(_("Isothermes en exces jusqu'a %s bar : a haute "
                         "pression, utilisez les quantites totales "
                         "(onglet Conversion).") % fmt(pmax_all, 3))
        if (basis == QST_BASES[0] and eos == "Table NIST"
                and not all(nist_available(gas, t) for t in Ts)):
            warns.append(_("La table NIST ne couvre pas toutes les "
                         "temperatures : les autres passent par Peng-Robinson. "
                         "Preferez une seule source (CoolProp ou "
                         "Peng-Robinson)."))
        sat = []
        for d in sel:
            psat, above, _src = saturation_check(d["gas"], d["T"], d["P"])
            if above.any():
                sat.append(_("%s (%d point(s) > Psat = %.2f bar)")
                           % (d["name"], int(above.sum()), psat))
        if sat:
            warns.append(_("Points au-dessus de la pression de vapeur saturante "
                         "(fluide liquide) : %s. Retirez-les puis refaites "
                         "l'ajustement : ils faussent les isosteres.")
                         % ", ".join(sat))
        npts = max(5, int(to_float_or(self.e_npts.get(), 40)))
        df_cc, entries, tables, missing = None, [], [], []
        try:
            if do_cc:
                for d in sel:
                    f = self._fit_for(d)
                    if f is None:
                        missing.append(d["name"])
                        continue
                    qd = np.asarray(f.get("q") or d["q"], float)
                    # temperature actuelle du jeu, pas celle notee lors de
                    # l'ajustement : elle a pu etre corrigee depuis
                    entries.append(dict(
                        name=d["name"], T=float(d["T"]),
                        model_key=f["model_key"], params=list(f["params"]),
                        ctx=dict(f["ctx"]),
                        P_min=float(f.get("P_exp_min", np.nanmin(d["P"]))),
                        P_max=float(f.get("P_exp_max", np.nanmax(d["P"]))),
                        q_min=float(np.nanmin(qd)), q_max=float(np.nanmax(qd))))
                if missing:
                    warns.append(_("Sans ajustement (ignores par Clausius-"
                                 "Clapeyron) : %s.") % ", ".join(missing))
                if len({round(e["T"], 2) for e in entries}) < 2:
                    raise ValueError(_("Clausius-Clapeyron demande des isothermes "
                                     "ajustees a au moins deux temperatures "
                                     "(onglet Ajustement)."))
                entries.sort(key=lambda e: e["T"])
                lo, hi = qst_common_range(entries)
                if not hi > lo:
                    raise ValueError(_("Les isothermes n'ont aucune quantite "
                                     "adsorbee en commun : impossible de "
                                     "construire des isosteres."))
                n_vals = np.linspace(lo, hi, npts)
                tables = qst_tables(entries, gas, basis, eos)
                df_cc = qst_clausius_clapeyron(entries, n_vals, gas, basis,
                                               eos, tables=tables)
                if len({round(e["T"], 2) for e in entries}) == 2:
                    warns.append(_("Deux temperatures seulement : Qst sans "
                                 "incertitude (au moins trois conseillees)."))
            vf = None
            if do_vir:
                pv = to_float_or(self.e_pvir.get(), np.nan)
                pts = []
                for d in sel:
                    P = np.asarray(d["P"], float)
                    q = np.asarray(d["q"], float)
                    if np.isfinite(pv) and pv > 0:
                        keep = P <= pv
                        P, q = P[keep], q[keep]
                    pts.append((float(d["T"]), P, q))
                m = self.e_m.get().strip()
                k = self.e_k.get().strip()
                vf = virial_fit(pts, m=int(float(m)) if m else None,
                                k=int(float(k)) if k else None, gas=gas,
                                basis=basis, eos=eos)
                pmax_v = max(float(np.max(p[1])) for p in pts if len(p[1]))
                if pmax_v > 5.0:
                    warns.append(_("Viriel ajuste jusqu'a %s bar : l'equation "
                                 "du viriel est faite pour les basses "
                                 "pressions ; limitez 'P max viriel'.")
                                 % fmt(pmax_v, 3))
        except Exception as e:
            messagebox.showerror(_("Chaleur isosterique"), str(e), parent=self)
            return

        # tableau commun
        if df_cc is not None:
            df = df_cc.copy()
        else:
            n_vals = np.linspace(0.0, vf["n_max_common"], npts)
            df = pd.DataFrame({"n (mmol/g)": n_vals})
        if vf is not None:
            Qv, uv = virial_qst(vf, df["n (mmol/g)"].values)
            outside = df["n (mmol/g)"].values > vf["n_max"] * 1.0001
            df["Qst viriel (kJ/mol)"] = np.where(outside, np.nan, Qv)
            df["u(Qst viriel) (kJ/mol)"] = np.where(outside, np.nan, uv)
        self.df, self.vf = df, vf
        self.entries, self.tables = entries, tables
        pv = to_float_or(self.e_pvir.get(), np.nan)
        self.config_used = dict(gas=gas, method=method, basis=basis, eos=eos,
                                datasets=[d["name"] for d in sel],
                                pvir=(float(pv) if np.isfinite(pv) and pv > 0
                                      else None))
        self.fill_table(df)
        self._summary(df, vf, entries)
        self.lbl_warn.config(text="  |  ".join(warns)[:600])
        for w in warns:
            self.app.log(_("Qst - ") + w)
        self.draw()
        self.app.mark_dirty()

    def _summary(self, df, vf, entries):
        parts = []
        if "Qst CC (kJ/mol)" in df and np.any(np.isfinite(df["Qst CC (kJ/mol)"])):
            q = df["Qst CC (kJ/mol)"].values
            n = df["n (mmol/g)"].values
            parts.append(_("Clausius-Clapeyron (%d isothermes, %s) : Qst de %s a "
                         "%s kJ/mol pour n = %s-%s mmol/g.")
                         % (len(entries), _(self.config_used.get("basis", "")),
                            fmt(np.nanmax(q), 3), fmt(np.nanmin(q), 3),
                            fmt(n[0], 3), fmt(n[-1], 3)))
        if vf is not None:
            parts.append(_("Viriel : degres a=%d, b=%d ; Qst0 = %s +/- %s kJ/mol ; "
                         "R2 = %s sur %d points.")
                         % (vf["m"], vf["k"], fmt(vf["Qst0"], 4),
                            fmt(vf["u_Qst0"], 2), fmt(vf["R2"], 6), vf["N"]))
        txt = "\n".join(parts)
        self.lbl_sum.config(text=txt)
        for p in parts:
            self.app.log(_("Qst - ") + p)

    def fill_table(self, df):
        cols = [c for c in df.columns if not c.startswith("P a ")]
        self.tv["columns"] = cols
        self.tv.delete(*self.tv.get_children())
        for c in cols:
            w = max(80, min(150, 8 * len(c)))
            self.tv.heading(c, text=tr_col(c, True))
            self.tv.column(c, width=w, minwidth=w, anchor="e", stretch=False)
        for _u, row in df.iterrows():
            self.tv.insert("", "end", values=[fmt(row[c], 5) for c in cols])

    # ------------------------------------------------------------- graphes
    def draw(self):
        self._render(self.fig)
        self.canvas.draw_idle()

    def _render(self, fig):
        fig.clear()
        df = self.df
        if df is None:
            return
        panels = [k for k, v in (("q", self.var_pq), ("i", self.var_pi),
                                 ("v", self.var_pv)) if v.get()]
        if "i" in panels and not self.entries:
            panels.remove("i")
        if "v" in panels and self.vf is None:
            panels.remove("v")
        if not panels:
            panels = ["q"]
        axes = panel_axes(fig, len(panels))
        lnlab = ("ln f" if self.config_used.get("basis") == QST_BASES[0]
                 else "ln P")
        for ax, kind in zip(axes, panels):
            if kind == "q":
                n = df["n (mmol/g)"].values
                if "Qst CC (kJ/mol)" in df:
                    q = df["Qst CC (kJ/mol)"].values
                    u = df["u(Qst CC) (kJ/mol)"].values
                    ax.plot(n, q, "-o", ms=3.5, color=PALETTE[0],
                            label=_("Clausius-Clapeyron"))
                    if np.any(np.isfinite(u)):
                        ax.fill_between(n, q - u, q + u, color=PALETTE[0],
                                        alpha=0.15, lw=0)
                if self.vf is not None:
                    nn = np.linspace(0.0, self.vf["n_max_common"], 200)
                    Qv, uv = virial_qst(self.vf, nn)
                    ax.plot(nn, Qv, "-", color=PALETTE[1], lw=1.8,
                            label=_("Viriel"))
                    ax.fill_between(nn, Qv - uv, Qv + uv, color=PALETTE[1],
                                    alpha=0.15, lw=0)
                    ax.plot([0.0], [self.vf["Qst0"]], "D", color=PALETTE[1],
                            ms=6)
                ax.set_xlabel(_("Quantite adsorbee n (mmol/g)"))
                ax.set_ylabel(_("Qst (kJ/mol)"))
                # echelle d'au moins 10 kJ/mol : une chaleur constante doit
                # apparaitre plate, pas comme un bruit numerique agrandi
                y0, y1 = ax.get_ylim()
                if np.isfinite(y0) and np.isfinite(y1) and y1 - y0 < 10.0:
                    ym = 0.5 * (y0 + y1)
                    ax.set_ylim(ym - 5.0, ym + 5.0)
            elif kind == "i":
                lo = float(df["n (mmol/g)"].min())
                hi = float(df["n (mmol/g)"].max())
                for j, n in enumerate(np.linspace(lo, hi, 6)):
                    invT, ys, _P = qst_isostere(self.entries, self.tables, n)
                    if len(invT) < 2:
                        continue
                    X = 1000.0 * np.asarray(invT)
                    Y = np.asarray(ys)
                    col = PALETTE[j % len(PALETTE)]
                    ax.plot(X, Y, "o", color=col, ms=5,
                            label="n = %s" % fmt(n, 3))
                    c = np.polyfit(X, Y, 1)
                    xx = np.linspace(X.min(), X.max(), 10)
                    ax.plot(xx, np.polyval(c, xx), "-", color=col, lw=1)
                ax.set_xlabel("1000 / T (1/K)")
                ax.set_ylabel(_("%s  (f, P en bar)") % lnlab)
            else:
                vf = self.vf
                cfg = self.config_used
                used = set(cfg.get("datasets", []))
                pv = cfg.get("pvir")
                for j, t in enumerate(vf["temps"]):
                    col = PALETTE[j % len(PALETTE)]
                    for d in self.app.datasets:
                        if d["name"] not in used or abs(float(d["T"]) - t) > 1e-6:
                            continue
                        P = np.asarray(d["P"], float)
                        q = np.asarray(d["q"], float)
                        ok = (P > 0) & (q > 0)
                        if pv:
                            ok &= P <= pv
                        if not np.any(ok):
                            continue
                        y = np.log(P[ok])
                        if cfg.get("basis") == QST_BASES[0]:
                            lp, lphi = ln_phi_curve(t, cfg.get("gas", ""),
                                                    cfg.get("eos", "Peng-Robinson"),
                                                    float(P[ok].max()) * 1.01)
                            y = y + np.interp(np.log(P[ok]), lp, lphi)
                        ax.plot(q[ok], y, "o", ms=4, color=col)
                    nn = np.linspace(max(1e-3, 0.02 * vf["n_max"]),
                                     vf["n_max"], 120)
                    ax.plot(nn, np.log(virial_pressure(vf, nn, t)), "-",
                            color=col, lw=1.2, label="%s K" % fmt(t, 1))
                ax.set_xlabel(_("Quantite adsorbee n (mmol/g)"))
                ax.set_ylabel(_("%s (bar)") % lnlab)
            ax.grid(True, ls="--", alpha=0.5)
            wide = ax.get_position().width > 0.6    # panneaux empiles
            if kind == "i":
                # legende au-dessus : elle ne cache aucun point
                ax.legend(fontsize=7.5, ncol=6 if wide else 3,
                          loc="lower center",
                          bbox_to_anchor=(0.5, 1.0), frameon=False,
                          handletextpad=0.3, columnspacing=1.2)
            else:
                ax.legend(fontsize=8, ncol=2 if wide else 1)
        try:
            fig.tight_layout()
        except Exception:
            pass

    # ------------------------------------------------------------- sorties
    def export(self):
        if self.df is None:
            messagebox.showwarning(_("Chaleur isosterique"),
                                   _("Lancez d'abord un calcul."), parent=self)
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".xlsx", filetypes=[("Excel", "*.xlsx")],
            initialfile=_("chaleur_isosterique_%s.xlsx")
                        % self.config_used.get("gas", ""))
        if not path:
            return
        with pd.ExcelWriter(path, engine="openpyxl") as w:
            self.df.to_excel(w, sheet_name="Qst", index=False)
            self.isotherms_frame().to_excel(w, sheet_name=tr_col("Isothermes"),
                                            index=False)
            if self.vf is not None:
                self.virial_frame().to_excel(w, sheet_name=tr_col("Viriel"),
                                             index=False)
        self.app.log(_("Export chaleur isosterique : %s") % path)
        messagebox.showinfo(_("Export"), _("Fichier enregistre :\n%s") % path,
                            parent=self)

    def isotherms_frame(self):
        rows = []
        for e in self.entries:
            m = MODELS[e["model_key"]]
            r = {"Jeu": e["name"], "T (K)": e["T"], "Modele": m.label,
                 "P min (bar)": e["P_min"], "P max (bar)": e["P_max"],
                 "q min (mmol/g)": e["q_min"], "q max (mmol/g)": e["q_max"]}
            for j, pn in enumerate(m.pnames):
                r[pn] = e["params"][j]
            rows.append(r)
        cfg = self.config_used
        rows.append({"Jeu": _("Gaz : %s ; base : %s ; equation d'etat : %s")
                     % (cfg.get("gas"), _(cfg.get("basis")), _(cfg.get("eos")))})
        return pd.DataFrame(rows)

    def virial_frame(self):
        vf = self.vf
        se = np.sqrt(np.maximum(np.diag(np.asarray(vf["cov"])), 0.0))
        rows = []
        for i, v in enumerate(vf["a"]):
            rows.append({"Coefficient": "a%d" % i, "Valeur": v,
                         "Ecart-type": se[i], "Unite": "K (mmol/g)^-%d" % i})
        for j, v in enumerate(vf["b"]):
            rows.append({"Coefficient": "b%d" % j, "Valeur": v,
                         "Ecart-type": se[len(vf["a"]) + j],
                         "Unite": "(mmol/g)^-%d" % j})
        rows.append({"Coefficient": _("Qst0 (kJ/mol)"), "Valeur": vf["Qst0"],
                     "Ecart-type": vf["u_Qst0"]})
        rows.append({"Coefficient": "R2 (ln P)", "Valeur": vf["R2"]})
        rows.append({"Coefficient": "N points", "Valeur": vf["N"]})
        for t, kh in vf["K_H"].items():
            rows.append({"Coefficient": "K_H a %s K" % fmt(t, 1), "Valeur": kh,
                         "Unite": "mmol/g/bar"})
        return pd.DataFrame(rows)

    def send_to_plot(self):
        if self.df is None:
            return
        gas = self.config_used.get("gas", "")
        n = self.df["n (mmol/g)"].values
        if not self.app.series:
            tp = self.app.tab_plot
            tp.v_xlab.set(_("Quantite adsorbee n (mmol/g)"))
            tp.v_ylab.set("Qst (kJ/mol)")
        if "Qst CC (kJ/mol)" in self.df:
            self.app.add_series("Qst CC %s" % gas, n,
                                self.df["Qst CC (kJ/mol)"].values,
                                kind="points+ligne")
        if self.vf is not None:
            nn = np.linspace(0.0, self.vf["n_max_common"], 120)
            self.app.add_series(_("Qst viriel %s") % gas, nn,
                                virial_qst(self.vf, nn)[0], kind="ligne")
        self.app.tab_plot.refresh_series()
        self.app.log(_("Series de chaleur isosterique envoyees vers l'onglet "
                     "Graphiques."))

    # ------------------------------------------------------------- session
    def to_session(self):
        if self.df is None:
            return None
        df = self.df
        return dict(columns=list(df.columns),
                    rows=df.astype(object).where(pd.notnull(df), None
                                                 ).values.tolist(),
                    vf=copy.deepcopy(self.vf),
                    entries=copy.deepcopy(self.entries),
                    config=copy.deepcopy(self.config_used))

    def from_session(self, d):
        self.df = self.vf = None
        self.entries, self.tables = [], []
        if not d or not d.get("columns"):
            self.tv.delete(*self.tv.get_children())
            self.fig.clear()
            self.canvas.draw_idle()
            return
        try:
            self.df = pd.DataFrame(d["rows"], columns=d["columns"]).astype(float)
            self.vf = d.get("vf")
            if self.vf and isinstance(self.vf.get("K_H"), dict):
                self.vf["K_H"] = {float(k): v for k, v in
                                  self.vf["K_H"].items()}
            self.entries = d.get("entries") or []
            self.config_used = d.get("config") or {}
            self.tables = qst_tables(self.entries, self.config_used.get("gas", ""),
                                     self.config_used.get("basis", QST_BASES[1]),
                                     self.config_used.get("eos", "Peng-Robinson"))
            self.fill_table(self.df)
            self._summary(self.df, self.vf, self.entries)
            self.draw()
        except Exception:
            self.df = None


# =============================================================================
# 11. ONGLET 6 : GRAPHIQUES PERSONNALISABLES
# =============================================================================

class TabPlot(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master, padding=10)
        self.app = app
        self.annotations = []
        pan = ttk.PanedWindow(self, orient="horizontal")
        pan.pack(fill="both", expand=True)
        left = ScrollFrame(pan)
        right = ttk.Frame(pan)
        pan.add(left, weight=0)
        pan.add(right, weight=1)
        L = left.inner

        cs = card(L, _("Series"), _("clic sur la case pour afficher ou masquer"))
        cs.pack(fill="x", pady=(0, 8))
        self.tv = ttk.Treeview(cs.body, columns=("v", "lab", "typ"),
                               show="headings", height=7, selectmode="browse")
        for c, h, w in (("v", "", 30), ("lab", _("Serie"), 250),
                        ("typ", "Type", 95)):
            self.tv.heading(c, text=tr_col(h, True))
            self.tv.column(c, width=w, anchor="w")
        self.tv.pack(fill="x")
        self.tv.bind("<Button-1>", self._click)
        self.tv.bind("<<TreeviewSelect>>", lambda e: self.load_style())
        bs = ttk.Frame(cs.body, style="Card.TFrame")
        bs.pack(fill="x", pady=(8, 0))
        b = ttk.Button(bs, text=_("Ajouter") + " ▾", style="Primary.TButton",
                       width=0)
        b.config(command=lambda b=b: popup_menu(b, [
            (_("Tous les jeux de donnees (points)"), self.add_datasets),
            (_("Jeu et courbes affiches dans l'onglet Ajustement"),
             app.tab_fit.send_to_plot),
            (_("Dernier calcul IAST"), app.tab_iast.send_to_plot),
            (_("Chaleur isosterique"), app.tab_qst.send_to_plot)]))
        tip(b, _("Ajoute des series sans quitter l'onglet. Le bouton 'Vers "
                 "Graphiques' des autres onglets fait la meme chose.")
            ).pack(side="left", padx=2)
        for txt, cmd, sty in ((_("Monter"), lambda: self.move(-1), ""),
                              (_("Descendre"), lambda: self.move(1), ""),
                              (_("Supprimer"), self.del_series, ""),
                              (_("Tout vider"), self.clear_series, "Danger.TButton")):
            kw = {"style": sty} if sty else {}
            ttk.Button(bs, text=txt, command=cmd, width=0, **kw).pack(
                side="left", padx=2)

        st_ = card(L, _("Style de la serie selectionnee"))
        st_.pack(fill="x", pady=(0, 8))
        st = st_.body
        st.columnconfigure(1, weight=1)
        self.e_lab = field(st, _("Legende :"), ttk.Entry, 34, 0, 0,
                           _("Texte affiche dans la legende"))
        rowc = ttk.Frame(st, style="Card.TFrame")
        ttk.Label(st, text=_("Type / couleur :"), style="Card.TLabel").grid(
            row=1, column=0, sticky="w", pady=3)
        rowc.grid(row=1, column=1, sticky="w")
        self.cb_kind = TCombobox(rowc, width=15, state="readonly",
                                    values=["points", "ligne", "points+ligne"])
        self.cb_kind.pack(side="left")
        self.btn_col = tk.Button(rowc, text="      ", bg="#1f77b4",
                                 relief="flat", bd=0, command=self.pick_color)
        self.btn_col.pack(side="left", padx=6)
        tip(self.btn_col, _("Choisir la couleur de la serie"))
        rowm = ttk.Frame(st, style="Card.TFrame")
        ttk.Label(st, text=_("Marqueur / ligne :"), style="Card.TLabel").grid(
            row=2, column=0, sticky="w", pady=3)
        rowm.grid(row=2, column=1, sticky="w")
        self.cb_mk = TCombobox(rowm, width=8, state="readonly",
                                  values=MARKERS)
        self.cb_mk.pack(side="left")
        self.cb_ls = TCombobox(rowm, width=8, state="readonly",
                                  values=LINESTYLES)
        self.cb_ls.pack(side="left", padx=6)
        rowe = ttk.Frame(st, style="Card.TFrame")
        ttk.Label(st, text=_("Trait / point / opacite :"),
                  style="Card.TLabel").grid(row=3, column=0, sticky="w", pady=3)
        rowe.grid(row=3, column=1, sticky="w")
        self.e_lw = ttk.Entry(rowe, width=7)
        self.e_lw.pack(side="left")
        tip(self.e_lw, _("Epaisseur du trait"))
        self.e_ms = ttk.Entry(rowe, width=7)
        self.e_ms.pack(side="left", padx=6)
        tip(self.e_ms, _("Taille des marqueurs"))
        self.e_al = ttk.Entry(rowe, width=7)
        self.e_al.pack(side="left")
        tip(self.e_al, _("Opacite entre 0 et 1"))
        self.var_y2 = tk.BooleanVar(value=False)
        ttk.Checkbutton(st, text=_("Tracer sur l'axe Y secondaire"),
                        variable=self.var_y2).grid(row=4, column=0,
                                                   columnspan=2, sticky="w",
                                                   pady=3)
        ttk.Button(st, text=_("Appliquer le style"), style="Primary.TButton",
                   command=self.apply_style).grid(row=5, column=0, columnspan=2,
                                                  sticky="ew", pady=(8, 0))

        ca = card(L, _("Axes et mise en forme"))
        ca.pack(fill="x", pady=(0, 8))
        ax = ca.body
        self.v_title = tk.StringVar(value="")
        self.v_xlab = tk.StringVar(value=_("Pression (bar)"))
        self.v_ylab = tk.StringVar(value=_("Quantite adsorbee (mmol/g)"))
        self.v_y2lab = tk.StringVar(value=_("Selectivite"))
        for i, (lab, var) in enumerate(((_("Titre :"), self.v_title),
                                        (_("Axe X :"), self.v_xlab),
                                        (_("Axe Y :"), self.v_ylab),
                                        (_("Axe Y2 :"), self.v_y2lab))):
            ttk.Label(ax, text=lab, style="Card.TLabel").grid(row=i, column=0,
                                                              sticky="w", pady=2)
            ttk.Entry(ax, textvariable=var, width=32).grid(row=i, column=1,
                                                           columnspan=3,
                                                           sticky="ew", padx=6)
        self.v_xmin = tk.StringVar()
        self.v_xmax = tk.StringVar()
        self.v_ymin = tk.StringVar()
        self.v_ymax = tk.StringVar()
        ttk.Label(ax, text=_("X min / max :"), style="Card.TLabel").grid(
            row=4, column=0, sticky="w", pady=2)
        ttk.Entry(ax, textvariable=self.v_xmin, width=11).grid(row=4, column=1,
                                                               sticky="w", padx=6)
        ttk.Entry(ax, textvariable=self.v_xmax, width=11).grid(row=4, column=2,
                                                               sticky="w")
        ttk.Label(ax, text=_("Y min / max :"), style="Card.TLabel").grid(
            row=5, column=0, sticky="w", pady=2)
        ttk.Entry(ax, textvariable=self.v_ymin, width=11).grid(row=5, column=1,
                                                               sticky="w", padx=6)
        ttk.Entry(ax, textvariable=self.v_ymax, width=11).grid(row=5, column=2,
                                                               sticky="w")
        self.v_logx = tk.BooleanVar(value=False)
        self.v_logy = tk.BooleanVar(value=False)
        self.v_grid = tk.BooleanVar(value=True)
        self.v_leg = tk.BooleanVar(value=True)
        box = ttk.Frame(ax, style="Card.TFrame")
        box.grid(row=6, column=0, columnspan=4, sticky="w", pady=3)
        for txt, var in ((_("Log X"), self.v_logx), (_("Log Y"), self.v_logy),
                         (_("Grille"), self.v_grid), (_("Legende"), self.v_leg)):
            ttk.Checkbutton(box, text=txt, variable=var).pack(side="left",
                                                              padx=(0, 12))
        self.cb_loc = field(ax, _("Position legende :"), TCombobox, 14, 7, 0,
                            None, values=LEGEND_LOCS, state="readonly")
        self.cb_loc.set("best")
        self.v_fs = tk.StringVar(value="11")
        self.v_w = tk.StringVar(value="8.0")
        self.v_h = tk.StringVar(value="6.0")
        self.v_dpi = tk.StringVar(value="300")
        ttk.Label(ax, text=_("Police :"), style="Card.TLabel").grid(row=8, column=0,
                                                                 sticky="w",
                                                                 pady=2)
        ttk.Entry(ax, textvariable=self.v_fs, width=7).grid(row=8, column=1,
                                                            sticky="w", padx=6)
        ttk.Label(ax, text=_("Export : largeur x hauteur (pouces) :"),
                  style="Card.TLabel").grid(row=9, column=0, sticky="w", pady=2)
        ttk.Entry(ax, textvariable=self.v_w, width=7).grid(row=9, column=1,
                                                           sticky="w", padx=6)
        ttk.Entry(ax, textvariable=self.v_h, width=7).grid(row=9, column=2,
                                                           sticky="w")
        ttk.Label(ax, text=_("DPI export :"), style="Card.TLabel").grid(
            row=10, column=0, sticky="w", pady=2)
        ttk.Entry(ax, textvariable=self.v_dpi, width=7).grid(row=10, column=1,
                                                             sticky="w", padx=6)

        an = card(L, _("Annotations"),
                  _("x et y vides : placement automatique en bas a droite"))
        an.pack(fill="x", pady=(0, 8))
        self.tbl_ann = EditableTable(an.body, [_("Texte"), "x", "y", _("Taille")],
                                     height=4, widths=[150, 70, 70, 60])
        self.tbl_ann.pack(fill="x")
        ab = ttk.Frame(an.body, style="Card.TFrame")
        ab.pack(fill="x", pady=(6, 0))
        ttk.Button(ab, text=_("+ Annotation"), width=14,
                   command=lambda: self.tbl_ann.add_row([_("Texte"), "", "", "10"])
                   ).pack(side="left", padx=2)
        ttk.Button(ab, text=_("- Annotation"), width=14,
                   command=self.tbl_ann.delete_selected).pack(side="left", padx=2)

        bt = ttk.Frame(L, style="Card.TFrame", padding=12)
        bt.pack(fill="x")
        tip(ttk.Button(bt, text=_("Actualiser le graphique"),
                       style="Primary.TButton", command=self.draw),
            _("Applique tous les reglages ci-dessus (F5)")).pack(fill="x")
        tip(ttk.Button(bt, text=_("Exporter l'image..."), style="Success.TButton",
                       command=self.export_image),
            _("PNG, PDF, SVG, EPS, TIFF ou JPEG a la resolution choisie")).pack(
            fill="x", pady=6)
        ttk.Button(bt, text=_("Exporter les donnees tracees..."),
                   command=self.export_data).pack(fill="x")

        cf = card(right, _("Figure"),
                  _("molette et barre d'outils pour zoomer  -  bouton Agrandir "
                  "pour une fenetre dediee"))
        cf.pack(fill="both", expand=True)
        self.fig = Figure(figsize=(4.5, 3.2), dpi=100, facecolor=UI["card"])
        self.ax = self.fig.add_subplot(111)
        self.ax2 = None
        self.canvas = make_canvas(cf.body, self.fig,
                                  (self._plot_on, _("Graphique"), app))
        set_sash(pan, 0, 470)
        self.draw()

    def add_datasets(self):
        for d in self.app.datasets:
            self.app.add_series(d["name"], np.asarray(d["P"]),
                                np.asarray(d["q"]), kind="points")
        self.refresh_series()

    def refresh_series(self):
        sel = self.tv.selection()
        self.tv.delete(*self.tv.get_children())
        for i, s in enumerate(self.app.series):
            self.tv.insert("", "end", iid=str(i),
                           values=("X" if s["visible"] else "", s["label"],
                                   _(s["kind"])))
        if sel and sel[0] in self.tv.get_children():
            self.tv.selection_set(sel[0])
        self.draw()
        try:
            self.app.mark_dirty()
        except Exception:
            pass

    def _click(self, event):
        if self.tv.identify_region(event.x, event.y) != "cell":
            return
        if self.tv.identify_column(event.x) != "#1":
            return
        iid = self.tv.identify_row(event.y)
        if not iid:
            return
        s = self.app.series[int(iid)]
        s["visible"] = not s["visible"]
        self.tv.set(iid, "v", "X" if s["visible"] else "")
        self.draw()
        return "break"

    def _sel(self):
        sel = self.tv.selection()
        return int(sel[0]) if sel else None

    def load_style(self):
        i = self._sel()
        if i is None:
            return
        s = self.app.series[i]
        self.e_lab.delete(0, "end")
        self.e_lab.insert(0, s["label"])
        self.cb_kind.set(s["kind"])
        self.btn_col.config(bg=s["color"])
        self.cb_mk.set(s["marker"])
        self.cb_ls.set(s["ls"])
        for e, v in ((self.e_lw, s["lw"]), (self.e_ms, s["ms"]),
                     (self.e_al, s["alpha"])):
            e.delete(0, "end")
            e.insert(0, str(v))
        self.var_y2.set(s.get("y2", False))

    def pick_color(self):
        c = colorchooser.askcolor(color=self.btn_col.cget("bg"), parent=self)
        if c and c[1]:
            self.btn_col.config(bg=c[1])

    def apply_style(self):
        i = self._sel()
        if i is None:
            return
        s = self.app.series[i]
        s["label"] = self.e_lab.get()
        s["kind"] = self.cb_kind.get()
        s["color"] = self.btn_col.cget("bg")
        s["marker"] = self.cb_mk.get()
        s["ls"] = self.cb_ls.get()
        s["lw"] = to_float_or(self.e_lw.get(), 1.5)
        s["ms"] = to_float_or(self.e_ms.get(), 6.0)
        s["alpha"] = min(max(to_float_or(self.e_al.get(), 1.0), 0.05), 1.0)
        s["y2"] = bool(self.var_y2.get())
        self.refresh_series()

    def del_series(self):
        i = self._sel()
        if i is None:
            return
        self.app.series.pop(i)
        self.refresh_series()

    def clear_series(self):
        self.app.series = []
        self.refresh_series()

    def move(self, d):
        i = self._sel()
        if i is None:
            return
        j = i + d
        if 0 <= j < len(self.app.series):
            self.app.series[i], self.app.series[j] = (self.app.series[j],
                                                      self.app.series[i])
            self.refresh_series()
            self.tv.selection_set(str(j))

    # ------------------------------------------------------------------
    def _style_axes(self, ax, ax2):
        fs = to_float_or(self.v_fs.get(), 11)
        ax.set_xlabel(self.v_xlab.get(), fontsize=fs)
        ax.set_ylabel(self.v_ylab.get(), fontsize=fs)
        if self.v_title.get():
            ax.set_title(self.v_title.get(), fontsize=fs + 1)
        ax.tick_params(labelsize=fs - 1)
        if self.v_logx.get():
            ax.set_xscale("log")
        if self.v_logy.get():
            ax.set_yscale("log")
        lims = [to_float(v.get()) for v in (self.v_xmin, self.v_xmax,
                                            self.v_ymin, self.v_ymax)]
        if np.isfinite(lims[0]) or np.isfinite(lims[1]):
            cur = ax.get_xlim()
            ax.set_xlim(lims[0] if np.isfinite(lims[0]) else cur[0],
                        lims[1] if np.isfinite(lims[1]) else cur[1])
        if np.isfinite(lims[2]) or np.isfinite(lims[3]):
            cur = ax.get_ylim()
            ax.set_ylim(lims[2] if np.isfinite(lims[2]) else cur[0],
                        lims[3] if np.isfinite(lims[3]) else cur[1])
        ax.grid(self.v_grid.get(), ls="--", alpha=0.5)
        if ax2 is not None:
            ax2.set_ylabel(self.v_y2lab.get(), fontsize=fs)
            ax2.tick_params(labelsize=fs - 1)
        if self.v_leg.get():
            h, l = ax.get_legend_handles_labels()
            if ax2 is not None:
                h2, l2 = ax2.get_legend_handles_labels()
                h, l = h + h2, l + l2
            if h:
                ax.legend(h, l, loc=(self.cb_loc.get() or "best"),
                          fontsize=max(fs - 2, 1))
        for row in self.tbl_ann.get_rows():
            txt = row[0].strip()
            if not txt:
                continue
            x, y = to_float(row[1]), to_float(row[2])
            sz = to_float_or(row[3], 10)
            if np.isfinite(x) and np.isfinite(y):
                ax.text(x, y, txt, fontsize=sz,
                        bbox=dict(boxstyle="round", fc="#FFFACD", alpha=0.7))
            else:
                ax.text(0.97, 0.05, txt, transform=ax.transAxes, fontsize=sz,
                        ha="right", va="bottom", multialignment="left",
                        bbox=dict(boxstyle="round", fc="#FFFACD", alpha=0.7))

    def _plot_on(self, fig):
        fig.clear()
        ax = fig.add_subplot(111)
        ax2 = None
        if not self.app.series:
            ax.axis("off")
            ax.text(0.5, 0.5, _("Aucune serie a tracer.\n\nBouton 'Ajouter' a "
                    "gauche, ou 'Vers Graphiques' dans les\nonglets Ajustement, "
                    "IAST et Chaleur isosterique."),
                    ha="center", va="center", color=UI["muted"])
            return ax, ax2
        if any(s.get("y2") and s["visible"] for s in self.app.series):
            ax2 = ax.twinx()
        for s in self.app.series:
            if not s["visible"]:
                continue
            tgt = ax2 if s.get("y2") else ax
            mk = s["marker"] if s["kind"] in ("points", "points+ligne") else "None"
            ls = s["ls"] if s["kind"] in ("ligne", "points+ligne") else "None"
            tgt.plot(s["x"], s["y"], marker=(None if mk == "None" else mk),
                     linestyle=("None" if ls == "None" else ls),
                     color=s["color"], lw=s["lw"], ms=s["ms"],
                     alpha=s["alpha"], label=s["label"])
        self._style_axes(ax, ax2)
        try:
            fig.tight_layout()
        except Exception:
            pass
        return ax, ax2

    def _figsize(self):
        w = min(max(to_float_or(self.v_w.get(), 8.0), 2.0), 40.0)
        h = min(max(to_float_or(self.v_h.get(), 6.0), 2.0), 40.0)
        return (w, h)

    def draw(self):
        # La taille en pouces ne s'applique qu'a l'export : imposer une taille
        # a la figure affichee entre en conflit avec le gestionnaire de
        # placement Tk et corrompt le rendu.
        self._plot_on(self.fig)
        self.canvas.draw_idle()

    def export_image(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".png", initialfile=_("figure.png"),
            filetypes=[("PNG", "*.png"), (_("PDF vectoriel"), "*.pdf"),
                       (_("SVG vectoriel"), "*.svg"), ("EPS", "*.eps"),
                       ("TIFF", "*.tif"), ("JPEG", "*.jpg")])
        if not path:
            return
        dpi = to_float_or(self.v_dpi.get(), 300)
        fig = Figure(figsize=self._figsize(), dpi=dpi)
        self._plot_on(fig)
        try:
            fig.savefig(path, dpi=dpi, bbox_inches="tight",
                        facecolor="white")
        except Exception as e:
            messagebox.showerror(_("Export"), str(e), parent=self)
            return
        self.app.log(_("Figure exportee : %s") % path)
        messagebox.showinfo(_("Export"), _("Figure enregistree :\n%s") % path,
                            parent=self)

    def export_data(self):
        vis = [s for s in self.app.series if s["visible"]]
        if not vis:
            messagebox.showwarning(_("Export"), _("Aucune serie affichee."), parent=self)
            return
        path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                            initialfile=_("donnees_graphique.xlsx"),
                                            filetypes=[("Excel", "*.xlsx"),
                                                       ("CSV", "*.csv")])
        if not path:
            return
        n = max(len(s["x"]) for s in vis)
        data = {}
        for s in vis:
            x = list(s["x"]) + [np.nan] * (n - len(s["x"]))
            y = list(s["y"]) + [np.nan] * (n - len(s["y"]))
            data["%s | x" % s["label"]] = x
            data["%s | y" % s["label"]] = y
        df = pd.DataFrame(data)
        if path.lower().endswith(".csv"):
            df.to_csv(path, index=False)
        else:
            df.to_excel(path, index=False, sheet_name=tr_col("Graphique"))
        self.app.log(_("Donnees du graphique exportees : %s") % path)
        messagebox.showinfo(_("Export"), _("Fichier enregistre :\n%s") % path,
                            parent=self)


# =============================================================================
# 12. EXPORTS GLOBAUX ET PROJET
# =============================================================================

def fits_summary_frame(app):
    rows = []
    for f in app.fits:
        m = MODELS[f["model_key"]]
        d = {"Jeu de donnees": f["dataset"], "Modele": m.label,
             "Equation": m.formula, "Ponderation": _(f.get("weights", ""))}
        for j, pn in enumerate(m.pnames):
            d["%s (%s)" % (pn, m.punits[j])] = f["params"][j]
            d["sigma(%s)" % pn] = f["errors"][j]
            if f.get("ci_lo"):
                d["%s IC 2.5%%" % pn] = f["ci_lo"][j]
                d["%s IC 97.5%%" % pn] = f["ci_hi"][j]
        for k, (v, u) in m.derived(f["params"], f["ctx"]).items():
            d["%s [%s]" % (_(k), u)] = v
        d["T (K)"] = f["ctx"].get("T")
        d["P0 (bar)"] = f["ctx"].get("P0")
        d["|r| max (correlation)"] = f.get("r_max", np.nan)
        d["Departs"] = f.get("n_starts", 1)
        d["Tirages bootstrap"] = f.get("n_boot", 0)
        d["P exp. max (bar)"] = f.get("P_exp_max", np.nan)
        d.update({("R2" if k == "R2" else k): v for k, v in f["stats"].items()})
        rows.append(d)
    return pd.DataFrame(rows)


def export_fits_excel(app, path):
    with pd.ExcelWriter(path, engine="openpyxl") as w:
        fits_summary_frame(app).to_excel(w, sheet_name=tr_col("Parametres"), index=False)
        # courbes ajustees
        curves = {}
        for f in app.fits:
            m = MODELS[f["model_key"]]
            P = np.asarray(f["P"], float)
            x = np.linspace(max(1e-6, P.min() * 0.01), P.max() * 1.1, 300)
            y = m.func(x, f["ctx"], *f["params"])
            key = "%s - %s" % (f["dataset"], m.label)
            curves["%s | P (bar)" % key] = x
            curves["%s | q (mmol/g)" % key] = np.asarray(y).ravel()
        if curves:
            pd.DataFrame(curves).to_excel(w, sheet_name=tr_col("Courbes ajustees"),
                                          index=False)
        res = {}
        for f in app.fits:
            m = MODELS[f["model_key"]]
            key = "%s - %s" % (f["dataset"], m.label)
            n = len(f["P"])
            res["%s | P" % key] = f["P"]
            res["%s | q exp" % key] = f["q"]
            res["%s | q calc" % key] = f["qpred"]
            res["%s | residu" % key] = f["residuals"]
        if res:
            n = max(len(v) for v in res.values())
            for k in res:
                res[k] = list(res[k]) + [np.nan] * (n - len(res[k]))
            pd.DataFrame(res).to_excel(w, sheet_name=tr_col("Residus"), index=False)


def export_all_excel(app, path):
    with pd.ExcelWriter(path, engine="openpyxl") as w:
        # 1. donnees brutes
        rows = []
        for d in app.datasets:
            for i in range(len(d["P"])):
                rows.append({"Jeu": d["name"], "Gaz": d["gas"], "T (K)": d["T"],
                             "Type": _(d["kind"]), "P (bar)": d["P"][i],
                             "q (mmol/g)": d["q"][i],
                             "P (%s)" % d["unit_p"]: d["P_raw"][i],
                             "q (%s)" % d["unit_q"]: d["q_raw"][i],
                             "Commentaire": d.get("note", "")})
        pd.DataFrame(rows).to_excel(w, sheet_name=tr_col("Donnees"), index=False)

        # 2. ajustements
        if app.fits:
            fits_summary_frame(app).to_excel(w, sheet_name=tr_col("Ajustements"),
                                             index=False)
            curves = {}
            for f in app.fits:
                m = MODELS[f["model_key"]]
                P = np.asarray(f["P"], float)
                x = np.linspace(max(1e-6, P.min() * 0.01), P.max() * 1.1, 300)
                y = np.asarray(m.func(x, f["ctx"], *f["params"])).ravel()
                key = "%s - %s" % (f["dataset"], m.label)
                curves["%s | P (bar)" % key] = x
                curves["%s | q (mmol/g)" % key] = y
            pd.DataFrame(curves).to_excel(w, sheet_name=tr_col("Courbes ajustees"),
                                          index=False)

        # 3. IAST
        df = getattr(app.tab_iast, "df", None)
        if df is not None:
            df.to_excel(w, sheet_name="IAST", index=False)

        # 3 bis. chaleur isosterique
        tq = getattr(app, "tab_qst", None)
        if tq is not None and tq.df is not None:
            tq.df.to_excel(w, sheet_name="Qst", index=False)
            if tq.entries:
                tq.isotherms_frame().to_excel(w, sheet_name=tr_col("Qst isothermes"),
                                              index=False)
            if tq.vf is not None:
                tq.virial_frame().to_excel(w, sheet_name=tr_col("Qst viriel"),
                                           index=False)

        # 4. series tracees
        vis = [s for s in app.series]
        if vis:
            n = max(len(s["x"]) for s in vis)
            data = {}
            for s in vis:
                data["%s | x" % s["label"]] = (list(s["x"])
                                               + [np.nan] * (n - len(s["x"])))
                data["%s | y" % s["label"]] = (list(s["y"])
                                               + [np.nan] * (n - len(s["y"])))
            pd.DataFrame(data).to_excel(w, sheet_name=tr_col("Graphique"), index=False)

        # 5. informations
        pd.DataFrame([{"Logiciel": "%s v%s" % (APP_NAME, APP_VERSION),
                       "Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                       "Jeux de donnees": len(app.datasets),
                       "Ajustements": len(app.fits)}]
                     ).to_excel(w, sheet_name=tr_col("Informations"), index=False)



def export_origin(app, path, npts=400):
    """Classeur au format attendu par Origin :
       ligne 1 = Long Name, ligne 2 = Units, donnees a partir de la ligne 3.
    Les series sont mises en colonnes cote a cote (format 'large'), ce qui est
    la disposition directement exploitable par Origin (une colonne = une
    courbe), contrairement au format 'long' d'un export classique.
    """
    from openpyxl import Workbook
    from openpyxl.styles import Font, Alignment, PatternFill
    from openpyxl.utils import get_column_letter

    H1 = Font(name="Arial", bold=True, size=10, color="FFFFFF")
    H2 = Font(name="Arial", italic=True, size=9, color="404040")
    BD = Font(name="Arial", size=10)
    FH = PatternFill("solid", fgColor="2F4F6F")
    FU = PatternFill("solid", fgColor="E8EDF2")

    def block(ws, cols, units):
        """cols : liste (nom, sequence). units : liste de chaines."""
        nmax = max((len(v) for _n, v in cols), default=0)
        for j, ((name, vals), un) in enumerate(zip(cols, units), start=1):
            name = tr_col(name)
            c = ws.cell(row=1, column=j, value=name)
            c.font, c.fill = H1, FH
            c.alignment = Alignment(horizontal="center", wrap_text=True)
            u = ws.cell(row=2, column=j, value=un)
            u.font, u.fill = H2, FU
            u.alignment = Alignment(horizontal="center")
            for i in range(nmax):
                v = vals[i] if i < len(vals) else None
                if v is not None:
                    try:
                        v = float(v)
                        if not np.isfinite(v):
                            v = None
                    except Exception:
                        pass
                cc = ws.cell(row=3 + i, column=j, value=v)
                cc.font = BD
                if isinstance(v, float):
                    cc.number_format = "0.######"
            ws.column_dimensions[get_column_letter(j)].width = \
                max(11, min(22, len(name) + 3))
        ws.freeze_panes = "A3"

    wb = Workbook()

    # ---------------------------------------------------- notice
    ws = wb.active
    ws.title = _("LISEZMOI")
    notes = [
        _("%s %s - export Origin") % (APP_NAME, APP_VERSION),
        datetime.datetime.now().strftime(_("genere le %d/%m/%Y a %H:%M")),
        "",
        _("STRUCTURE DES FEUILLES"),
        _("  ligne 1 : Long Name (nom de colonne Origin)"),
        _("  ligne 2 : Units (unite)"),
        _("  ligne 3 et suivantes : donnees"),
        "",
        _("IMPORT DANS ORIGIN"),
        _("  File > Import > Excel...  puis dans les options d'import :"),
        "     Main Header Lines = 0",
        "     Long Names        = 1",
        "     Units             = 2",
        "     Data begins on    = 3",
        _("  Chaque colonne devient une colonne Origin nommee et unitee ;"),
        _("  il ne reste qu'a designer les colonnes X et Y."),
        "",
        "FEUILLES",
        _("  Isothermes      : points experimentaux, un bloc de colonnes par jeu"),
        _("  Courbes_modeles : courbes lissees des ajustements (%d points)") % npts,
        _("  Parametres      : parametres et statistiques de chaque ajustement"),
        _("  IAST            : dernier calcul IAST effectue"),
        _("  Qst             : chaleur isosterique (Clausius-Clapeyron, viriel)"),
        "",
        _("Les colonnes vides en bas d'un bloc sont normales : les jeux n'ont pas"),
        _("tous le meme nombre de points."),
    ]
    for i, t in enumerate(notes, start=1):
        c = ws.cell(row=i, column=1, value=t)
        c.font = Font(name="Arial", size=10,
                      bold=t.isupper() and len(t) > 3)
    ws.column_dimensions["A"].width = 88

    # ---------------------------------------------------- isothermes
    ws = wb.create_sheet(tr_col("Isothermes"))
    cols, units = [], []
    for d in app.datasets:
        tag = d["name"].replace(" ", "_")
        cols.append(("P_%s" % tag, list(np.asarray(d["P"], float))))
        units.append("bar")
        cols.append(("q_%s" % tag, list(np.asarray(d["q"], float))))
        units.append("mmol/g")
    if cols:
        block(ws, cols, units)
    else:
        ws.cell(row=1, column=1, value=_("aucun jeu de donnees"))

    # ---------------------------------------------------- courbes de modeles
    ws = wb.create_sheet(tr_col("Courbes_modeles"))
    cols, units = [], []
    for f in app.fits:
        m = MODELS[f["model_key"]]
        P = np.asarray(f["P"], float)
        if P.size < 2:
            continue
        grid = np.linspace(max(float(np.min(P)), 1e-4), float(np.max(P)), npts)
        try:
            q = np.asarray(m.func(grid, f["ctx"], *f["params"]),
                           dtype=float).ravel()
        except Exception:
            continue
        tag = f["label"].replace(" ", "_").replace("-", "_")
        cols.append(("P_%s" % tag, list(grid)))
        units.append("bar")
        cols.append(("q_%s" % tag, list(q)))
        units.append("mmol/g")
    if cols:
        block(ws, cols, units)
    else:
        ws.cell(row=1, column=1, value=_("aucun ajustement"))

    # ---------------------------------------------------- parametres
    ws = wb.create_sheet(tr_col("Parametres"))
    rows = []
    for f in app.fits:
        m = MODELS[f["model_key"]]
        r = {"Jeu": f["dataset"], "Gaz": f.get("gas", ""), "Modele": m.label}
        for i in range(m.nparam):
            r["p%d_nom" % (i + 1)] = m.pnames[i]
            r["p%d" % (i + 1)] = f["params"][i]
            r["p%d_err" % (i + 1)] = f["errors"][i]
            r["p%d_unite" % (i + 1)] = m.punits[i]
        st = f["stats"]
        r.update({"N": st["N"], "R2": st["R2"], "R2_ajuste": st["R2adj"],
                  "RMSE": st["RMSE"], "AICc": st["AICc"], "BIC": st["BIC"],
                  "T": f["ctx"].get("T"), "P0": f["ctx"].get("P0")})
        rows.append(r)
    if rows:
        keys = []
        for r in rows:
            for k in r:
                if k not in keys:
                    keys.append(k)
        U = {"RMSE": "mmol/g", "T": "K", "P0": "bar"}
        block(ws, [(k, [r.get(k) for r in rows]) for k in keys],
              [U.get(k, "") for k in keys])
    else:
        ws.cell(row=1, column=1, value=_("aucun ajustement"))

    # ---------------------------------------------------- IAST
    ws = wb.create_sheet("IAST")
    df = getattr(app.tab_iast, "df", None)
    if df is not None and len(df):
        # l'unite est celle que porte le nom de la colonne : deviner d'apres
        # l'initiale donnait "bar" a pi* et aux rapports P0/P_exp
        block(ws, [(str(c), list(df[c].values)) for c in df.columns],
              ["".join(re.findall(r"\((bar|mmol/g)\)$", str(c)))
               for c in df.columns])
    else:
        ws.cell(row=1, column=1,
                value=_("aucun calcul IAST - lancez d'abord l'onglet IAST"))

    # ---------------------------------------------------- chaleur isosterique
    ws = wb.create_sheet("Qst")
    tq = getattr(app, "tab_qst", None)
    if tq is not None and tq.df is not None and len(tq.df):
        dq = tq.df

        def unit(c):
            c = str(c)
            if "kJ/mol" in c:
                return "kJ/mol"
            if c.startswith("n "):
                return "mmol/g"
            if c.startswith("P "):
                return "bar"
            return ""
        cols = [(str(c), list(dq[c].values)) for c in dq.columns]
        units = [unit(c) for c in dq.columns]
        if tq.vf is not None:
            nn = np.linspace(0.0, tq.vf["n_max_common"], 200)
            Qv, uv = virial_qst(tq.vf, nn)
            cols += [(_("n viriel"), list(nn)), (_("Qst viriel (courbe)"), list(Qv)),
                     (_("u Qst viriel (courbe)"), list(uv))]
            units += ["mmol/g", "kJ/mol", "kJ/mol"]
        block(ws, cols, units)
    else:
        ws.cell(row=1, column=1, value=_("aucun calcul de chaleur isosterique"))

    wb.save(path)
    return path


def save_project(app, path):
    data = dict(version=APP_VERSION, datasets=app.datasets,
                fits=app.fits,
                series=[{k: (list(map(float, v)) if k in ("x", "y") else v)
                         for k, v in s.items()} for s in app.series])
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=1, ensure_ascii=False, default=float)


def load_project(app, path):
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    app.datasets = data.get("datasets", [])
    app.fits = data.get("fits", [])
    app.series = [{k: (np.asarray(v, float) if k in ("x", "y") else v)
                   for k, v in s.items()} for s in data.get("series", [])]


HELP_TEXT = """\
%s v%s - aide rapide
================================================================================

1) ONGLET DONNEES
   - "Importer des fichiers..." lit un ou plusieurs .xlsx / .xls / .csv. Le
     gaz, la temperature (en K, ex. ZTC850-CO2_303K.xlsx) et l'echantillon
     sont lus dans le nom du fichier ; un tableau recapitulatif permet de les
     corriger avant l'import. Les lignes en jaune sont a verifier.
   - "Importer en choisissant les colonnes..." sert aux fichiers a plusieurs
     feuilles ou plusieurs colonnes : vous choisissez la feuille, les colonnes
     et les unites.
   - "Nouveau jeu vide" cree un jeu vide ; tapez les valeurs ou collez deux
     colonnes depuis Excel avec Ctrl+V.
   - Les unites sont converties en interne en bar et mmol/g.
   - Le jeu est enregistre automatiquement quand vous changez de jeu ou
     d'onglet, lancez un calcul, enregistrez la session ou quittez.
   - Deux jeux ne portent jamais le meme nom : "(2)" est ajoute au besoin.

2) ONGLET CONVERSION  (exces -> total)
   - Volume poreux    : n_tot = n_exc + V_pore x rho_gaz(T,P)
     rho_gaz vient de CoolProp (equations de reference, incluses dans le
     programme Windows), de la table NIST (CO2, CH4, H2 a 303 K) ou de
     Peng-Robinson. V_pore est a saisir : aucune valeur n'est proposee.
   - Densite adsorbee : n_tot = n_exc / (1 - rho_gaz/rho_ads)
   - Densite fournie  : vous saisissez vous-meme rho_gaz (colonne 2 du tableau)
     par exemple depuis NIST REFPROP.
   - "Creer un jeu 'total'" ajoute le resultat comme nouveau jeu, directement
     utilisable pour l'ajustement.
   - Sous la temperature critique, les points au-dessus de la pression de
     vapeur saturante (ex. CO2 a 273 K au-dela de 34,9 bar) sont signales :
     le fluide y est liquide et la conversion n'a plus de sens.
   - "Convertir TOUS les jeux en exces" : si les jeux viennent de plusieurs
     echantillons, un volume poreux est demande pour chacun.

3) ONGLET AJUSTEMENT
   - Modeles : Langmuir, Langmuir bi-site, Freundlich, Sips, Toth,
     Dubinin-Radushkevich et Dubinin-Astakhov (P0 fixe ou ajuste).
   - Le jeu propose au depart est un jeu 'total' s'il en existe un : a haute
     pression, c'est lui qu'il faut ajuster pour l'IAST et la chaleur
     isosterique. "Ajuster TOUS les jeux x TOUS les modeles coches" ne
     reprend pas les jeux en exces deja convertis.
   - P0 peut etre estimee automatiquement : correlation de Lee-Kesler si
     T < Tc, regle de Dubinin Pc(T/Tc)^2 si T > Tc.
   - Les valeurs initiales et les bornes sont modifiables dans le tableau.
   - Ponderation : moindres carres, 1/q ou 1/q^2 (erreur relative).
   - Multi-depart : relance l'ajustement depuis plusieurs points de depart
     aleatoires et conserve le meilleur. Utile pour Toth, Sips et D-A qui
     possedent des minima locaux.
   - Bootstrap : reajuste le modele N fois sur des residus reechantillonnes et
     fournit un intervalle de confiance a 95 %% par parametre. Plus honnete que
     l'ecart-type asymptotique de la matrice de covariance.
   - Colonne |r|max : plus forte correlation entre deux parametres. Au-dela de
     0,99 (ligne rouge), q_max et b se compensent : leurs valeurs individuelles
     ne sont pas identifiables, meme avec un R2 de 0,9999. La capacite
     q_max issue d'un ajustement de Sips ou Toth doit alors etre citee avec
     son intervalle de confiance, pas comme une valeur exacte.
   - Menu "Comparer" : le classement (AIC) compare les modeles en penalisant
     le nombre de parametres (dAIC < 2 : modeles equivalents) ; la matrice met
     tous les jeux et tous les modeles cote a cote.
   - Menu "Exporter" : courbes (P, q) ou classeur Excel complet.
   - "Vers Graphiques" envoie les lignes selectionnees du tableau ou, sans
     selection, le jeu affiche et ses courbes.

4) ONGLET IAST
   - Chaque constituant recoit un modele : un ajustement de l'onglet
     precedent, ou une saisie manuelle des parametres ("Editer...").
   - Au depart, AdsorpSuite propose pour chaque gaz son ajustement sur un jeu
     'total', a la meme temperature pour tous. C'est une proposition a
     verifier : avant le calcul, un avertissement signale un ajustement qui
     appartient a un autre gaz, une isotherme en exces, le meme ajustement
     pour deux constituants ou des temperatures differentes.
   - P max est propose d'apres la gamme mesuree ; au-dela, le calcul repose
     sur l'extrapolation des modeles.
   - La pression d'etalement reduite pi* = integrale de q/P dP est analytique
     pour Langmuir, Langmuir bi-site, Freundlich, Sips, D-R et D-A, et
     numerique pour Toth. Le solveur travaille a une seule inconnue (pi*),
     ce qui est nettement plus robuste qu'un systeme a N equations.
   - Deux modes : balayage en pression totale, ou balayage en composition a
     pression fixee.
   - Sorties : P0_i, x_i, q_i, q_total, selectivites S_i/j, et la quantite
     adsorbee du corps pur a la meme pression partielle (reference).
   - Avertissement : les modeles D-R et D-A ont une constante de Henry nulle ;
     l'IAST y est thermodynamiquement discutable a tres basse pression.
   - CONTROLE D'EXTRAPOLATION : pour calculer un melange a P_totale, l'IAST
     a besoin des isothermes de corps purs jusqu'a P0_i, souvent bien au-dela
     de la pression mesuree (typiquement x5 pour un constituant peu adsorbe
     comme H2 a 60 bar). Les colonnes "P0/P_exp_i" et "Extrapolation max"
     donnent ce rapport ; les lignes concernees sont surlignees (orange
     au-dela de 1, rouge au-dela de 2) et la zone correspondante est grisee
     sur le graphique. Au-dela de 2, le resultat depend surtout du modele
     choisi, pas des mesures.
   - Melanges types (liste deroulante) : CO2/CH4, CO2/N2 15:85, CO2/H2,
     CH4/N2, CH4/H2, C2H2/CO2, C2H2/C2H4 1:99, C2H4/C2H6, C3H6/C3H8,
     Xe/Kr 20:80 et ternaire CO2/CH4/H2.
   - Les resultats de l'IAST concordent avec pyIAST (verification interne).

5) ONGLET CHALEUR ISOSTERIQUE
   - Choisissez un gaz, puis les isothermes d'un meme materiau mesurees a
     plusieurs temperatures (au moins deux, trois ou plus conseillees).
   - Clausius-Clapeyron : pour chaque quantite adsorbee n, la pression a
     chaque temperature est tiree du modele ajuste (onglet Ajustement), puis
     Qst = -R d(ln f)/d(1/T). Seules les quantites mesurees a TOUTES les
     temperatures sont utilisees : aucune extrapolation. Avec trois
     temperatures ou plus, une incertitude-type est donnee pour chaque n.
   - Viriel : ln P = ln n + (1/T) somme a_i n^i + somme b_j n^j, ajuste sur
     tous les points mesures ; Qst(n) = -R somme a_i n^i et Qst0 a
     recouvrement nul. Faite pour les isothermes de basse pression : limitez
     les points avec "P max viriel". Degres choisis par AICc si vides.
   - Base fugacite (par defaut) : exacte a haute pression ; base pression :
     hypothese du gaz parfait. Le coefficient de fugacite vient de
     l'equation d'etat choisie (CoolProp, table NIST ou Peng-Robinson).
   - A haute pression, utilisez des isothermes totales (absolues) plutot
     qu'en exces.
   - Qst est donne positif ; l'enthalpie d'adsorption vaut -Qst.

6) ONGLET GRAPHIQUES
   - Le bouton "Ajouter" place dans le graphique tous les jeux de donnees, le
     jeu et les courbes de l'onglet Ajustement, le dernier calcul IAST ou la
     chaleur isosterique. Le bouton "Vers Graphiques" des autres onglets
     fait la meme chose.
   - Couleur, marqueur, style de ligne, epaisseur, opacite, axe Y secondaire,
     bornes, echelles log, legende, annotations : tout est modifiable.
   - Export PNG / PDF / SVG / EPS / TIFF / JPEG a la resolution choisie, et
     export Excel des donnees effectivement tracees.

7) ONGLET SESSION / EXPORT
   - "Enregistrer la session" ecrit UN SEUL fichier .adsp qui contient tout :
     jeux de donnees, ajustements et leurs statistiques, constituants et
     resultats IAST, chaleur isosterique, series et mise en forme des
     graphiques, annotations. Il suffit de le rouvrir pour retrouver
     l'integralite du travail, y compris sur un autre ordinateur. Le format
     est du JSON lisible ; une session enregistree en francais s'ouvre en
     anglais et inversement.
   - Une copie .adsp.bak de la version precedente est conservee a chaque
     enregistrement, et le programme propose d'enregistrer avant de quitter si
     des modifications sont en cours.
   - "Verification interne" rejoue les controles numeriques du programme
     (modeles, pression d'etalement, IAST, equation d'etat, chaleur
     isosterique) et affiche un rapport. Equivalent en ligne de commande :
     AdsorpSuite.exe --selftest
   - Export Excel global : donnees, ajustements, courbes, IAST, chaleur
     isosterique, graphique.
   - Export Origin : une feuille par resultat, ligne 1 = Long Name,
     ligne 2 = Units.

LANGUE
   - Menu "Langue / Language" : francais ou anglais. Le programme redemarre
     pour appliquer le changement et rouvre la session en cours.

FENETRE ET JOURNAL
   - Le bouton "Journal" (en bas a droite) affiche ou masque l'historique des
     messages ; le dernier message reste visible dans la barre d'etat.
   - La taille de la fenetre est memorisee d'un lancement a l'autre.

GRAPHIQUES ET LISIBILITE
   - Sous chaque graphique, "Agrandir le graphique" l'ouvre dans une fenetre
     separee et redimensionnable, avec zoom, deplacement et export haute
     resolution.
   - Onglet IAST : cases "quantites / selectivites / fractions x / P0" pour
     choisir les panneaux traces, et bouton "Masquer le tableau" pour donner
     toute la hauteur aux courbes.
   - Les separateurs entre panneaux se deplacent a la souris ; les colonnes de
     reglages defilent a la molette.
   - La taille en pouces reglee dans l'onglet Graphiques ne concerne que
     l'export : la figure affichee s'adapte a la fenetre.

RACCOURCIS CLAVIER
   Ctrl+N nouvelle session      Ctrl+O ouvrir       Ctrl+S enregistrer
   Ctrl+Maj+S enregistrer sous  Ctrl+I importer     Ctrl+E export Origin
   Ctrl+1..7 onglets            F1 aide
   F5 lance l'action principale de l'onglet courant
   Maj+F5 traite tous les jeux (onglets Conversion et Ajustement)
   Dans les tableaux : double-clic pour editer, Ctrl+V coller, Suppr effacer

RAPPELS D'UNITES
   P : bar    q : mmol/g    V_pore : cm3/g    rho : mmol/cm3
   E (D-A) : J/mol          K (D-R) : mol2/J2       E = 1/sqrt(K)
   Qst : kJ/mol
""" % (APP_NAME, APP_VERSION)


def models_text():
    lines = [_("MODELES DISPONIBLES"), "=" * 78, ""]
    for k in MODEL_ORDER:
        m = MODELS[k]
        lines.append("%s" % m.label)
        lines.append(_("   Equation   : %s") % m.formula)
        lines.append(_("   Parametres : %s") % ", ".join(
            "%s [%s]" % (p, u) for p, u in zip(m.pnames, m.punits)))
        lines.append(_("   pi* (IAST) : %s")
                     % (_("analytique") if m.pi else _("integration numerique")))
        if m.needs:
            lines.append(_("   Contexte   : %s") % ", ".join(m.needs))
        if m.note:
            lines.append(_("   Remarque   : %s") % m.note)
        lines.append("")
    return "\n".join(lines)


# =============================================================================
# 13. ONGLET 7 : EXPORT ET PROJET
# =============================================================================

class TabExport(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master, padding=10)
        self.app = app
        top = ttk.Frame(self)
        top.pack(fill="x")

        c1 = card(top, _("Session de travail"),
                  _("un seul fichier contient tout : donnees, ajustements, IAST, "
                  "graphiques"))
        c1.pack(side="left", fill="both", expand=True)
        g = c1.body
        tip(ttk.Button(g, text=_("Enregistrer la session..."),
                       style="Primary.TButton", command=self.save),
            _("Ecrit un fichier .adsp contenant l'integralite du travail "
            "(Ctrl+S)")).pack(fill="x", pady=3)
        tip(ttk.Button(g, text=_("Enregistrer sous un nouveau nom..."),
                       command=lambda: self.save(as_new=True)),
            _("Utile pour garder des versions successives")).pack(fill="x", pady=3)
        tip(ttk.Button(g, text=_("Ouvrir une session..."), style="Success.TButton",
                       command=self.open),
            _("Recharge integralement une session enregistree (Ctrl+O)")).pack(
            fill="x", pady=3)
        ttk.Label(g, style="Muted.TLabel", justify="left", wraplength=430,
                  text=_("Le fichier .adsp est du texte JSON : il se copie d'un "
                       "PC a l'autre, se sauvegarde et reste lisible. Une copie "
                       ".adsp.bak de la version precedente est conservee a "
                       "chaque enregistrement.")).pack(anchor="w", pady=(8, 0))

        c2 = card(top, _("Exports"))
        c2.pack(side="left", fill="both", expand=True, padx=(10, 0))
        h = c2.body
        tip(ttk.Button(h, text=_("Export Excel global"), style="Primary.TButton",
                       command=self.export_all),
            _("Donnees, ajustements, courbes, IAST et graphique dans un seul "
            "classeur")).pack(fill="x", pady=3)
        ttk.Button(h, text=_("Ajustements uniquement"),
                   command=self.export_fits).pack(fill="x", pady=3)
        tip(ttk.Button(h, text=_("Export Origin (large, Long Name + Units)"),
                       style="Success.TButton", command=self.export_origin),
            _("Classeur au format attendu par Origin : ligne 1 = Long Name, "
            "ligne 2 = Units, donnees ligne 3. Une colonne par courbe.")).pack(
            fill="x", pady=3)
        ttk.Button(h, text=_("Tous les jeux en CSV"),
                   command=self.export_csv).pack(fill="x", pady=3)
        ttk.Button(h, text=_("Verification interne du programme"),
                   command=self.run_selftest).pack(fill="x", pady=(12, 3))
        ttk.Label(h, style="Muted.TLabel", justify="left", wraplength=430,
                  text=_("La verification interne rejoue les tests numeriques "
                       "(modeles, IAST, equation d'etat) et affiche un rapport.")
                  ).pack(anchor="w")

        c3 = card(self, _("Resume de la session"))
        c3.pack(fill="both", expand=True, pady=(10, 0))
        self.txt = tk.Text(c3.body, font=("Consolas", 9), wrap="none",
                           relief="flat", background="#fbfdff")
        vs = ttk.Scrollbar(c3.body, orient="vertical", command=self.txt.yview)
        self.txt.configure(yscrollcommand=vs.set)
        self.txt.pack(side="left", fill="both", expand=True)
        vs.pack(side="right", fill="y")
        ttk.Button(self, text=_("Actualiser le resume"),
                   command=self.refresh).pack(anchor="w", pady=(8, 0))

    def refresh(self):
        a = self.app
        lines = ["%s v%s   -   %s" % (APP_NAME, APP_VERSION,
                                      datetime.datetime.now().strftime("%d/%m/%Y %H:%M")),
                 "", _("JEUX DE DONNEES (%d)") % len(a.datasets)]
        for d in a.datasets:
            lines.append(_("  - %-28s %-5s %8.2f K  %-6s %3d points  "
                         "P: %s-%s bar   q_max=%s mmol/g")
                         % (d["name"], d["gas"], d["T"], _(d["kind"]), len(d["P"]),
                            fmt(min(d["P"]), 3), fmt(max(d["P"]), 3),
                            fmt(max(d["q"]), 3)))
        lines += ["", _("AJUSTEMENTS (%d)") % len(a.fits)]
        for f in a.fits:
            m = MODELS[f["model_key"]]
            lines.append("  - %-28s %-30s R2=%s  RMSE=%s"
                         % (f["dataset"], m.label, fmt(f["stats"]["R2"], 5),
                            fmt(f["stats"]["RMSE"], 5)))
            lines.append("      %s" % ", ".join(
                "%s = %s +/- %s %s" % (m.pnames[j], fmt(f["params"][j], 5),
                                       fmt(f["errors"][j], 5), m.punits[j])
                for j in range(m.nparam)))
        df = getattr(a.tab_iast, "df", None)
        lines += ["", _("IAST : %s") % (_("aucun calcul") if df is None
                                     else _("%d points, colonnes : %s")
                                     % (len(df), ", ".join(df.columns[:6]) + "..."))]
        lines += ["", _("SERIES GRAPHIQUES (%d)") % len(a.series)]
        for s in a.series:
            lines.append("  - %-40s %s  (%d points)"
                         % (s["label"], s["kind"], len(s["x"])))
        self.txt.delete("1.0", "end")
        self.txt.insert("1.0", "\n".join(lines))

    def export_all(self):
        if not self.app.datasets:
            messagebox.showwarning(_("Export"), _("Aucune donnee."), parent=self)
            return
        path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                            initialfile=_("AdsorpSuite_export.xlsx"),
                                            filetypes=[("Excel", "*.xlsx")])
        if not path:
            return
        try:
            export_all_excel(self.app, path)
        except Exception as e:
            messagebox.showerror(_("Export"), "%s\n%s" % (e, traceback.format_exc()),
                                 parent=self)
            return
        self.app.log(_("Export global : %s") % path)
        messagebox.showinfo(_("Export"), _("Fichier enregistre :\n%s") % path,
                            parent=self)

    def export_fits(self):
        if not self.app.fits:
            messagebox.showwarning(_("Export"), _("Aucun ajustement."), parent=self)
            return
        path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                            initialfile=_("ajustements.xlsx"),
                                            filetypes=[("Excel", "*.xlsx")])
        if path:
            export_fits_excel(self.app, path)
            messagebox.showinfo(_("Export"), _("Fichier enregistre :\n%s") % path,
                                parent=self)

    def export_origin(self):
        if not self.app.datasets and not self.app.fits:
            messagebox.showinfo(_("Export Origin"), _("Rien a exporter."),
                                parent=self)
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".xlsx", title=_("Export Origin"),
            initialfile=_("export_origin.xlsx"),
            filetypes=[(_("Classeur Excel"), "*.xlsx")])
        if not path:
            return
        try:
            export_origin(self.app, path)
        except Exception as e:
            messagebox.showerror(_("Export Origin"), str(e), parent=self)
            self.app.log(_("[ECHEC] export Origin : %s") % e)
            return
        self.app.log(_("Export Origin : %s") % path)
        self.app.set_status(_("Export Origin ecrit."))
        messagebox.showinfo(
            _("Export Origin"),
            _("Fichier ecrit :\n%s\n\nDans Origin : File > Import > Excel, "
            "avec Long Names = 1, Units = 2, Data begins on = 3.") % path,
            parent=self)

    def export_csv(self):
        if not self.app.datasets:
            return
        d = filedialog.askdirectory(title=_("Dossier de destination"))
        if not d:
            return
        for ds in self.app.datasets:
            fn = "".join(c if c.isalnum() or c in "-_ " else "_"
                         for c in ds["name"]).strip()
            pd.DataFrame({"P (bar)": ds["P"], "q (mmol/g)": ds["q"]}).to_csv(
                os.path.join(d, "%s.csv" % fn), index=False)
        messagebox.showinfo(_("Export"), _("%d fichiers CSV ecrits dans :\n%s")
                            % (len(self.app.datasets), d), parent=self)

    def save(self, as_new=False):
        self.app.save_session(as_new=as_new)

    def open(self):
        self.app.open_session()

    def run_selftest(self):
        show_text_window(self, _("Verification interne"), run_selftest())


# =============================================================================
# 14. FENETRE PRINCIPALE
# =============================================================================

# =============================================================================
# 14. VERIFICATION INTERNE
# =============================================================================

def run_selftest():
    """Rejoue les controles numeriques du noyau scientifique."""
    out = []
    ok_n = [0]
    ko_n = [0]

    def chk(name, cond, detail=""):
        (ok_n if cond else ko_n).__getitem__(0)
        if cond:
            ok_n[0] += 1
        else:
            ko_n[0] += 1
        out.append("  [%s] %-52s %s" % ("OK " if cond else _("ECHEC"), name, detail))

    t0 = datetime.datetime.now()
    out.append(_("VERIFICATION INTERNE  -  %s v%s") % (APP_NAME, APP_VERSION))
    out.append("=" * 78)
    ctx = {"T": 303.15, "P0": 64.0}
    P = np.linspace(0.05, 50, 40)

    out.append(_("\n1. Ajustement : recuperation de parametres exacts"))
    cases = [("langmuir", [14.5, 0.08]), ("dsl", [8.0, 0.5, 7.0, 0.02]),
             ("freundlich", [3.0, 0.45]), ("sips", [16.0, 0.06, 0.85]),
             ("toth", [18.0, 0.05, 0.7]), ("dr", [12.0, 2.2e-9]),
             ("da", [12.0, 18000.0, 2.4])]
    for key, true in cases:
        m = MODELS[key]
        q = np.asarray(m.func(P, ctx, *true)).ravel()
        try:
            r = fit_isotherm(m, P, q, ctx)
            e = max(abs(a - b) / max(abs(b), 1e-12)
                    for a, b in zip(r["params"], true))
            chk(m.label, r["stats"]["R2"] > 0.9999 and e < 1e-4,
                _("R2=%.8f  erreur relative max=%.1e") % (r["stats"]["R2"], e))
        except Exception as ex:
            chk(m.label, False, str(ex))

    out.append(_("\n2. Pression d'etalement : formule analytique vs integration"))
    def pi_num(m, par, Pt):
        y = np.linspace(math.log(Pt) - 40, math.log(Pt), 200000)
        return float(_TRAPZ(np.asarray(m.func(np.exp(y), ctx, *par)).ravel(), y))
    for key, par in cases:
        m = MODELS[key]
        sp = SpreadingPressure(m, ctx, par)
        errs = []
        for Pt in (0.5, 5.0, 40.0):
            a = float(sp.value(Pt)[0])
            n = pi_num(m, par, Pt)
            errs.append(abs(a - n) / max(abs(n), 1e-12))
        chk("pi* " + m.label, max(errs) < 1e-5, _("ecart relatif max=%.1e")
            % max(errs))

    out.append(_("\n3. IAST : coherence thermodynamique"))
    L = MODELS["langmuir"]
    qm, b1, b2 = 12.0, 0.30, 0.05
    c2 = [SpreadingPressure(L, ctx, [qm, b1]), SpreadingPressure(L, ctx, [qm, b2])]
    err = 0.0
    for Pt in (0.01, 0.5, 5, 50, 200):
        r = iast_point(Pt, [0.4, 0.6], c2)
        p1, p2 = 0.4 * Pt, 0.6 * Pt
        den = 1 + b1 * p1 + b2 * p2
        ex = [qm * b1 * p1 / den, qm * b2 * p2 / den]
        err = max(err, max(abs(r["q"][i] - ex[i]) / ex[i] for i in (0, 1)))
    chk(_("q_max identiques -> Langmuir competitif exact"), err < 1e-9,
        _("ecart relatif max=%.1e") % err)

    c3 = [SpreadingPressure(MODELS["toth"], ctx, [18.0, 0.05, 0.7]),
          SpreadingPressure(MODELS["sips"], ctx, [9.0, 0.03, 0.85]),
          SpreadingPressure(MODELS["da"], ctx, [6.0, 12000.0, 2.0])]
    dpi_max, dx_max = 0.0, 0.0
    for Pt in (0.5, 5.0, 30.0, 60.0):
        r = iast_point(Pt, [0.5, 0.3, 0.2], c3)
        pis = [float(c3[i].value(r["P0"][i])[0]) for i in range(3)]
        dpi_max = max(dpi_max, max(pis) - min(pis))
        dx_max = max(dx_max, abs(sum(r["x"]) - 1.0))
    chk(_("melange Toth+Sips+D-A : pi identiques et somme x = 1"),
        dpi_max < 1e-6 and dx_max < 1e-9,
        _("ecart pi max=%.1e   |somme x - 1|=%.1e") % (dpi_max, dx_max))

    r = iast_point(1e-6, [0.4, 0.6], c2)
    e1 = abs(r["q"][0] / (0.4e-6) - qm * b1) / (qm * b1)
    e2 = abs(r["q"][1] / (0.6e-6) - qm * b2) / (qm * b2)
    chk(_("limite basse pression -> constantes de Henry"), max(e1, e2) < 1e-5,
        _("ecart relatif max=%.1e") % max(e1, e2))

    sp = [SpreadingPressure(L, ctx, p, P_exp_max=60.0)
          for p in ([14.8885, 0.0806], [7.4225, 0.0577], [12.0235, 0.0090])]
    df = iast_scan(np.array([10.0, 60.0]), [1 / 3, 1 / 3, 1 / 3], sp,
                   ["CO2", "CH4", "H2"])
    rr = float(df["Extrapolation max (P0/P_exp)"].iloc[-1])
    chk(_("detection de l'extrapolation des modeles"), rr > 2.0,
        _("P0 max = %.1f x la pression mesuree a 60 bar") % rr)

    # Valeurs de reference calculees par pyIAST 1.4.3 (Simon, Smit et
    # Haranczyk, Comput. Phys. Commun. 2016) avec les memes isothermes ;
    # Toth, Sips et D-A y passent par une table interpolee (tolerance 1e-4).
    _l1, _l2 = ("langmuir", [10.87, 0.181]), ("langmuir", [7.12, 0.0817])
    _ref = [
        ([_l1, _l2], 1.0, [0.5, 0.5],
         [0.8754956900612786, 0.2512783539742332], 1e-9),
        ([_l1, _l2], 10.0, [0.15, 0.85],
         [1.6498462505520577, 2.38315931137052], 1e-9),
        ([_l1, _l2], 40.0, [0.5, 0.5],
         [7.186096348451396, 1.1938869139381696], 1e-9),
        ([("dsl", [2.0, 5.0, 6.0, 0.1]), ("langmuir", [7.0, 0.05])], 10.0,
         [0.25, 0.75], [2.7883843395140198, 0.7200173343040145], 1e-9),
        ([_l1, _l2, ("langmuir", [5.29, 0.0131])], 10.0, [0.5, 0.3, 0.2],
         [4.701489947678235, 0.672026831970503, 0.0425032920310536], 1e-9),
        ([("toth", [18.0, 0.05, 0.7]), ("sips", [9.0, 0.03, 0.85])], 20.0,
         [0.5, 0.5], [3.7517058918812376, 1.4778104537010128], 1e-4),
        ([("da", [12.0, 18000.0, 2.4]), _l2], 20.0, [0.5, 0.5],
         [11.528623284312763, 0.0048248076492007], 1e-4),
    ]
    _ok, _wa, _wt = True, 0.0, 0.0
    for _cps, _Pt, _y, _qref, _tol in _ref:
        _sps = [SpreadingPressure(MODELS[k], ctx, p) for k, p in _cps]
        _r = iast_point(_Pt, _y, _sps)
        _rel = max(abs(_r["q"][i] - _qref[i]) / _qref[i]
                   for i in range(len(_qref)))
        if _tol < 1e-6:
            _wa = max(_wa, _rel)
        else:
            _wt = max(_wt, _rel)
        _ok = _ok and _rel < _tol
    chk(_("IAST = pyIAST 1.4.3 sur 7 melanges de reference"), _ok,
        _("ecart max %.0e (analytique), %.0e (table)") % (_wa, _wt))

    out.append(_("\n4. Equation d'etat et pressions de saturation"))
    z1 = eos_z_effective(298.15, 1.0, "CO2")
    z2 = eos_z_effective(298.15, 100.0, "CH4")
    z3 = eos_z_effective(298.15, 100.0, "H2")
    chk(_("Z(CO2, 1 bar) proche de 1"), 0.99 < z1 < 1.0, "Z=%.4f" % z1)
    chk(_("Z(CH4, 100 bar) entre 0.80 et 0.88"), 0.80 < z2 < 0.88, "Z=%.4f" % z2)
    chk(_("Z(H2, 100 bar) superieur a 1"), 1.0 < z3 < 1.10, "Z=%.4f" % z3)
    ps, meth = saturation_pressure("CO2", 298.15)
    chk(_("P_sat(CO2, 298.15 K) proche de 64.2 bar"), abs(ps - 64.2) < 1.5,
        _("%.2f bar (%s)") % (ps, meth))
    ps2, meth2 = saturation_pressure("CH4", 298.15)
    chk(_("CH4 supercritique -> regle de Dubinin"), "Dubinin" in meth2,
        _("%.1f bar") % ps2)
    _ps, _ab, _sr = saturation_check("CO2", 273.15, [10.0, 30.0, 36.0, 40.0])
    chk(_("points au-dessus de Psat signales (CO2 a 273 K)"),
        list(_ab) == [False, False, True, True] and abs(_ps - 34.85) < 1.0
        and not saturation_check("CH4", 303.15, [100.0])[1].any(),
        _("Psat = %.2f bar (%s)") % (_ps, _sr))
    nt, rho = excess_to_total(np.array([1.0, 30.0]), np.array([2.0, 12.0]),
                              298.15, "CO2", "Volume poreux", V_pore=0.6)
    chk(_("conversion exces -> total croissante avec P"),
        nt[0] > 2.0 and nt[1] > 12.0 and (nt[1] - 12.0) > (nt[0] - 2.0),
        _("n_tot = %.4f puis %.4f mmol/g") % (nt[0], nt[1]))

    out.append(_("\n5. Unites et robustesse"))
    q0 = np.array([1.0, 5.0, 12.0])
    rt = mmol_g_to_unit(q_to_mmol_g(q0, "cm3(STP)/g", 44.01), "cm3(STP)/g", 44.01)
    chk(_("aller-retour d'unites cm3(STP)/g"), np.allclose(rt, q0, rtol=1e-12))
    chk(_("lecture de nombres a virgule decimale"),
        abs(to_float("1,25") - 1.25) < 1e-12 and np.isnan(to_float("abc")))
    chk(_("valeur de repli sur saisie invalide"),
        to_float_or("abc", 7.0) == 7.0 and to_float_or("", 3.0) == 3.0)

    out.append(_("\n6. Robustesse statistique"))
    rng = np.random.default_rng(4)
    qn = np.asarray(MODELS["sips"].func(P, ctx, 16.0, 0.06, 0.85)).ravel()
    qn = qn * (1 + rng.normal(0, 0.012, len(P)))
    r = fit_isotherm(MODELS["sips"], P, qn, ctx, n_starts=8, n_boot=60)
    chk(_("multi-depart et bootstrap operationnels"),
        r["n_boot"] >= 10 and r["ci_lo"] is not None
        and r["ci_lo"][0] < r["params"][0] < r["ci_hi"][0],
        _("%d tirages, IC q_max = [%.2f ; %.2f]")
        % (r["n_boot"], r["ci_lo"][0], r["ci_hi"][0]))
    chk(_("correlation des parametres calculee"),
        np.isfinite(r.get("r_max", np.nan)), _("|r|max = %.4f") % r["r_max"])
    bad = [200.0, 1e-4, 2.5]
    r1 = fit_isotherm(MODELS["toth"], P, qn, ctx, p0=bad, n_starts=1)
    r2 = fit_isotherm(MODELS["toth"], P, qn, ctx, p0=bad, n_starts=20)
    chk(_("multi-depart jamais moins bon qu'un depart unique"),
        r2["stats"]["SSR"] <= r1["stats"]["SSR"] * (1 + 1e-9),
        _("SSR %.4e -> %.4e") % (r1["stats"]["SSR"], r2["stats"]["SSR"]))

    # ---------------------------------------------------- 7. ajouts v3.0
    out.append("")
    out.append(_("7. Densites de reference et conversion (v3.0)"))
    chk(_("table NIST : 3 gaz a 303 K"),
        set(g for g, _T in NIST_TABLES) == {"CO2", "CH4", "H2"},
        ", ".join(sorted(g for g, _T in NIST_TABLES)))
    _v = nist_density_mmol_cm3(303.0, 40.0, "CH4")
    chk(_("rho(CH4, 303 K, 40 bar) = 1.69394 mol/L"), abs(_v - 1.69394) < 1e-5,
        _("%.5f mol/L") % _v)
    _v = nist_density_mmol_cm3(303.0, 40.0, "CO2")
    chk(_("rho(CO2, 303 K, 40 bar) = 2.04183 mol/L"), abs(_v - 2.04183) < 1e-5,
        _("%.5f mol/L") % _v)
    chk(_("CO2 au-dela de Psat(303 K) : hors table"),
        not np.isfinite(nist_density_mmol_cm3(303.0, 80.0, "CO2")),
        _("Psat = 71.89 bar"))
    _a = gas_density_mmol_cm3(303.0, 80.0, "CO2", eos="Table NIST")
    _b = gas_density_mmol_cm3(303.0, 80.0, "CO2", eos="Peng-Robinson")
    chk(_("repli automatique sur Peng-Robinson hors table"),
        abs(_a - _b) < 1e-12, _("rho = %.5f mol/L") % _a)
    _e = 100.0 * abs(gas_density_mmol_cm3(303.0, 40.0, "CH4",
                                          eos="Peng-Robinson") / 1.69394 - 1)
    chk(_("ecart Peng-Robinson / NIST sur CH4 inferieur a 3 %"), _e < 3.0,
        _("%.2f %% a 40 bar") % _e)
    chk(_("deduction du gaz depuis le nom de fichier"),
        guess_gas_from_name("ZTC850-CO2.xlsx") == "CO2"
        and guess_gas_from_name("P800_CH4.csv") == "CH4"
        and guess_gas_from_name("ZTC-H2.xlsx") == "H2")
    chk(_("deduction de l'echantillon depuis le nom de fichier"),
        guess_sample_from_name("ZTC850-CO2.xlsx") == "ZTC850",
        guess_sample_from_name("ZTC850-CO2.xlsx"))
    chk(_("temperature lue dans le nom de fichier, noms de jeux uniques"),
        guess_temperature_from_name("ZTC850-CO2_303K.xlsx") == 303.0
        and guess_temperature_from_name("MOF 273.15 K N2.csv") == 273.15
        and guess_temperature_from_name("ZTC-800C_CO2.xlsx") is None
        and guess_temperature_from_name("K2CO3-CO2.xlsx") is None
        and dataset_name_from_file("ZTC850-CO2_303K.xlsx", "CO2")
        == "ZTC850 303K CO2"
        and dataset_name_from_file("CO2.xlsx", "CO2") == "CO2"
        and unique_name("A", {"A", "A (2)"}) == "A (3)")
    _fmt = lambda s: re.findall(r"%[-+ #0-9.]*[a-zA-Z%]", s)
    chk(_("accents du francais affiche, codes de format intacts"),
        all(len(v) == len(k) and _fmt(v) == _fmt(k) for k, v in TR_FR.items())
        and fr_accents("%d jeu(x) cree(s), Degre a, D-A a %.2f K")
        == "%d jeu(x) créé(s), Degré a, D-A à %.2f K")
    _P = np.array([0.0, 10.0, 40.0])
    _nt, _rho = excess_to_total(_P, np.array([0.0, 3.0, 5.0]), 303.0, "CH4",
                                method="Volume poreux", V_pore=0.54,
                                eos="Table NIST")
    chk(_("conversion exces -> total via la table NIST"),
        abs(_nt[2] - (5.0 + 1.69394 * 0.54)) < 1e-6,
        _("n_tot(40 bar) = %.5f mmol/g") % _nt[2])

    out.append(_("\n8. Gaz et chaleur isosterique"))
    chk(_("base des gaz complete (Tc, Pc, w, M)"),
        all(all(k in d and np.isfinite(d[k]) for k in ("Tc", "Pc", "w", "M"))
            for d in GAS_DB.values()), _("%d gaz") % len(GAS_DB))
    chk(_("reconnaissance des nouveaux gaz dans les noms de fichiers"),
        guess_gas_from_name("MOF_ethylene_273K.csv") == "C2H4"
        and guess_gas_from_name("X-methane.xlsx") == "CH4"
        and guess_gas_from_name("Z_isobutane.csv") == "i-C4H10"
        and guess_gas_from_name("A-C2H2.xlsx") == "C2H2")
    # coefficient de fugacite : integration de Z contre la formule de PR
    _g = GAS_DB["CO2"]
    _T, _Pb = 303.15, 40.0
    _kap = 0.37464 + 1.54226 * _g["w"] - 0.26992 * _g["w"] ** 2
    _al = (1 + _kap * (1 - math.sqrt(_T / _g["Tc"]))) ** 2
    _a = 0.45723553 * R_J ** 2 * _g["Tc"] ** 2 / (_g["Pc"] * 1e5) * _al
    _b = 0.07779607 * R_J * _g["Tc"] / (_g["Pc"] * 1e5)
    _A = _a * _Pb * 1e5 / (R_J * _T) ** 2
    _B = _b * _Pb * 1e5 / (R_J * _T)
    _Z = pr_compressibility(_T, _Pb, _g["Tc"], _g["Pc"], _g["w"])
    _lnphi = (_Z - 1 - math.log(_Z - _B) - _A / (2 * math.sqrt(2) * _B)
              * math.log((_Z + (1 + math.sqrt(2)) * _B)
                         / (_Z + (1 - math.sqrt(2)) * _B)))
    _c = 0.40768 * (R_J * _g["Tc"] / (_g["Pc"] * 1e5)) * (
        0.29441 - (0.29056 - 0.08775 * _g["w"]))
    _lnphi -= _c * _Pb * 1e5 / (R_J * _T)
    _num = math.log(fugacity_coefficient(_T, _Pb, "CO2", "Peng-Robinson"))
    chk(_("fugacite : integration numerique = formule de Peng-Robinson"),
        abs(_num - _lnphi) < 5e-4,
        _("phi(CO2, 303 K, 40 bar) = %.4f") % math.exp(_num))
    _d1 = abs(math.log(fugacity_coefficient(303.15, 0.1, "CO2", "Table NIST"))
              - math.log(fugacity_coefficient(303.15, 0.1, "CO2")))
    _d5 = abs(math.log(fugacity_coefficient(303.15, 5.0, "CO2", "Table NIST"))
              - math.log(fugacity_coefficient(303.15, 5.0, "CO2")))
    chk(_("fugacite par la table NIST coherente a basse pression"),
        _d1 < 2e-4 and _d5 < 3e-3,
        _("ecart ln(phi) %.1e a 0,1 bar, %.1e a 5 bar") % (_d1, _d5))
    # isothermes de Langmuir a chaleur constante Q = 25 kJ/mol
    _Q, _qm, _Pq = 25000.0, 10.0, np.geomspace(0.01, 10.0, 20)
    _ent, _pts = [], []
    for _Tq in (273.15, 298.15, 323.15):
        _bq = 0.5 * math.exp(_Q / R_J * (1 / _Tq - 1 / 298.15))
        _qq = _qm * _bq * _Pq / (1 + _bq * _Pq)
        _ent.append(dict(name="L", T=_Tq, model_key="langmuir",
                         params=[_qm, _bq], ctx={"T": _Tq, "P0": 50.0},
                         P_min=0.01, P_max=10.0, q_min=float(_qq.min()),
                         q_max=float(_qq.max())))
        _pts.append((_Tq, _Pq[_Pq <= 1.0], _qq[_Pq <= 1.0]))
    _lo, _hi = qst_common_range(_ent)
    _dfq = qst_clausius_clapeyron(_ent, np.linspace(_lo, _hi, 9), "CO2",
                                  basis=QST_BASES[1])
    _err = float(np.nanmax(np.abs(_dfq["Qst CC (kJ/mol)"].values - 25.0)))
    chk(_("Qst Clausius-Clapeyron : Langmuir a Q = 25 kJ/mol"), _err < 1e-3,
        _("ecart max %.1e kJ/mol") % _err)
    _vf = virial_fit(_pts, basis=QST_BASES[1])
    _Qv, _uv = virial_qst(_vf, np.linspace(0.05, _vf["n_max_common"], 6))
    chk(_("Qst viriel (P <= 1 bar) : Langmuir a Q = 25 kJ/mol"),
        abs(_vf["Qst0"] - 25.0) < 0.05 and float(np.max(np.abs(_Qv - 25))) < 0.1,
        _("Qst0 = %.3f kJ/mol") % _vf["Qst0"])

    dt = (datetime.datetime.now() - t0).total_seconds()
    out.append("\n" + "=" * 78)
    out.append(_("RESULTAT : %d controles reussis, %d echecs   (%.1f s)")
               % (ok_n[0], ko_n[0], dt))
    if ko_n[0] == 0:
        out.append(_("Le noyau scientifique se comporte comme attendu."))
    else:
        out.append(_("ATTENTION : au moins un controle a echoue, voir le detail."))
    return "\n".join(out)


# =============================================================================
# 15. FENETRE PRINCIPALE  (v2)
# =============================================================================

STEPS = ["Donnees", "Conversion", "Ajustement", "IAST", "Chaleur isosterique",
         "Graphiques", "Session / Export"]
TAB_DATA, TAB_CONV, TAB_FIT, TAB_IAST, TAB_QST, TAB_PLOT, TAB_EXPORT = range(7)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.datasets = []
        self.fits = []
        self.series = []
        self.notes = ""
        self.session_path = None
        self.dirty = False
        self._last_tab = 0
        self.settings = load_settings()

        apply_theme(self)
        self.title("%s v%s" % (APP_NAME, APP_VERSION))
        for ic in ("adsorpsuite.ico", "adsorpsuite.png"):
            try:
                path = resource_path(ic)
                if not os.path.exists(path):
                    continue
                if ic.endswith(".ico"):
                    self.iconbitmap(default=path)
                else:
                    self.iconphoto(True, tk.PhotoImage(file=path))
                break
            except Exception:
                continue
        geo = self.settings.get("geometry")
        fits = self._geo_fits(geo)
        self.geometry(geo if fits else "1500x960")
        self.minsize(1150, 720)
        if self.settings.get("zoomed", not fits) or not fits:
            try:
                self.state("zoomed")
            except Exception:
                pass

        self._build_menu()
        self._build_toolbar()

        self.steps = StepBar(self, STEPS, command=self.goto)
        self.steps.pack(fill="x")
        tk.Frame(self, height=1, bg=UI["line"]).pack(fill="x")
        # barre d'etat et journal places avant les onglets : ils gardent leur
        # place meme quand les onglets demandent plus de hauteur que la fenetre
        self._build_status()
        self._build_logbar()

        body = ttk.Frame(self, padding=(8, 8, 8, 4))
        body.pack(fill="both", expand=True)
        self.nb = ttk.Notebook(body, style="Hidden.TNotebook")
        self.nb.pack(fill="both", expand=True)
        self.tab_data = TabData(self.nb, self)
        self.tab_conv = TabConversion(self.nb, self)
        self.tab_fit = TabFit(self.nb, self)
        self.tab_iast = TabIAST(self.nb, self)
        self.tab_qst = TabQst(self.nb, self)
        self.tab_plot = TabPlot(self.nb, self)
        self.tab_export = TabExport(self.nb, self)
        for t, n in zip((self.tab_data, self.tab_conv, self.tab_fit,
                         self.tab_iast, self.tab_qst, self.tab_plot,
                         self.tab_export), STEPS):
            self.nb.add(t, text=_(n))
        self.nb.bind("<<NotebookTabChanged>>", self._tab_changed)

        self._bind_keys()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.steps.set_active(0)

        self.log(_("%s v%s pret.") % (APP_NAME, APP_VERSION))
        self.log(_("CoolProp %s. Astuce : F1 ouvre l'aide, F5 lance l'action de "
                 "l'onglet courant.")
                 % (_("detecte") if HAS_COOLPROP else _("absent, Peng-Robinson "
                    "utilise")))
        last = self.settings.get("last_session")
        if last and os.path.exists(last):
            self.set_status(_("Derniere session : %s  (menu Fichier pour la "
                            "rouvrir)") % os.path.basename(last))

    # ------------------------------------------------------------ interface
    def _build_toolbar(self):
        bar = ttk.Frame(self, style="Bar.TFrame", padding=(10, 7))
        bar.pack(fill="x")
        ttk.Label(bar, text=APP_NAME, style="Title.TLabel").pack(side="left",
                                                                 padx=(0, 4))
        ttk.Label(bar, text="v%s" % APP_VERSION,
                  style="Muted.TLabel").pack(side="left", padx=(0, 18))

        def sep():
            tk.Frame(bar, width=1, bg=UI["line"]).pack(side="left", fill="y",
                                                       padx=8, pady=2)

        def btn(txt, cmd, hint, style="Tool.TButton"):
            # width=0 : largeur du texte, sinon "Aide" sort d'une fenetre
            # de 1150 px
            b = ttk.Button(bar, text=txt, style=style, command=cmd, width=0)
            b.pack(side="left", padx=2)
            tip(b, hint)
            return b

        btn(_("Nouvelle session"), self.new_session,
            _("Repartir de zero (Ctrl+N)"))
        btn(_("Ouvrir..."), self.open_session,
            _("Recharger une session enregistree (Ctrl+O)"))
        self.btn_save = btn(_("Enregistrer"), self.save_session,
                            _("Enregistrer toute la session dans un fichier "
                            ".adsp (Ctrl+S)"), "Primary.TButton")
        sep()
        btn(_("Importer des donnees"), self._import_many,
            _("Lire un ou plusieurs fichiers Excel ou CSV d'isothermes "
              "(Ctrl+I)"))
        btn(_("Ajuster"), lambda: (self.goto(TAB_FIT), self.tab_fit.run_fit()),
            _("Aller a l'ajustement et lancer les modeles coches"))
        btn("IAST", lambda: (self.goto(TAB_IAST), self.tab_iast.run()),
            _("Aller au calcul de melange et le lancer"))
        btn("Qst", lambda: self.goto(TAB_QST),
            _("Chaleur isosterique a partir de plusieurs temperatures"))
        sep()
        btn(_("Export Excel"), self.tab_export_all,
            _("Classeur complet : donnees, ajustements, courbes, IAST"))
        btn(_("Aide"), self.show_help, _("Aide rapide (F1)"))

    def _build_logbar(self):
        """Historique des messages, replie au depart : la barre d'etat montre
        le dernier, le bouton 'Journal' deplie la liste."""
        self.logbox = ttk.Frame(self, style="Card.TFrame", padding=(10, 4))
        self.txt_log = tk.Text(self.logbox, height=5, font=("Consolas", 9),
                               relief="flat", background="#fbfdff",
                               foreground=UI["ink"])
        vs = ttk.Scrollbar(self.logbox, orient="vertical",
                           command=self.txt_log.yview)
        self.txt_log.configure(yscrollcommand=vs.set)
        ttk.Button(self.logbox, text=_("Effacer"), style="Ghost.TButton",
                   command=lambda: self.txt_log.delete("1.0", "end")).pack(
            side="right", anchor="n")
        vs.pack(side="right", fill="y")
        self.txt_log.pack(side="left", fill="x", expand=True)

    def _toggle_log(self):
        if self.logbox.winfo_ismapped():
            self.logbox.pack_forget()
        else:           # juste au-dessus de la barre d'etat, avant les onglets
            self.logbox.pack(fill="x", side="bottom", after=self._status)

    def _build_status(self):
        st = self._status = ttk.Frame(self, style="Bar.TFrame", padding=(10, 3))
        st.pack(fill="x", side="bottom")
        tip(ttk.Button(st, text=_("Journal"), style="Ghost.TButton",
                       command=self._toggle_log),
            _("Affiche ou masque l'historique des messages")).pack(side="right")
        self.lbl_session = ttk.Label(st, text=_("Session non enregistree"),
                                     style="Status.TLabel")
        self.lbl_session.pack(side="right", padx=12)
        self.pb = ttk.Progressbar(st, mode="determinate", length=170)
        self.lbl_status = ttk.Label(st, text=_("Pret"), style="Status.TLabel")
        self.lbl_status.pack(side="left")

    def _build_menu(self):
        mb = tk.Menu(self)
        m1 = tk.Menu(mb, tearoff=0)
        m1.add_command(label=_("Nouvelle session"), accelerator="Ctrl+N",
                       command=self.new_session)
        m1.add_command(label=_("Ouvrir une session..."), accelerator="Ctrl+O",
                       command=self.open_session)
        m1.add_command(label=_("Enregistrer la session"), accelerator="Ctrl+S",
                       command=self.save_session)
        m1.add_command(label=_("Enregistrer sous..."),
                       accelerator=_("Ctrl+Maj+S"),
                       command=lambda: self.save_session(as_new=True))
        self.menu_recent = tk.Menu(m1, tearoff=0)
        m1.add_cascade(label=_("Sessions recentes"), menu=self.menu_recent)
        m1.add_separator()
        m1.add_command(label=_("Importer des fichiers..."),
                       accelerator="Ctrl+I", command=self._import_many)
        m1.add_command(label=_("Export Origin (Long Name + Units)..."),
                       accelerator="Ctrl+E",
                       command=lambda: self.tab_export.export_origin())
        m1.add_separator()
        m1.add_command(label=_("Export Excel global..."),
                       command=self.tab_export_all)
        m1.add_separator()
        m1.add_command(label=_("Quitter"), command=self.on_close)
        mb.add_cascade(label=_("Fichier"), menu=m1)
        m2 = tk.Menu(mb, tearoff=0)
        for i, nm in enumerate(STEPS):
            m2.add_command(label="%d. %s" % (i + 1, _(nm)),
                           accelerator="Ctrl+%d" % (i + 1),
                           command=lambda k=i: self.goto(k))
        mb.add_cascade(label=_("Aller a"), menu=m2)
        m3 = tk.Menu(mb, tearoff=0)
        m3.add_command(label=_("Aide rapide"), accelerator="F1",
                       command=self.show_help)
        m3.add_command(label=_("Modeles et equations"),
                       command=lambda: show_text_window(self, _("Modeles"),
                                                        models_text()))
        m3.add_command(label=_("Verification interne du programme"),
                       command=lambda: show_text_window(
                           self, _("Verification interne"), run_selftest()))
        m3.add_command(label=_("A propos"), command=self.about)
        m4 = tk.Menu(mb, tearoff=0)
        self.var_lang = tk.StringVar(value=LANG)
        for code, name in LANGUAGES:
            m4.add_radiobutton(label=name, value=code, variable=self.var_lang,
                               command=lambda c=code: self.change_language(c))
        mb.add_cascade(label="Langue / Language", menu=m4)
        mb.add_cascade(label=_("Aide"), menu=m3)
        self.config(menu=mb)
        self._refresh_recent()

    def _bind_keys(self):
        self.bind_all("<Control-s>", lambda e: self.save_session())
        self.bind_all("<Control-S>", lambda e: self.save_session(as_new=True))
        self.bind_all("<Control-o>", lambda e: self.open_session())
        self.bind_all("<Control-n>", lambda e: self.new_session())
        self.bind_all("<F1>", lambda e: self.show_help())
        self.bind_all("<F5>", lambda e: self.run_current())
        self.bind_all("<Shift-F5>", lambda e: self._run_all())
        self.bind_all("<Control-i>", lambda e: self._import_many())
        self.bind_all("<Control-e>", lambda e: self.tab_export.export_origin())
        for i in range(len(STEPS)):
            self.bind_all("<Control-Key-%d>" % (i + 1),
                          lambda e, k=i: self.goto(k))
        if sys.platform.startswith("win"):
            # meme chose par la touche physique : sur un clavier AZERTY,
            # Ctrl+1 envoie '&' et les raccourcis ci-dessus restent muets
            self.bind_all("<Control-KeyPress>", lambda e: (
                self.goto(e.keycode - 49)
                if 49 <= e.keycode < 49 + len(STEPS) else None))

    def _run_all(self):
        """Maj+F5 : action 'en lot' de l'onglet actif."""
        try:
            i = self.nb.index(self.nb.select())
        except Exception:
            return
        if i == TAB_CONV:
            self.tab_conv.convert_all()
        elif i == TAB_FIT:
            self.tab_fit.run_fit_all()
        else:
            self.set_status(_("Maj+F5 : disponible dans les onglets Conversion "
                            "et Ajustement."))

    def _import_many(self):
        self.goto(TAB_DATA)
        self.tab_data.import_many()

    # ------------------------------------------------------------ navigation
    def goto(self, idx):
        try:
            self.nb.select(idx)
        except Exception:
            pass

    def run_current(self):
        i = self._last_tab
        try:
            (self.tab_data.save_current, self.tab_conv.compute,
             self.tab_fit.run_fit, self.tab_iast.run, self.tab_qst.run,
             self.tab_plot.draw, self.tab_export.refresh)[i]()
        except Exception as e:
            self.log("F5 : %s" % e)

    def _tab_changed(self, event=None):
        try:
            if getattr(self, "tab_data", None) is not None:
                self.tab_data._autosave()
        except Exception:
            pass
        try:
            idx = self.nb.index(self.nb.select())
        except Exception:
            return
        self._last_tab = idx
        self.steps.set_active(idx)
        if idx == TAB_CONV:
            self.tab_conv.refresh()
        elif idx == TAB_FIT:
            self.tab_fit.refresh()
        elif idx == TAB_IAST:
            self.tab_iast.refresh()
        elif idx == TAB_QST:
            self.tab_qst.refresh()
        elif idx == TAB_EXPORT:
            self.tab_export.refresh()

    # --------------------------------------------------------------- session
    def _title(self):
        nm = (os.path.basename(self.session_path) if self.session_path
              else _("session non enregistree"))
        self.title("%s v%s  -  %s%s" % (APP_NAME, APP_VERSION, nm,
                                        " *" if self.dirty else ""))
        try:
            self.lbl_session.config(
                text="%s%s" % (nm, _("  (modifie)") if self.dirty else ""))
        except Exception:
            pass

    def mark_dirty(self, state=True):
        self.dirty = bool(state)
        self._title()

    def save_session(self, as_new=False):
        self.tab_data._autosave()       # la saisie en cours fait partie de la session
        path = self.session_path
        if as_new or not path:
            init = os.path.basename(path) if path else _("session_adsorption.adsp")
            path = filedialog.asksaveasfilename(
                defaultextension=SESSION_EXT, initialfile=init,
                initialdir=self.settings.get("last_dir", ""),
                title=_("Enregistrer la session"),
                filetypes=[(_("Session AdsorpSuite"), "*" + SESSION_EXT),
                           ("JSON", "*.json")])
            if not path:
                return False
        try:
            write_session(self, path)
        except Exception as e:
            messagebox.showerror(_("Session"), _("Enregistrement impossible :\n%s")
                                 % e, parent=self)
            return False
        self.session_path = path
        self.settings["last_session"] = path
        self.settings["last_dir"] = os.path.dirname(path)
        self._push_recent(path)
        save_settings(self.settings)
        self.mark_dirty(False)
        self.log(_("Session enregistree : %s") % path)
        self.set_status(_("Session enregistree (%d jeux, %d ajustements)")
                        % (len(self.datasets), len(self.fits)))
        return True

    def open_session(self, path=None):
        if not self._confirm_discard():
            return
        if not path:
            path = filedialog.askopenfilename(
                title=_("Ouvrir une session"),
                initialdir=self.settings.get("last_dir", ""),
                filetypes=[(_("Session AdsorpSuite"), "*" + SESSION_EXT),
                           ("JSON", "*.json"), (_("Tous les fichiers"), "*.*")])
        if not path:
            return
        try:
            data = read_session(path)
            info = restore_session(self, data)
        except Exception as e:
            messagebox.showerror(_("Session"), _("Lecture impossible :\n%s\n\n%s")
                                 % (e, traceback.format_exc()), parent=self)
            return
        self.session_path = path
        self.settings["last_session"] = path
        self.settings["last_dir"] = os.path.dirname(path)
        self._push_recent(path)
        save_settings(self.settings)
        self.refresh_all()
        self.mark_dirty(False)
        msg = (_("Session chargee : %d jeux, %d ajustements, %d series, "
               "%d points IAST") % (info["datasets"], info["fits"],
                                   info["series"], info["iast"]))
        self.log(msg + "  (%s)" % path)
        self.set_status(msg)

    def new_session(self):
        if not self._confirm_discard():
            return
        self.datasets, self.fits, self.series = [], [], []
        self.notes = ""
        self.session_path = None
        self.tab_iast.reset()
        self.tab_qst.from_session(None)
        self.refresh_all()
        self.mark_dirty(False)
        self.log(_("Nouvelle session."))

    def _confirm_discard(self):
        self.tab_data._autosave()       # sinon la saisie en cours partirait sans question
        if not self.dirty:
            return True
        r = messagebox.askyesnocancel(
            _("Session en cours"),
            _("La session en cours contient des modifications non "
            "enregistrees.\n\nVoulez-vous l'enregistrer maintenant ?"),
            parent=self)
        if r is None:
            return False
        if r:
            return self.save_session()
        return True

    def _push_recent(self, path):
        rec = [p for p in self.settings.get("recent", []) if p != path]
        rec.insert(0, path)
        self.settings["recent"] = rec[:8]
        self._refresh_recent()

    def _refresh_recent(self):
        try:
            self.menu_recent.delete(0, "end")
        except Exception:
            return
        rec = [p for p in self.settings.get("recent", []) if os.path.exists(p)]
        if not rec:
            self.menu_recent.add_command(label=_("(aucune)"), state="disabled")
            return
        for p in rec:
            self.menu_recent.add_command(
                label=os.path.basename(p),
                command=lambda q=p: self.open_session(q))

    def _geo_fits(self, geo):
        """Vrai si la geometrie enregistree tient dans l'ecran."""
        try:
            w, h, x, y = (int(v) for v in geo.replace("x", "+").split("+"))
            return (x >= -10 and y >= -10
                    and x + w <= self.winfo_screenwidth() + 10
                    and y + h <= self.winfo_screenheight() - 40)
        except Exception:
            return False

    def _save_window(self):
        """Memorise la fenetre. Agrandie, Tk renvoie sa taille plein ecran
        avec la position de la fenetre normale : on note alors seulement
        'agrandie', sinon elle rouvrirait plus grande que l'ecran."""
        try:
            self.settings["zoomed"] = self.state() == "zoomed"
            if not self.settings["zoomed"]:
                self.settings["geometry"] = self.geometry()
            save_settings(self.settings)
        except Exception:
            pass

    def on_close(self):
        if not self._confirm_discard():
            return
        self._save_window()
        self.destroy()

    # ------------------------------------------------------------- services
    def refresh_all(self):
        for fn in (self.tab_data.refresh_list, self.tab_fit.refresh_fits,
                   self.tab_plot.refresh_series, self.tab_conv.refresh,
                   self.tab_fit.refresh, self.tab_iast.refresh,
                   self.tab_qst.refresh, self.tab_export.refresh):
            try:
                fn()
            except Exception:
                pass

    def notify_datasets(self):
        try:
            self.tab_data.refresh_list()
        except Exception:
            pass
        for t in (self.tab_conv, self.tab_fit):
            try:
                t.refresh()
            except Exception:
                pass
        self.mark_dirty()

    def notify_fits(self):
        for t in (self.tab_iast, self.tab_qst):
            try:
                t.refresh()
            except Exception:
                pass
        self.mark_dirty()

    def add_series(self, label, x, y, kind="ligne"):
        i = len(self.series)
        self.series.append(dict(label=label, x=np.asarray(x, float),
                                y=np.asarray(y, float), kind=kind,
                                color=PALETTE[i % len(PALETTE)],
                                marker=MARKERS[i % 6], ls="-",
                                lw=1.8, ms=6.0, alpha=1.0, visible=True,
                                y2=False))
        self.mark_dirty()

    def tab_export_all(self):
        self.goto(TAB_EXPORT)
        self.tab_export.export_all()

    def show_help(self):
        show_text_window(self, _("Aide rapide"), fr_accents(HELP_TEXT)
                         if LANG == "fr" else HELP_TEXT_EN)

    def change_language(self, code):
        """Memorise la langue choisie et propose de redemarrer."""
        if code == LANG:
            return
        self.settings["language"] = code
        save_settings(self.settings)
        msg = {"fr": fr_accents("Le francais sera utilise au prochain "
                                "demarrage.\n\nRedemarrer AdsorpSuite "
                                "maintenant ?"),
               "en": "English will be used at the next start.\n\n"
                     "Restart AdsorpSuite now?"}[code]
        if messagebox.askyesno("Langue / Language", msg, parent=self):
            if self._confirm_discard():
                self.restart()
        else:
            try:
                self.var_lang.set(LANG)
            except Exception:
                pass

    def restart(self):
        """Relance le programme et rouvre la session en cours."""
        self._save_window()
        # sans l'ancienne langue ni une ancienne session passees en argument
        args = [a for a in sys.argv[1:] if not (
            a.startswith("--lang") or a.lower().endswith(SESSION_EXT))]
        if self.session_path:
            args.append(self.session_path)
        if not getattr(sys, "frozen", False):
            args.insert(0, sys.argv[0])
        try:
            import subprocess
            # PYINSTALLER_RESET_ENVIRONMENT : sans lui le .exe relance
            # reutilise le dossier temporaire de l'ancien, qui l'efface en
            # se fermant (plantage au demarrage)
            subprocess.Popen([sys.executable] + args, env=dict(
                os.environ, PYINSTALLER_RESET_ENVIRONMENT="1"))
        except Exception as e:
            messagebox.showerror("AdsorpSuite", str(e), parent=self)
            return
        self.destroy()

    def about(self):
        messagebox.showinfo(
            _("A propos"),
            _("%s v%s\n\nAnalyse d'isothermes d'adsorption : ajustement de "
            "modeles, conversion exces/total, IAST binaire et ternaire, "
            "graphiques et exports.\n\nPython %s\nnumpy %s - pandas %s - "
            "matplotlib %s\nCoolProp : %s\n\nConfiguration : %s")
            % (APP_NAME, APP_VERSION, sys.version.split()[0], np.__version__,
               pd.__version__, matplotlib.__version__,
               _("installe") if HAS_COOLPROP else _("non installe"), config_dir()),
            parent=self)

    def set_status(self, txt):
        try:
            self.lbl_status.config(text=txt)
        except Exception:
            pass

    def busy(self, on=True, value=None):
        """Affiche ou masque la barre de progression."""
        try:
            if on:
                self.pb.pack(side="right", padx=10)
                if value is not None:
                    self.pb["value"] = value
                self.config(cursor="watch")
            else:
                self.pb.pack_forget()
                self.config(cursor="")
            self.update_idletasks()
        except Exception:
            pass

    def log(self, msg):
        ts = datetime.datetime.now().strftime("%H:%M:%S")
        try:
            self.txt_log.insert("end", "[%s] %s\n" % (ts, msg))
            self.txt_log.see("end")
        except Exception:
            print(msg)
        self.set_status(msg[:150])


# =============================================================================
# 16. TRADUCTION ANGLAISE DE L'INTERFACE
# =============================================================================

HELP_TEXT_EN = """\
%s v%s - quick help
================================================================================

1) DATA TAB
   - "Import files..." reads one or several .xlsx / .xls / .csv files. The
     gas, the temperature (in K, e.g. ZTC850-CO2_303K.xlsx) and the sample
     are read from the file name; a summary table lets you correct them
     before the import. Rows in yellow should be checked.
   - "Import with column choice..." is for files with several sheets or
     several columns: you choose the sheet, the columns and the units.
   - "New empty dataset" creates an empty dataset; type the values or paste
     two columns from Excel with Ctrl+V.
   - Units are converted internally to bar and mmol/g.
   - The dataset is saved automatically when you switch dataset or tab,
     start a calculation, save the session or quit.
   - Two datasets never share a name: "(2)" is added when needed.

2) CONVERSION TAB  (excess -> total)
   - Pore volume      : n_tot = n_exc + V_pore x rho_gas(T,P)
     rho_gas comes from CoolProp (reference equations, included in the
     Windows program), from the NIST table (CO2, CH4, H2 at 303 K) or from
     Peng-Robinson. V_pore has to be entered: no value is suggested.
   - Adsorbed density : n_tot = n_exc / (1 - rho_gas/rho_ads)
   - Supplied density : you enter rho_gas yourself (column 2 of the table),
     for example from NIST REFPROP.
   - "Create a 'total' dataset" adds the result as a new dataset, ready for
     fitting.
   - Below the critical temperature, points above the saturation pressure
     (e.g. CO2 at 273 K above 34.9 bar) are flagged: the fluid is liquid
     there and the conversion no longer makes sense.
   - "Convert ALL excess datasets": when the datasets come from several
     samples, a pore volume is asked for each sample.

3) FITTING TAB
   - Models: Langmuir, dual-site Langmuir, Freundlich, Sips, Toth,
     Dubinin-Radushkevich and Dubinin-Astakhov (fixed or fitted P0).
   - The dataset offered first is a 'total' dataset when there is one: at
     high pressure, that is the one to fit for IAST and the isosteric heat.
     "Fit ALL datasets x ALL ticked models" skips the excess datasets that
     have already been converted.
   - P0 can be estimated automatically: Lee-Kesler correlation if T < Tc,
     Dubinin rule Pc(T/Tc)^2 if T > Tc.
   - Initial values and bounds can be edited in the table.
   - Weighting: least squares, 1/q or 1/q^2 (relative error).
   - Multi-start: restarts the fit from several random starting points and
     keeps the best. Useful for Toth, Sips and D-A, which have local minima.
   - Bootstrap: refits the model N times on resampled residuals and gives a
     95 %% confidence interval for each parameter. More honest than the
     asymptotic standard deviation of the covariance matrix.
   - Column |r|max: strongest correlation between two parameters. Above 0.99
     (red row), q_max and b compensate each other: their individual values
     cannot be identified, even with an R2 of 0.9999. A q_max from a Sips or
     Toth fit should then be quoted with its confidence interval.
   - "Compare" menu: the ranking (AIC) compares the models while penalising
     the number of parameters (dAIC < 2: equivalent models); the matrix
     puts all datasets and all models side by side.
   - "Export" menu: curves (P, q) or the complete Excel workbook.
   - "To Plots" sends the rows selected in the table or, with no selection,
     the displayed dataset and its curves.

4) IAST TAB
   - Each component gets a model: a fit from the previous tab, or parameters
     entered by hand ("Edit...").
   - At first, AdsorpSuite suggests for each gas its fit on a 'total'
     dataset, at the same temperature for all. This is a suggestion to
     check: before the calculation, a warning flags a fit that belongs to
     another gas, an excess isotherm, the same fit used for two components
     or different temperatures.
   - Max P is suggested from the measured range; beyond it, the calculation
     relies on the extrapolation of the models.
   - The reduced spreading pressure pi* = integral of q/P dP is analytical
     for Langmuir, dual-site Langmuir, Freundlich, Sips, D-R and D-A, and
     numerical for Toth. The solver works on a single unknown (pi*), which is
     much more robust than a system of N equations.
   - Two modes: total pressure sweep, or composition sweep at fixed pressure.
   - Outputs: P0_i, x_i, q_i, q_total, selectivities S_i/j, and the
     pure-component amount at the same partial pressure (reference).
   - Warning: the D-R and D-A models have a zero Henry constant; IAST is
     thermodynamically questionable with them at very low pressure.
   - EXTRAPOLATION CHECK: to compute a mixture at P_total, IAST needs the
     pure-component isotherms up to P0_i, often far beyond the measured
     pressure (typically x5 for a weakly adsorbed component such as H2 at
     60 bar). Columns "P0/P_exp_i" and "Max extrapolation" give this ratio;
     the rows concerned are highlighted (orange above 1, red above 2) and the
     corresponding area is shaded on the plot. Above 2, the result depends
     mostly on the chosen model, not on the measurements.
   - Preset mixtures (drop-down list): CO2/CH4, CO2/N2 15:85, CO2/H2,
     CH4/N2, CH4/H2, C2H2/CO2, C2H2/C2H4 1:99, C2H4/C2H6, C3H6/C3H8,
     Xe/Kr 20:80 and the CO2/CH4/H2 ternary.
   - The IAST results agree with pyIAST (internal check).

5) ISOSTERIC HEAT TAB
   - Choose a gas, then isotherms of one material measured at several
     temperatures (two at least, three or more recommended).
   - Clausius-Clapeyron: for each adsorbed amount n, the pressure at each
     temperature comes from the fitted model (Fitting tab), then
     Qst = -R d(ln f)/d(1/T). Only amounts measured at ALL temperatures are
     used: no extrapolation. With three temperatures or more, a standard
     uncertainty is given for each n.
   - Virial: ln P = ln n + (1/T) sum a_i n^i + sum b_j n^j, fitted to all the
     measured points; Qst(n) = -R sum a_i n^i and Qst0 at zero coverage.
     Meant for low-pressure isotherms: limit the points with
     "Max P for virial". Degrees chosen by AICc when left empty.
   - Fugacity basis (default): exact at high pressure; pressure basis:
     ideal-gas assumption. The fugacity coefficient comes from the chosen
     equation of state (CoolProp, NIST table or Peng-Robinson).
   - At high pressure, use total (absolute) isotherms rather than excess.
   - Qst is positive; the adsorption enthalpy is -Qst.

6) PLOTS TAB
   - The "Add" button puts on the plot all the datasets, the dataset and
     curves of the Fitting tab, the last IAST calculation or the isosteric
     heat. The "To Plots" button of the other tabs does the same.
   - Colour, marker, line style, width, opacity, secondary Y axis, bounds,
     log scales, legend, annotations: everything can be changed.
   - Export to PNG / PDF / SVG / EPS / TIFF / JPEG at the chosen resolution,
     and Excel export of the plotted data.

7) SESSION / EXPORT TAB
   - "Save the session" writes ONE .adsp file holding everything: datasets,
     fits and their statistics, IAST components and results, isosteric heat,
     series and plot formatting, annotations. Reopen it to get the whole
     work back, including on another computer. The format is readable JSON,
     and a session saved in French opens in English and vice versa.
   - A .adsp.bak copy of the previous version is kept at every save, and the
     program offers to save before quitting if there are unsaved changes.
   - "Internal check" replays the numerical tests of the program (models,
     spreading pressure, IAST, equation of state, isosteric heat) and shows a
     report. Command line equivalent: AdsorpSuite.exe --selftest
   - Global Excel export: data, fits, curves, IAST, isosteric heat, plot.
   - Origin export: one sheet per result, row 1 = Long Name, row 2 = Units.

LANGUAGE
   - Menu "Langue / Language": French or English. The program restarts to
     apply the change and reopens the current session.

WINDOW AND LOG
   - The "Log" button (bottom right) shows or hides the message history; the
     last message stays visible in the status bar.
   - The window size is remembered from one start to the next.

PLOTS AND READABILITY
   - Under every plot, "Enlarge plot" opens it in a separate, resizable
     window, with zoom, pan and high-resolution export.
   - IAST tab: boxes "loadings / selectivities / x fractions / P0" to choose
     the panels drawn, and "Hide the table" button to give the plots the
     full height.
   - Splitters between panels can be dragged with the mouse; the settings
     columns scroll with the mouse wheel.
   - The size in inches set in the Plots tab only applies to the export: the
     displayed figure adapts to the window.

KEYBOARD SHORTCUTS
   Ctrl+N new session          Ctrl+O open         Ctrl+S save
   Ctrl+Shift+S save as        Ctrl+I import       Ctrl+E Origin export
   Ctrl+1..7 tabs              F1 help
   F5 runs the main action of the current tab
   Shift+F5 processes all datasets (Conversion and Fitting tabs)
   In tables: double-click to edit, Ctrl+V paste, Del delete

UNITS
   P : bar    q : mmol/g    V_pore : cm3/g    rho : mmol/cm3
   E (D-A) : J/mol          K (D-R) : mol2/J2       E = 1/sqrt(K)
   Qst : kJ/mol
""" % (APP_NAME, APP_VERSION)


TR_EN.update({
    'LISEZMOI': 'README',
    'Departs': 'Starts',
    'Tirages bootstrap': 'Bootstrap draws',
    'P exp. max (bar)': 'Max exp. P (bar)',
    'E (energie caract.)': 'E (characteristic energy)',
    'ECHEC': 'FAIL',
    '\n\nEchecs :\n  - ': '\n\nFailures:\n  - ',
    '\n1. Ajustement : recuperation de parametres exacts': '\n1. Fitting: recovery of exact parameters',
    "\n2. Pression d'etalement : formule analytique vs integration": '\n2. Spreading pressure: analytical formula vs integration',
    '\n3. IAST : coherence thermodynamique': '\n3. IAST: thermodynamic consistency',
    "\n4. Equation d'etat et pressions de saturation": '\n4. Equation of state and saturation pressures',
    '\n5. Unites et robustesse': '\n5. Units and robustness',
    '\n6. Robustesse statistique': '\n6. Statistical robustness',
    '\n8. Gaz et chaleur isosterique': '\n8. Gases and isosteric heat',
    '   Contexte   : %s': '   Context    : %s',
    '   Parametres : %s': '   Parameters : %s',
    '   Remarque   : %s': '   Note       : %s',
    '  (modifie)': '  (modified)',
    "  -> parametre le moins bien determine : %s (largeur de l'IC = %.0f %% de la valeur).": '  -> least well determined parameter: %s (CI width = %.0f %% of the value).',
    '  -> |r|max = %.4f : correlation acceptable.': '  -> |r|max = %.4f: acceptable correlation.',
    '  -> |r|max = %.4f : forte correlation, interpretez les parametres avec prudence.': '  -> |r|max = %.4f: strong correlation, interpret the parameters with care.',
    '  -> |r|max = %.4f : parametres quasi indissociables. q_max et b compensent mutuellement ; les valeurs individuelles ne sont pas identifiables de facon fiable, meme avec un R2 excellent.': '  -> |r|max = %.4f: parameters almost inseparable. q_max and b compensate each other; their individual values cannot be identified reliably, even with an excellent R2.',
    '  bootstrap %s : %d / %d': '  bootstrap %s: %d / %d',
    '  Chaque colonne devient une colonne Origin nommee et unitee ;': '  Each column becomes a named Origin column with its unit;',
    '  Courbes_modeles : courbes lissees des ajustements (%d points)': '  Model_curves    : smoothed curves of the fits (%d points)',
    "  File > Import > Excel...  puis dans les options d'import :": '  File > Import > Excel...  then in the import options:',
    '  IAST            : dernier calcul IAST effectue': '  IAST            : last IAST calculation',
    "  il ne reste qu'a designer les colonnes X et Y.": '  you only need to designate the X and Y columns.',
    '  Isothermes      : points experimentaux, un bloc de colonnes par jeu': '  Isotherms       : experimental points, one block of columns per dataset',
    '  ligne 1 : Long Name (nom de colonne Origin)': '  row 1 : Long Name (Origin column name)',
    '  ligne 2 : Units (unite)': '  row 2 : Units',
    '  ligne 3 et suivantes : donnees': '  row 3 onwards : data',
    '  Parametres      : parametres et statistiques de chaque ajustement': '  Parameters      : parameters and statistics of each fit',
    '  Qst             : chaleur isosterique (Clausius-Clapeyron, viriel)': '  Qst             : isosteric heat (Clausius-Clapeyron, virial)',
    ' (copie)': ' (copy)',
    '%.2f %% a 40 bar': '%.2f %% at 40 bar',
    '%d ajustement(s) reussi(s), %d echec(s).': '%d fit(s) succeeded, %d failure(s).',
    '%d fichier(s) lu(s). Verifiez le gaz, la temperature et les unites, puis validez.': '%d file(s) read. Check the gas, temperature and units, then confirm.',
    '%d fichiers CSV ecrits dans :\n%s': '%d CSV files written to:\n%s',
    '%d gaz': '%d gases',
    '%d isotherme(s) importee(s).': '%d isotherm(s) imported.',
    '%d isotherme(s), %d temperature(s) : %s K': '%d isotherm(s), %d temperature(s): %s K',
    "%d jeu(x) 'total' cree(s).": "%d 'total' dataset(s) created.",
    '%d points, colonnes : %s': '%d points, columns: %s',
    '%d tirages, IC q_max = [%.2f ; %.2f]': '%d draws, CI q_max = [%.2f ; %.2f]',
    '%s  (f, P en bar)': '%s  (f, P in bar)',
    '%s %s - export Origin': '%s %s - Origin export',
    "%s v%s\n\nAnalyse d'isothermes d'adsorption : ajustement de modeles, conversion exces/total, IAST binaire et ternaire, graphiques et exports.\n\nPython %s\nnumpy %s - pandas %s - matplotlib %s\nCoolProp : %s\n\nConfiguration : %s": '%s v%s\n\nAdsorption isotherm analysis: model fitting, excess/total conversion, binary and ternary IAST, isosteric heat, plots and exports.\n\nPython %s\nnumpy %s - pandas %s - matplotlib %s\nCoolProp: %s\n\nConfiguration: %s',
    '%s v%s pret.': '%s v%s ready.',
    '(aucune)': '(none)',
    '+ Ligne': '+ Row',
    '- Ligne': '- Row',
    '1. Constituants du melange': '1. Mixture components',
    '1. Isothermes a combiner': '1. Isotherms to combine',
    '1. Jeu de donnees et contexte': '1. Dataset and context',
    '1. Jeu de donnees et methode': '1. Dataset and method',
    '1.5 x P_max (par defaut)': '1.5 x P_max (default)',
    '1/q (poids intermediaire)': '1/q (intermediate weight)',
    '1/q^2 (erreur relative)': '1/q^2 (relative error)',
    '1/q^2 donne le meme poids relatif a tous les points : utile quand les faibles pressions comptent autant que la saturation': '1/q^2 gives the same relative weight to every point: useful when low pressures matter as much as saturation',
    '2. Conditions de calcul': '2. Calculation conditions',
    '2. Modeles a ajuster': '2. Models to fit',
    '2. Options de calcul': '2. Calculation options',
    '2. Parametres': '2. Parameters',
    "3. Options d'ajustement": '3. Fitting options',
    '4. Valeurs initiales et bornes': '4. Initial values and bounds',
    '7. Densites de reference et conversion (v3.0)': '7. Reference densities and conversion (v3.0)',
    '[ECHEC] %s / %s : %s': '[FAILED] %s / %s: %s',
    '[ECHEC] export Origin : %s': '[FAILED] Origin export: %s',
    '_courbes.csv': '_curves.csv',
    'A propos': 'About',
    'absent, Peng-Robinson utilise': 'missing, Peng-Robinson used',
    'Actualiser': 'Refresh',
    'Actualiser le graphique': 'Refresh the plot',
    'Actualiser le resume': 'Refresh the summary',
    'Afficher :': 'Show:',
    'Afficher le tableau': 'Show the table',
    'Agrandir le graphique': 'Enlarge plot',
    'Aide': 'Help',
    'Aide rapide': 'Quick help',
    'Aide rapide (F1)': 'Quick help (F1)',
    "Ajoute le resultat comme nouveau jeu de donnees, utilisable pour l'ajustement": 'Adds the result as a new dataset, ready for fitting',
    'Ajouter une ligne vide': 'Add an empty row',
    'Ajustement': 'Fitting',
    'Ajustement %d / %d  -  %s / %s': 'Fit %d / %d  -  %s / %s',
    'Ajustement %s (%d departs, %d tirages bootstrap)...': 'Fitting %s (%d starts, %d bootstrap draws)...',
    "Ajustement : %d reussi(s), %d echec(s) sur '%s'.": "Fitting: %d succeeded, %d failure(s) on '%s'.",
    'ajustement du viriel': 'virial fit',
    'Ajustement en lot': 'Batch fit',
    'Ajustement en lot : %d reussi(s), %d echec(s).': 'Batch fit: %d succeeded, %d failure(s).',
    'Ajustement en lot termine.': 'Batch fit finished.',
    'Ajustement selectionne (%d)': 'Selected fit (%d)',
    'Ajustements': 'Fits',
    'AJUSTEMENTS (%d)': 'FITS (%d)',
    'Ajustements uniquement': 'Fits only',
    'ajustements.xlsx': 'fits.xlsx',
    'Ajuster': 'Fit',
    'Ajuster les modeles coches': 'Fit the ticked models',
    'Ajuster TOUS les jeux x TOUS les modeles coches': 'Fit ALL datasets x ALL ticked models',
    'Aller a': 'Go to',
    "Aller a l'ajustement et lancer les modeles coches": 'Go to fitting and run the ticked models',
    'Aller au calcul de melange et le lancer': 'Go to the mixture calculation and run it',
    "aller-retour d'unites cm3(STP)/g": 'cm3(STP)/g unit round trip',
    'analytique': 'analytical',
    'Annuler': 'Cancel',
    'Apercu': 'Preview',
    "Applique la meme methode et les memes parametres a chaque jeu de type 'Exces' et cree en une fois tous les jeux 'total' correspondants.": "Applies the same method and parameters to every 'Excess' dataset and creates all the matching 'total' datasets at once.",
    'Applique tous les reglages ci-dessus (F5)': 'Applies all the settings above (F5)',
    'Appliquer': 'Apply',
    'Appliquer a tous  -  T (K) :': 'Apply to all  -  T (K):',
    'Appliquer le style': 'Apply the style',
    'ATTENTION : ': 'WARNING: ',
    'ATTENTION : au moins un controle a echoue, voir le detail.': 'WARNING: at least one check failed, see the details.',
    'Aucun': 'None',
    'aucun ajustement': 'no fit',
    'Aucun ajustement a exporter.': 'No fit to export.',
    'Aucun ajustement dans cette selection.': 'No fit in this selection.',
    'Aucun ajustement disponible.': 'No fit available.',
    'Aucun ajustement pour ce jeu.': 'No fit for this dataset.',
    'Aucun ajustement.': 'No fit.',
    'aucun calcul': 'no calculation',
    'aucun calcul de chaleur isosterique': 'no isosteric heat calculation',
    "aucun calcul IAST - lancez d'abord l'onglet IAST": 'no IAST calculation - run the IAST tab first',
    "aucun depart n'a converge (%d essais)": 'no start converged (%d attempts)',
    'aucun jeu de donnees': 'no dataset',
    'Aucun jeu de donnees.': 'No dataset.',
    "Aucun jeu de type 'Exces' a convertir.": "No 'Excess' dataset to convert.",
    'Aucun point exploitable pour le viriel.': 'No usable point for the virial fit.',
    'Aucune (moindres carres)': 'None (least squares)',
    'Aucune donnee numerique valide dans le tableau.': 'No valid numeric data in the table.',
    'Aucune donnee.': 'No data.',
    'aucune paire de colonnes numeriques': 'no pair of numeric columns',
    'aucune paire de colonnes numeriques (feuille %s)': 'no pair of numeric columns (sheet %s)',
    'Aucune serie affichee.': 'No series displayed.',
    'Axe X :': 'X axis:',
    'Axe Y :': 'Y axis:',
    'Axe Y2 :': 'Y2 axis:',
    'Axes et mise en forme': 'Axes and layout',
    'Balayage en composition (y1)': 'Composition sweep (y1)',
    'Balayage en pression totale': 'Total pressure sweep',
    'Base :': 'Basis:',
    'base des gaz complete (Tc, Pc, w, M)': 'complete gas database (Tc, Pc, w, M)',
    'biogaz, gaz naturel': 'biogas, natural gas',
    'Bootstrap IC 95 %, tirages :': 'Bootstrap 95 % CI, draws:',
    'Borne basse du balayage en pression': 'Lower bound of the pressure sweep',
    "Borne haute. Au-dela de la pression mesuree, le calcul repose sur l'extrapolation du modele.": 'Upper bound. Beyond the measured pressure, the result relies on model extrapolation.',
    "Boucle sur l'ensemble des jeux de donnees et lance les modeles coches sur chacun. Une barre de progression indique l'avancement (Maj+F5).": 'Loops over all datasets and runs the ticked models on each one. A progress bar shows the progress (Shift+F5).',
    'Calcule rho_gaz(T,P) et n_total pour chaque point': 'Computes rho_gas(T,P) and n_total for each point',
    'Calculer la chaleur isosterique': 'Compute the isosteric heat',
    'Calculer la conversion': 'Compute the conversion',
    'CH4 supercritique -> regle de Dubinin': 'supercritical CH4 -> Dubinin rule',
    'Chaleur isosterique': 'Isosteric heat',
    'Chaleur isosterique a partir de plusieurs temperatures': 'Isosteric heat from several temperatures',
    'chaleur isosterique en fonction de la quantite adsorbee': 'isosteric heat versus adsorbed amount',
    'chaleur_isosterique_%s.xlsx': 'isosteric_heat_%s.xlsx',
    'chaque constituant recoit un modele de corps pur': 'each component gets a pure-component model',
    'Choisir la couleur de la serie': 'Choose the series colour',
    'Classement': 'Ranking',
    'Classement des modeles': 'Model ranking',
    'Classement des modeles (AIC)': 'Model ranking (AIC)',
    "Classement des modeles pour '%s'": "Model ranking for '%s'",
    'Classeur au format attendu par Origin : ligne 1 = Long Name, ligne 2 = Units, donnees ligne 3. Une colonne par courbe.': 'Workbook in the layout Origin expects: row 1 = Long Name, row 2 = Units, data from row 3. One column per curve.',
    'Classeur complet : donnees, ajustements, courbes, IAST': 'Complete workbook: data, fits, curves, IAST',
    'Classeur Excel': 'Excel workbook',
    'Clausius-Clapeyron (%d isothermes, %s) : Qst de %s a %s kJ/mol pour n = %s-%s mmol/g.': 'Clausius-Clapeyron (%d isotherms, %s): Qst from %s to %s kJ/mol for n = %s-%s mmol/g.',
    'Clausius-Clapeyron (modeles ajustes)': 'Clausius-Clapeyron (fitted models)',
    'Clausius-Clapeyron : isosteres calculees avec les modeles ajustes, sans sortir des quantites mesurees.\nViriel : une seule equation ajustee sur tous les points ; adaptee aux isothermes de basse pression, donne Qst a recouvrement nul.': 'Clausius-Clapeyron: isosteres computed from the fitted models, without leaving the measured loadings.\nVirial: a single equation fitted to all points; suited to low-pressure isotherms, gives Qst at zero coverage.',
    'Clausius-Clapeyron demande des isothermes ajustees a au moins deux temperatures (onglet Ajustement).': 'Clausius-Clapeyron needs fitted isotherms at two temperatures or more (Fitting tab).',
    'clic sur la case pour afficher ou masquer': 'click the box to show or hide',
    'CO2 au-dela de Psat(303 K) : hors table': 'CO2 above Psat(303 K): outside the table',
    'Cochez au moins un modele.': 'Tick at least one model.',
    'cochez dans la colonne de gauche': 'tick in the left column',
    'Coller': 'Paste',
    'Coller deux colonnes depuis le presse-papiers': 'Paste two columns from the clipboard',
    'Colonne pression :': 'Pressure column:',
    'Colonne quantite :': 'Loading column:',
    'Commentaire': 'Comment',
    'Commentaire :': 'Comment:',
    'Comparaison exces / total': 'Excess / total comparison',
    'composition de la phase adsorbee': 'composition of the adsorbed phase',
    "Configure les constituants et leurs fractions molaires, puis associe automatiquement l'ajustement disponible pour chaque gaz.": 'Sets the components and their mole fractions, then automatically links the available fit for each gas.',
    "Constante de Henry nulle => prudence avec l'IAST.": 'Zero Henry constant => use IAST with care.',
    'Constituant': 'Component',
    'Constituant %d :': 'Component %d:',
    'Constituant %d : aucun modele defini (choisissez un ajustement ou saisissez les parametres).': 'Component %d: no model defined (choose a fit or enter the parameters).',
    'Contexte       : T = %s K, P0 = %s bar': 'Context        : T = %s K, P0 = %s bar',
    "Conversion effectuee (%s, %s) sur '%s'.": "Conversion done (%s, %s) on '%s'.",
    'Conversion en lot': 'Batch conversion',
    'Conversion en lot : %d jeu(x) cree(s), %d echec(s).': 'Batch conversion: %d dataset(s) created, %d failure(s).',
    'conversion exces -> total croissante avec P': 'excess -> total conversion increases with P',
    'conversion exces -> total via la table NIST': 'excess -> total conversion with the NIST table',
    "converti de '%s' : %s, V_pore=%s cm3/g, EOS=%s": "converted from '%s': %s, V_pore=%s cm3/g, EOS=%s",
    "Converti par '%s' (%s)": "Converted by '%s' (%s)",
    "Convertir %d jeu(x) en quantite totale ?\n\n  methode  : %s\n  EOS      : %s\n  V_pore   : %s cm3/g\n\nLes jeux 'total' deja presents portant le meme nom seront remplaces.": "Convert %d dataset(s) to total amount?\n\n  method   : %s\n  EOS      : %s\n  V_pore   : %s cm3/g\n\nExisting 'total' datasets with the same name will be replaced.",
    'Convertir TOUS les jeux en exces': 'Convert ALL excess datasets',
    "CoolProp %s. Astuce : F1 ouvre l'aide, F5 lance l'action de l'onglet courant.": 'CoolProp %s. Tip: F1 opens the help, F5 runs the action of the current tab.',
    'Copier le jeu selectionne': 'Copy the selected dataset',
    'Correction appliquee': 'Applied correction',
    'correlation de Lee-Kesler': 'Lee-Kesler correlation',
    'correlation des parametres calculee': 'parameter correlation computed',
    'Couleur': 'Colour',
    'Courbe lissee et points experimentaux en .xlsx ou .csv': 'Smoothed curve and experimental points as .xlsx or .csv',
    'Courbes ajustees': 'Fitted curves',
    'courbes_ajustement.xlsx': 'fit_curves.xlsx',
    'Courbes_modeles': 'Model_curves',
    "Creer un jeu 'total'": "Create a 'total' dataset",
    'Creer un jeu vide et saisir ou coller les valeurs a la main': 'Create an empty dataset and type or paste the values by hand',
    'dAIC < 2 : modeles equivalents.': 'dAIC < 2 : equivalent models.',
    'dAIC = 0 : meilleur compromis qualite / nombre de parametres.': 'dAIC = 0 : best balance between fit quality and number of parameters.',
    'dAIC > 10 : modele nettement moins bon.': 'dAIC > 10 : clearly worse model.',
    "deduction de l'echantillon depuis le nom de fichier": 'sample detected from the file name',
    'deduction du gaz depuis le nom de fichier': 'gas detected from the file name',
    'Degre a (viriel) :': 'Degree of a (virial):',
    'Degre b (viriel) :': 'Degree of b (virial):',
    'Densite adsorbee': 'Adsorbed density',
    'Densite de phase adsorbee invalide.': 'Invalid adsorbed-phase density.',
    "Densite du liquide au point d'ebullition normal pour ce gaz": 'Liquid density at the normal boiling point for this gas',
    'Densite fournie': 'Supplied density',
    'densites de reference %s': 'reference densities %s',
    'Derniere session : %s  (menu Fichier pour la rouvrir)': 'Last session: %s  (File menu to reopen it)',
    'Descendre': 'Move down',
    "Details de l'ajustement": 'Fit details',
    'detecte': 'detected',
    "detection de l'extrapolation des modeles": 'detection of model extrapolation',
    "Determine la masse molaire, Tc, Pc et l'acentricite": 'Sets the molar mass, Tc, Pc and acentric factor',
    'Deux temperatures seulement : Qst sans incertitude (au moins trois conseillees).': 'Only two temperatures: Qst without uncertainty (three or more recommended).',
    'domaine sur': 'safe range',
    'Domaine valide : tous les P0 restent dans la gamme mesuree (max x%.2f).': 'Valid range: all P0 stay within the measured range (max x%.2f).',
    'Donne toute la largeur aux graphiques': 'Gives the full width to the plots',
    'Donnees': 'Data',
    'Donnees : %s': 'Data: %s',
    'Donnees du graphique exportees : %s': 'Plot data exported: %s',
    'Donnees enregistrees :\n%s': 'Data saved:\n%s',
    'Donnees experimentales': 'Experimental data',
    'Donnees, ajustements, courbes, IAST et graphique dans un seul classeur': 'Data, fits, curves, IAST and plot in a single workbook',
    'donnees_graphique.xlsx': 'plot_data.xlsx',
    'Dossier de destination': 'Destination folder',
    'double-clic pour editer  -  Ctrl+V pour coller depuis Excel': 'double-click to edit  -  Ctrl+V to paste from Excel',
    "Double-clic sur 'Nom du jeu', 'Gaz' ou 'T (K)' pour corriger une ligne.": "Double-click 'Dataset name', 'Gas' or 'T (K)' to correct a row.",
    'double-clic sur une ligne pour le detail complet': 'double-click a row for full details',
    'DPI export :': 'Export DPI:',
    'du modele surligne ci-dessus': 'of the model highlighted above',
    'Dubinin-Astakhov (P0 ajuste)': 'Dubinin-Astakhov (fitted P0)',
    'Dubinin-Astakhov (P0 fixe)': 'Dubinin-Astakhov (fixed P0)',
    'Dubinin-Radushkevich (P0 ajuste)': 'Dubinin-Radushkevich (fitted P0)',
    'Dubinin-Radushkevich (P0 fixe)': 'Dubinin-Radushkevich (fixed P0)',
    'Dupliquer': 'Duplicate',
    'Ecart (%)': 'Deviation (%)',
    'Ecart de temperature inferieur a 10 K : Qst sera tres sensible au bruit de mesure.': 'Temperature span below 10 K: Qst will be very sensitive to measurement noise.',
    'ecart max %.1e kJ/mol': 'max deviation %.1e kJ/mol',
    'Ecart maximal exces/total : %s mmol/g  -  %s': 'Maximum excess/total gap: %s mmol/g  -  %s',
    'ecart Peng-Robinson / NIST sur CH4 inferieur a 3 %': 'Peng-Robinson / NIST deviation on CH4 below 3 %',
    'ecart pi max=%.1e   |somme x - 1|=%.1e': 'max pi deviation=%.1e   |sum x - 1|=%.1e',
    'ecart relatif max=%.1e': 'max relative deviation=%.1e',
    'Ecart-type': 'Std. deviation',
    'ecart-type': 'std. dev.',
    'Echec du solveur : %s': 'Solver failure: %s',
    'Echelle logarithmique en pression': 'Logarithmic pressure scale',
    "Ecrit un fichier .adsp contenant l'integralite du travail (Ctrl+S)": 'Writes one .adsp file holding the whole work (Ctrl+S)',
    'Editer...': 'Edit...',
    'Effacer': 'Clear',
    'Effacer le filtre': 'Clear the filter',
    'Effacer tous les ajustements': 'Delete all fits',
    'Effacer tout le tableau': 'Clear the whole table',
    "Encadrement de la pression d'etalement impossible.": 'Could not bracket the spreading pressure.',
    'Enregistre le tableau de conversion': 'Saves the conversion table',
    'Enregistrement impossible :\n%s': 'Cannot save:\n%s',
    'Enregistrer': 'Save',
    "Enregistrer l'image...": 'Save image...',
    'Enregistrer la session': 'Save the session',
    'Enregistrer la session...': 'Save the session...',
    'Enregistrer le jeu de donnees': 'Save the dataset',
    'Enregistrer le jeu de donnees  (Ctrl+S)': 'Save the dataset  (Ctrl+S)',
    'Enregistrer sous un nouveau nom...': 'Save under a new name...',
    'Enregistrer sous...': 'Save as...',
    'Enregistrer toute la session dans un fichier .adsp (Ctrl+S)': 'Save the whole session in one .adsp file (Ctrl+S)',
    "Envoyer donnees et courbes vers l'onglet Graphiques": 'Send data and curves to the Plots tab',
    'Epaisseur du trait': 'Line width',
    "Equation d'etat :": 'Equation of state:',
    'Estimer P0 automatiquement': 'Estimate P0 automatically',
    'Etat quasi-critique (Tr=%.2f, Pr=%.2f) : l\'ecart de Peng-Robinson sur la densite peut atteindre 10 a 25 %%. Utilisez CoolProp (pip install CoolProp) ou la methode "Densite fournie" avec des valeurs NIST/REFPROP.': 'Near-critical state (Tr=%.2f, Pr=%.2f): the Peng-Robinson density error can reach 10 to 25 %%. Use CoolProp (pip install CoolProp) or the "Supplied density" method with NIST/REFPROP values.',
    'Exces': 'Excess',
    'Export : %s': 'Export: %s',
    'Export : largeur x hauteur (pouces) :': 'Export: width x height (inches):',
    'Export chaleur isosterique : %s': 'Isosteric heat export: %s',
    'Export des ajustements : %s': 'Fit export: %s',
    'Export des courbes ajustees (%d ajustement(s)) : %s': 'Export of fitted curves (%d fit(s)): %s',
    'Export Excel': 'Excel export',
    'Export Excel global': 'Global Excel export',
    'Export Excel global...': 'Global Excel export...',
    'Export global : %s': 'Global export: %s',
    'Export IAST : %s': 'IAST export: %s',
    'Export Origin': 'Origin export',
    'Export Origin (large, Long Name + Units)': 'Origin export (wide, Long Name + Units)',
    'Export Origin (Long Name + Units)...': 'Origin export (Long Name + Units)...',
    'Export Origin : %s': 'Origin export: %s',
    'Export Origin ecrit.': 'Origin export written.',
    'export_origin.xlsx': 'origin_export.xlsx',
    'Exporter en Excel': 'Export to Excel',
    "Exporter l'image...": 'Export image...',
    'Exporter les courbes (P, q)...': 'Export curves (P, q)...',
    "Exporter les donnees d'ajustement": 'Export fit data',
    'Exporter les donnees tracees...': 'Export plotted data...',
    'Exporter tout en Excel': 'Export all to Excel',
    'Exporter...': 'Export...',
    "EXTRAPOLATION : les P0 requis depassent jusqu'a x%.1f la pression mesuree (%s) sur %d point(s). Ces points reposent sur l'extrapolation des isothermes de corps purs, pas sur des mesures.": 'EXTRAPOLATION: the required P0 reach up to x%.1f the measured pressure (%s) on %d point(s). These points rely on extrapolating the pure-component isotherms, not on measurements.',
    'Extrapolation courbe (x P_max) :': 'Curve extrapolation (x P_max):',
    'Extrapolation legere : P0 max = x%.1f la pression mesuree (%s).': 'Slight extrapolation: max P0 = x%.1f the measured pressure (%s).',
    'Extrapolation max (P0/P_exp)': 'Max extrapolation (P0/P_exp)',
    'Feuille': 'Sheet',
    'Feuille :': 'Sheet:',
    'Fichier': 'File',
    'Fichier ecrit :\n%s\n\nDans Origin : File > Import > Excel, avec Long Names = 1, Units = 2, Data begins on = 3.': 'File written:\n%s\n\nIn Origin: File > Import > Excel, with Long Names = 1, Units = 2, Data begins on = 3.',
    'Fichier enregistre :\n%s': 'File saved:\n%s',
    'Fichier enregistre :\n%s\n\nFeuilles : Parametres / Courbes ajustees / Residus': 'File saved:\n%s\n\nSheets: Parameters / Fitted curves / Residuals',
    'Fichier(s) ignore(s) :\n  - ': 'Skipped file(s):\n  - ',
    'Figure enregistree :\n%s': 'Figure saved:\n%s',
    'Figure exportee : %s': 'Figure exported: %s',
    'Filtrer :': 'Filter:',
    'Fraction adsorbee x': 'Adsorbed fraction x',
    'Fraction molaire gazeuse y_%s': 'Gas-phase mole fraction y_%s',
    'Fraction molaire y': 'Mole fraction y',
    "Fractions molaires configurees.\n\nAucun ajustement disponible pour : %s.\nAjustez d'abord ces isothermes dans l'onglet Ajustement, ou saisissez les parametres a la main (bouton 'Editer...').": "Mole fractions set.\n\nNo fit available for: %s.\nFit these isotherms first in the Fitting tab, or enter the parameters by hand ('Edit...' button).",
    'fractions x': 'x fractions',
    'Fugacite (gaz reel)': 'Fugacity (real gas)',
    'Fugacite : exacte a haute pression (gaz reel). Pression : hypothese du gaz parfait, suffisante a basse pression.': 'Fugacity: exact at high pressure (real gas). Pressure: ideal-gas assumption, adequate at low pressure.',
    'fugacite : integration numerique = formule de Peng-Robinson': 'fugacity: numerical integration = Peng-Robinson formula',
    'fumees de combustion': 'flue gas',
    'Gamme de pression invalide.': 'Invalid pressure range.',
    'Gaz': 'Gas',
    'Gaz :': 'Gas:',
    "Gaz : %s ; base : %s ; equation d'etat : %s": 'Gas: %s; basis: %s; equation of state: %s',
    "gaz et temperature servent aux modeles D-R / D-A et a l'IAST": 'gas and temperature are used by the D-R / D-A models and by IAST',
    'gaz inconnu': 'unknown gas',
    'gaz naturel, grisou': 'natural gas, coal-mine methane',
    'Gaz parfait': 'Ideal gas',
    'gaz rares (retraitement nucleaire)': 'noble gases (nuclear reprocessing)',
    'genere le %d/%m/%Y a %H:%M': 'generated on %Y-%m-%d at %H:%M',
    'Grandeurs derivees :': 'Derived quantities:',
    'Graphique': 'Plot',
    'Graphiques': 'Plots',
    'Grille': 'Grid',
    'hors domaine de la correlation': 'outside the range of the correlation',
    'IAST : %d points calcules, %d non convergents.': 'IAST: %d points calculated, %d not converged.',
    'IAST : %s': 'IAST: %s',
    'Import : %s (%d points)': 'Import: %s (%d points)',
    'IMPORT DANS ORIGIN': 'IMPORT INTO ORIGIN',
    'Import de donnees - %s': 'Data import - %s',
    'Import en lot': 'Batch import',
    'Import en lot - verifier avant de valider': 'Batch import - check before confirming',
    'Import en lot : %d jeu(x) ajoute(s).': 'Batch import: %d dataset(s) added.',
    'Importe de %s': 'Imported from %s',
    'importe de %s (feuille %s, colonnes %s)': 'imported from %s (sheet %s, columns %s)',
    'Importer': 'Import',
    'Importer des donnees': 'Import data',
    "Importer des donnees d'isotherme": 'Import isotherm data',
    'Importer plusieurs isothermes': 'Import several isotherms',
    'Importer plusieurs isothermes...': 'Import several isotherms...',
    'Importer un dossier / plusieurs fichiers...': 'Import a folder / several files...',
    'Importer un fichier...': 'Import a file...',
    'Inclure les points experimentaux, la valeur calculee et le residu': 'Include the experimental points, the calculated value and the residual',
    'Inclure une feuille avec les parametres et les statistiques': 'Include a sheet with the parameters and statistics',
    'Informations': 'Information',
    'installe': 'installed',
    'integration numerique': 'numerical integration',
    'Intervalles de confiance a 95 %% par bootstrap (%d tirages retenus) :': '95 %% bootstrap confidence intervals (%d draws kept):',
    'Isotherme et residus': 'Isotherm and residuals',
    'Isothermes': 'Isotherms',
    "Isothermes en exces jusqu'a %s bar : a haute pression, utilisez les quantites totales (onglet Conversion).": 'Excess isotherms up to %s bar: at high pressure, use total amounts (Conversion tab).',
    'Jeu': 'Dataset',
    'Jeu %d': 'Dataset %d',
    "Jeu '%s' ajoute (%d points).\n\nAller a l'onglet Donnees pour le voir ?": "Dataset '%s' added (%d points).\n\nGo to the Data tab to see it?",
    'Jeu de donnees': 'Dataset',
    'Jeu de donnees :': 'Dataset:',
    'Jeu de donnees : %s': 'Dataset        : %s',
    'Jeu de donnees enregistre : %s (%d points)': 'Dataset saved: %s (%d points)',
    'Jeu importe': 'Imported dataset',
    'Jeux de donnees': 'Datasets',
    'JEUX DE DONNEES (%d)': 'DATASETS (%d)',
    'Journal  -  afficher': 'Log  -  show',
    'Journal  -  masquer': 'Log  -  hide',
    'La courbe lissee est echantillonnee entre P min et P max.\nLaisser vide pour utiliser la gamme des donnees experimentales.': 'The smoothed curve is sampled between P min and P max.\nLeave empty to use the range of the experimental data.',
    "La session en cours contient des modifications non enregistrees.\n\nVoulez-vous l'enregistrer maintenant ?": 'The current session has unsaved changes.\n\nDo you want to save it now?',
    "La verification interne rejoue les tests numeriques (modeles, IAST, equation d'etat) et affiche un rapport.": 'The internal check replays the numerical tests (models, IAST, equation of state) and shows a report.',
    "Lance l'ajustement non lineaire sur le jeu selectionne (F5)": 'Runs the non-linear fit on the selected dataset (F5)',
    'Lancer %d ajustement(s) (%d jeux x %d modeles) ?\n\nLes ajustements existants portant le meme couple jeu / modele seront remplaces.': 'Run %d fit(s) (%d datasets x %d models)?\n\nExisting fits with the same dataset / model pair will be replaced.',
    'Lancer le calcul IAST': 'Run the IAST calculation',
    "Lancez d'abord le calcul.": 'Run the calculation first.',
    "Lancez d'abord un calcul.": 'Run a calculation first.',
    'Langmuir bi-site (DSL)': 'Dual-site Langmuir (DSL)',
    "Le fichier .adsp est du texte JSON : il se copie d'un PC a l'autre, se sauvegarde et reste lisible. Une copie .adsp.bak de la version precedente est conservee a chaque enregistrement.": 'The .adsp file is JSON text: it can be copied from one PC to another, backed up, and stays readable. A .adsp.bak copy of the previous version is kept at every save.',
    'Le modele retenu par jeu (AICc minimal) est marque <<.': 'The model retained for each dataset (lowest AICc) is marked <<.',
    'Le noyau scientifique se comporte comme attendu.': 'The scientific core behaves as expected.',
    'Le viriel demande des isothermes a au moins deux temperatures.': 'The virial method needs isotherms at two temperatures or more.',
    'lecture de nombres a virgule decimale': 'reading numbers with a decimal comma',
    'Lecture impossible :\n%s': 'Cannot read:\n%s',
    'Lecture impossible :\n%s\n\n%s': 'Cannot read:\n%s\n\n%s',
    'Lee-Kesler si T < Tc, regle de Dubinin Pc(T/Tc)^2 si T > Tc': 'Lee-Kesler if T < Tc, Dubinin rule Pc(T/Tc)^2 if T > Tc',
    'Legende': 'Legend',
    'Legende :': 'Legend:',
    "Les colonnes vides en bas d'un bloc sont normales : les jeux n'ont pas": 'Empty cells at the bottom of a block are normal: datasets do not all',
    'Les deux methodes': 'Both methods',
    "Les isothermes n'ont aucune quantite adsorbee en commun : impossible de construire des isosteres.": 'The isotherms share no common adsorbed amount: isosteres cannot be built.',
    'ligne': 'line',
    'limite basse pression -> constantes de Henry': 'low-pressure limit -> Henry constants',
    'Lire un .xlsx, .xls ou .csv et choisir la feuille, les colonnes et les unites': 'Read an .xlsx, .xls or .csv file and choose the sheet, columns and units',
    "Lire un fichier Excel ou CSV d'isotherme": 'Read an isotherm from an Excel or CSV file',
    'ln f contre 1/T a quantite constante : des droites attendues': 'ln f versus 1/T at constant loading: straight lines expected',
    'Logiciel': 'Software',
    'Maj+F5 : disponible dans les onglets Conversion et Ajustement.': 'Shift+F5: available in the Conversion and Fitting tabs.',
    'Marqueur': 'Marker',
    'Marqueur / ligne :': 'Marker / line:',
    'Masquer le tableau': 'Hide the table',
    'Matrice': 'Matrix',
    'MATRICE DE COMPARAISON DES MODELES': 'MODEL COMPARISON MATRIX',
    'Matrice de comparaison des modeles': 'Model comparison matrix',
    'Matrice de correlation des parametres :': 'Parameter correlation matrix:',
    'Meilleur AICc par isotherme': 'Best AICc for each isotherm',
    'Melange %s pret - lancez le calcul IAST.': 'Mixture %s ready - run the IAST calculation.',
    "Melange d'isothermes en exces et totales : selectionnez un seul type.": 'Mix of excess and total isotherms: select a single type.',
    'melange Toth+Sips+D-A : pi identiques et somme x = 1': 'Toth+Sips+D-A mixture: equal pi and sum x = 1',
    'Melange type': 'Preset mixture',
    'Melange type applique : %s': 'Preset mixture applied: %s',
    'Melanges types :': 'Preset mixtures:',
    'Metadonnees': 'Metadata',
    'Methode': 'Method',
    'Methode :': 'Method:',
    'Mode :': 'Mode:',
    'Modele': 'Model',
    'Modele         : %s': 'Model          : %s',
    'Modele :': 'Model:',
    "Modele de remplissage de micropores : constante de Henry nulle => usage de l'IAST a tres basse pression a eviter.": 'Micropore-filling model: zero Henry constant => avoid using IAST at very low pressure.',
    'Modele utilise pour Clausius-Clapeyron. Le meme modele a toutes les temperatures est le choix le plus coherent.': 'Model used for Clausius-Clapeyron. Using the same model at every temperature is the most consistent choice.',
    'Modeles': 'Models',
    'Modeles %s : constante de Henry nulle ou non definie, IAST discutable a tres basse pression.': 'Models %s: zero or undefined Henry constant, IAST questionable at very low pressure.',
    'MODELES DISPONIBLES': 'AVAILABLE MODELS',
    'Modeles et equations': 'Models and equations',
    "molette et barre d'outils pour zoomer  -  bouton Agrandir pour une fenetre dediee": 'mouse wheel and toolbar to zoom  -  Enlarge button for a dedicated window',
    'Monter': 'Move up',
    'Multi-depart : %d essais, %d convergents.': 'Multi-start: %d attempts, %d converged.',
    'multi-depart et bootstrap operationnels': 'multi-start and bootstrap working',
    "multi-depart jamais moins bon qu'un depart unique": 'multi-start never worse than a single start',
    'Multi-depart, essais :': 'Multi-start, attempts:',
    'n viriel': 'n virial',
    'n_exces (mmol/g)': 'n_excess (mmol/g)',
    'n_tot = %.4f puis %.4f mmol/g': 'n_tot = %.4f then %.4f mmol/g',
    'Nb isothermes': 'No. of isotherms',
    'Nom :': 'Name:',
    'Nom affiche dans tous les onglets': 'Name shown in every tab',
    'Nom du jeu': 'Dataset name',
    'Nom du jeu :': 'Dataset name:',
    'Nombre de constituants :': 'Number of components:',
    'Nombre de points :': 'Number of points:',
    'Nombre de points calcules': 'Number of calculated points',
    'Nombre de quantites adsorbees calculees': 'Number of loadings calculated',
    'non installe': 'not installed',
    'non renseignee': 'not set',
    'Normaliser les fractions molaires': 'Normalise the mole fractions',
    "Note libre : origine de l'echantillon, appareil...": 'Free note: sample origin, instrument...',
    'Nouveau jeu cree : %s (%d points)': 'New dataset created: %s (%d points)',
    'Nouveau jeu vide': 'New empty dataset',
    'Nouvelle session': 'New session',
    'Nouvelle session.': 'New session.',
    'olefine / paraffine': 'olefin / paraffin',
    'Opacite entre 0 et 1': 'Opacity between 0 and 1',
    'orange : P0 au-dela du domaine mesure  -  rouge : au-dela du double': 'orange: P0 beyond the measured range  -  red: beyond twice that range',
    'Ouvre le graphique dans une fenetre separee et redimensionnable, avec zoom, deplacement et export haute resolution': 'Opens the plot in a separate resizable window, with zoom, pan and high-resolution export',
    'Ouvrir une session': 'Open a session',
    'Ouvrir une session...': 'Open a session...',
    'Ouvrir...': 'Open...',
    'P experimentale max (bar) :': 'Max experimental P (bar):',
    'P experimentale max non renseignee pour : %s (extrapolation non controlee).': 'Maximum experimental P not set for: %s (extrapolation not checked).',
    'P fixe pour balayage en y (bar) :': 'Fixed P for the y sweep (bar):',
    'P max (bar) :': 'P max (bar):',
    'P max viriel (bar) :': 'Max P for virial (bar):',
    'P min (bar) :': 'P min (bar):',
    'P0 (bar) :': 'P0 (bar):',
    'P0 max = %.1f x la pression mesuree a 60 bar': 'P0 max = %.1f x the measured pressure at 60 bar',
    'P_sat(CO2, 298.15 K) proche de 64.2 bar': 'P_sat(CO2, 298.15 K) close to 64.2 bar',
    'Parametre': 'Parameter',
    'Parametres': 'Parameters',
    'Parametres du constituant': 'Component parameters',
    'Parametres, courbes et residus de tous les ajustements': 'Parameters, curves and residuals of all fits',
    'Parametres, IC, matrice de correlation et statistiques': 'Parameters, CI, correlation matrix and statistics',
    'Pas assez de points valides (%d) pour %d parametres.': 'Not enough valid points (%d) for %d parameters.',
    "pas d'ajustement": 'no fit',
    'Pas de limite de saturation ; IAST valable seulement si n_F < 1 et loin de la saturation.': 'No saturation limit; IAST valid only if n_F < 1 and far from saturation.',
    'PDF vectoriel': 'Vector PDF',
    "Plusieurs isothermes a la meme temperature : verifiez qu'elles decrivent bien le meme materiau.": 'Several isotherms at the same temperature: check that they describe the same material.',
    'PNG, PDF, SVG, EPS, TIFF ou JPEG a la resolution choisie': 'PNG, PDF, SVG, EPS, TIFF or JPEG at the chosen resolution',
    'Points :': 'Points:',
    'Points en n :': 'Points in n:',
    'Points et residus': 'Points and residuals',
    'points mesures et equation du viriel': 'measured points and virial equation',
    "Points retenus pour le viriel (vide : tous). L'equation du viriel est faite pour les isothermes de basse pression.": 'Points kept for the virial fit (empty: all). The virial equation is meant for low-pressure isotherms.',
    'points+ligne': 'points+line',
    'Police :': 'Font:',
    'Ponderation': 'Weighting',
    'Ponderation    : %s': 'Weighting      : %s',
    'Ponderation :': 'Weighting:',
    'Position legende :': 'Legend position:',
    'precombustion (gaz de synthese)': 'pre-combustion (syngas)',
    'Pression (bar)': 'Pressure (bar)',
    'Pression (gaz parfait)': 'Pressure (ideal gas)',
    "Pression d'etalement calculee par integration numerique.": 'Spreading pressure computed by numerical integration.',
    'Pression de saturation ou pseudo-saturation, requise par D-R et D-A a P0 fixe': 'Saturation or pseudo-saturation pressure, required by D-R and D-A with fixed P0',
    'Pression totale imposee lors du balayage en composition': 'Total pressure imposed during the composition sweep',
    "pressions de reference exigees par l'IAST": 'reference pressures required by IAST',
    'Pret': 'Ready',
    'pseudo-saturation de Dubinin  Pc(T/Tc)^2': 'Dubinin pseudo-saturation  Pc(T/Tc)^2',
    "purification de l'acetylene": 'acetylene purification',
    "purification de l'ethylene": 'ethylene purification',
    "purification de l'hydrogene": 'hydrogen purification',
    'q adsorbee (mmol/g)': 'Adsorbed q (mmol/g)',
    'q_max identiques -> Langmuir competitif exact': 'equal q_max -> exact competitive Langmuir',
    'Qst Clausius-Clapeyron : Langmuir a Q = 25 kJ/mol': 'Qst Clausius-Clapeyron: Langmuir with Q = 25 kJ/mol',
    'Qst en fonction de la quantite adsorbee (F5)': 'Qst versus adsorbed amount (F5)',
    'Qst isothermes': 'Qst isotherms',
    "Qst positif ; enthalpie d'adsorption = -Qst": 'Qst is positive; adsorption enthalpy = -Qst',
    'Qst viriel': 'Qst virial',
    'Qst viriel %s': 'Qst virial %s',
    'Qst viriel (courbe)': 'Qst virial (curve)',
    'Qst viriel (kJ/mol)': 'Qst virial (kJ/mol)',
    'Qst viriel (P <= 1 bar) : Langmuir a Q = 25 kJ/mol': 'Qst virial (P <= 1 bar): Langmuir with Q = 25 kJ/mol',
    'Quantite adsorbee (mmol/g)': 'Adsorbed amount (mmol/g)',
    'Quantite adsorbee n (mmol/g)': 'Adsorbed amount n (mmol/g)',
    'Quantite adsorbee pure nulle a P0.': 'Zero pure-component loading at P0.',
    'Quantite en exces': 'Excess amount',
    'Quantite en exces (mesure brute) ou totale (absolue)': 'Excess amount (raw measurement) or total (absolute) amount',
    'Quantite totale': 'Total amount',
    'quantites': 'loadings',
    'Que faut-il exporter ?': 'What should be exported?',
    'Quitter': 'Quit',
    'R2 ajuste': 'Adj. R2',
    'R2=%.8f  erreur relative max=%.1e': 'R2=%.8f  max relative error=%.1e',
    'R2_ajuste': 'R2_adj',
    'Ramene la somme des y a 1': 'Rescales the sum of y to 1',
    "Reajuste le modele N fois sur des residus reechantillonnes. Plus fiable que l'ecart-type asymptotique quand les parametres sont correles. Comptez quelques secondes par modele.": 'Refits the model N times on resampled residuals. More reliable than the asymptotic standard deviation when parameters are correlated. Allow a few seconds per model.',
    'Recharge integralement une session enregistree (Ctrl+O)': 'Fully reloads a saved session (Ctrl+O)',
    'Recharger une session enregistree (Ctrl+O)': 'Reload a saved session (Ctrl+O)',
    'reconnaissance des nouveaux gaz dans les noms de fichiers': 'new gases recognised in file names',
    'Reinitialiser (automatique)': 'Reset (automatic)',
    "Relance l'ajustement depuis plusieurs points de depart aleatoires et garde le meilleur. Recommande pour Toth, Sips et D-A qui ont des minima locaux.": 'Restarts the fit from several random starting points and keeps the best. Recommended for Toth, Sips and D-A, which have local minima.',
    'Remarque : %s': 'Note: %s',
    'Renseignez un volume poreux > 0.': 'Enter a pore volume > 0.',
    'Repartir de zero (Ctrl+N)': 'Start from scratch (Ctrl+N)',
    'repli automatique sur Peng-Robinson hors table': 'automatic fallback to Peng-Robinson outside the table',
    'Residus': 'Residuals',
    "Resolution sur la pression d'etalement (F5)": 'Solved on the spreading pressure (F5)',
    'RESULTAT : %d controles reussis, %d echecs   (%.1f s)': 'RESULT: %d checks passed, %d failures   (%.1f s)',
    'Resultats': 'Results',
    'Resultats des ajustements': 'Fit results',
    'resultats_IAST.xlsx': 'IAST_results.xlsx',
    'Resume de la session': 'Session summary',
    "Retirer l'ajustement selectionne": 'Remove the selected fit',
    'Retirer la ligne': 'Remove the row',
    'rho phase adsorbee :': 'Adsorbed-phase rho:',
    'rho_gaz (mmol/cm3)': 'rho_gas (mmol/cm3)',
    'Rien a exporter.': 'Nothing to export.',
    'Saisie manuelle...': 'Manual entry...',
    'Saisissez une colonne rho_gaz de meme longueur que les donnees (colonne 2 du tableau), puis relancez le calcul.': 'Enter a rho_gas column of the same length as the data (column 2 of the table), then run the calculation again.',
    'Sans ajustement (ignores par Clausius-Clapeyron) : %s.': 'Without a fit (ignored by Clausius-Clapeyron): %s.',
    "Selectionner plusieurs fichiers d'un coup. Le gaz, l'echantillon et les unites sont deduits du nom de fichier (ex. ZTC850-CO2.xlsx) ; un recapitulatif est affiche avant import.": 'Select several files at once. Gas, sample and units are deduced from the file name (e.g. ZTC850-CO2.xlsx); a summary is shown before import.',
    'Selectionnez des isothermes du meme gaz a au moins deux temperatures differentes.': 'Select isotherms of the same gas at two different temperatures or more.',
    'selectionnez pour ouvrir': 'select to open',
    'Selectionnez un jeu de donnees.': 'Select a dataset.',
    'Selectivite': 'Selectivity',
    'selectivites': 'selectivities',
    'Serie': 'Series',
    "Series de chaleur isosterique envoyees vers l'onglet Graphiques.": 'Isosteric heat series sent to the Plots tab.',
    "Series envoyees vers l'onglet Graphiques.": 'Series sent to the Plots tab.',
    'SERIES GRAPHIQUES (%d)': 'PLOT SERIES (%d)',
    "Series IAST envoyees vers l'onglet Graphiques.": 'IAST series sent to the Plots tab.',
    "Sert uniquement a signaler l'extrapolation du modele pendant le calcul IAST.": 'Only used to flag model extrapolation during the IAST calculation.',
    'Session AdsorpSuite': 'AdsorpSuite session',
    'Session chargee : %d jeux, %d ajustements, %d series, %d points IAST': 'Session loaded: %d datasets, %d fits, %d series, %d IAST points',
    'Session de travail': 'Working session',
    'Session en cours': 'Current session',
    'Session enregistree (%d jeux, %d ajustements)': 'Session saved (%d datasets, %d fits)',
    'Session enregistree : %s': 'Session saved: %s',
    'session non enregistree': 'unsaved session',
    'Session non enregistree': 'Unsaved session',
    'session_adsorption.adsp': 'adsorption_session.adsp',
    'Sessions recentes': 'Recent sessions',
    'Source du coefficient de fugacite (meme choix que pour la conversion exces -> total).': 'Source of the fugacity coefficient (same choice as for the excess -> total conversion).',
    'Statistiques :': 'Statistics:',
    'Statut': 'Status',
    'STRUCTURE DES FEUILLES': 'SHEET LAYOUT',
    'Style de la serie selectionnee': 'Style of the selected series',
    'Supprimer': 'Delete',
    "Supprimer '%s' ?": "Delete '%s'?",
    'Supprimer definitivement le jeu selectionne': 'Permanently delete the selected dataset',
    'Supprimer les lignes selectionnees (touche Suppr)': 'Delete the selected rows (Del key)',
    'Supprimer tous les ajustements ?': 'Delete all fits?',
    'SVG vectoriel': 'Vector SVG',
    'Table NIST': 'NIST table',
    'table NIST : 3 gaz a 303 K': 'NIST table: 3 gases at 303 K',
    "Table NIST : densites de reference tabulees (CO2, CH4, H2 a 303 K) - le plus exact, repli automatique sur Peng-Robinson hors table. Peng-Robinson : EOS cubique translatee Peneloux, 1 a 3 % d'ecart pres du point critique.": 'NIST table: tabulated reference densities (CO2, CH4, H2 at 303 K) - the most accurate, automatic fallback to Peng-Robinson outside the table. Peng-Robinson: cubic EOS with Peneloux volume translation, 1 to 3 % deviation near the critical point.',
    'Tableau croise jeu x modele : R2, RMSE et AIC cote a cote, avec le meilleur modele signale par jeu.': 'Dataset x model cross table: R2, RMSE and AIC side by side, with the best model flagged for each dataset.',
    'Taille': 'Size',
    'Taille des marqueurs': 'Marker size',
    'Temperature de la mesure, en kelvin': 'Measurement temperature, in kelvin',
    'Temperature, utilisee par D-R et D-A': 'Temperature, used by D-R and D-A',
    'ternaire': 'ternary',
    'Texte': 'Text',
    'Texte affiche dans la legende': 'Text shown in the legend',
    'Titre :': 'Title:',
    'tous le meme nombre de points.': 'have the same number of points.',
    'Tous les ajustements (%d)': 'All fits (%d)',
    'Tous les ajustements du jeu de donnees courant (%d)': 'All fits of the current dataset (%d)',
    'Tous les fichiers': 'All files',
    'Tous les jeux en CSV': 'All datasets as CSV',
    'Tout cocher': 'Tick all',
    'Tout decocher': 'Untick all',
    'Tout selectionner': 'Select all',
    'Tout supprimer': 'Delete all',
    'Tout vider': 'Clear all',
    'Toutes les valeurs doivent etre renseignees.': 'All values must be filled in.',
    "Tracer sur l'axe Y secondaire": 'Plot on the secondary Y axis',
    'Trait / point / opacite :': 'Line / point / opacity:',
    'Trier': 'Sort',
    'Trier par pression croissante': 'Sort by increasing pressure',
    "Trop peu de points pour l'equation du viriel (%d points).": 'Too few points for the virial equation (%d points).',
    'Type / couleur :': 'Type / colour:',
    'Type :': 'Type:',
    'Typique': 'Typical',
    'u Qst viriel (courbe)': 'u Qst virial (curve)',
    'u(Qst viriel) (kJ/mol)': 'u(Qst virial) (kJ/mol)',
    'Un bloc par indicateur : R2, RMSE (mmol/g) puis AICc.': 'One block per indicator: R2, RMSE (mmol/g), then AICc.',
    'un meme gaz sur un meme materiau, mesure a plusieurs temperatures': 'one gas on one material, measured at several temperatures',
    'un seul fichier contient tout : donnees, ajustements, IAST, graphiques': 'one single file holds everything: data, fits, IAST, plots',
    'Unite': 'Unit',
    'Unite :': 'Unit:',
    'Unite de la colonne pression du tableau': 'Unit of the pressure column of the table',
    'Unite de la colonne quantite adsorbee': 'Unit of the adsorbed amount column',
    'Unite P :': 'P unit:',
    'Unite q :': 'q unit:',
    'Utile pour garder des versions successives': 'Useful to keep successive versions',
    'V_pore (cm3/g) :': 'V_pore (cm3/g):',
    'Valeur': 'Value',
    'valeur de repli sur saisie invalide': 'fallback value on invalid input',
    'valeurs non finies (hors table ?)': 'non-finite values (outside the table?)',
    "Valide le tableau et les metadonnees. L'enregistrement est aussi automatique quand vous changez de jeu, lancez un ajustement ou quittez l'onglet - vos saisies ne sont plus perdues.": 'Validates the table and the metadata. Saving is also automatic when you switch dataset, start a fit or leave the tab - your entries are never lost.',
    'Valider': 'OK',
    'Verification interne': 'Internal check',
    'VERIFICATION INTERNE  -  %s v%s': 'INTERNAL CHECK  -  %s v%s',
    'Verification interne du programme': 'Internal check of the program',
    'Vers Graphiques': 'To Plots',
    'Vide : choix automatique par AICc (0 a 3)': 'Empty: automatic choice by AICc (0 to 3)',
    'Vide : choix automatique par AICc (1 a 6)': 'Empty: automatic choice by AICc (1 to 6)',
    'Vider': 'Clear',
    'Viriel': 'Virial',
    'Viriel (points mesures)': 'Virial (measured points)',
    'Viriel : degres a=%d, b=%d ; Qst0 = %s +/- %s kJ/mol ; R2 = %s sur %d points.': 'Virial: degrees a=%d, b=%d; Qst0 = %s +/- %s kJ/mol; R2 = %s on %d points.',
    "Viriel ajuste jusqu'a %s bar : l'equation du viriel est faite pour les basses pressions ; limitez 'P max viriel'.": "Virial fitted up to %s bar: the virial equation is meant for low pressures; lower 'Max P for virial'.",
    'Volume poreux': 'Pore volume',
    'Volume poreux      n_tot = n_exc + V_pore x rho_gaz(T,P)\nDensite adsorbee   n_tot = n_exc / (1 - rho_gaz/rho_ads)\nDensite fournie    vous saisissez rho_gaz dans la colonne 2 du tableau (valeurs NIST par exemple)': 'Pore volume        n_tot = n_exc + V_pore x rho_gas(T,P)\nAdsorbed density   n_tot = n_exc / (1 - rho_gas/rho_ads)\nSupplied density   you enter rho_gas in column 2 of the table (NIST values for example)',
    'Volume poreux invalide.': 'Invalid pore volume.',
    'Volume poreux total accessible, mesure par DFT, D-R ou pycnometrie helium': 'Total accessible pore volume, from DFT, D-R or helium pycnometry',
    'x et y vides : placement automatique en bas a droite': 'empty x and y: automatic placement at the bottom right',
    'X min / max :': 'X min / max:',
    'Y min / max :': 'Y min / max:',
    'Z(CH4, 100 bar) entre 0.80 et 0.88': 'Z(CH4, 100 bar) between 0.80 and 0.88',
    'Z(CO2, 1 bar) proche de 1': 'Z(CO2, 1 bar) close to 1',
    'Z(H2, 100 bar) superieur a 1': 'Z(H2, 100 bar) greater than 1',
    '●  modifications non enregistrees': '●  unsaved changes',
    '✓  a jour': '✓  up to date',
})

# v3.1.0 : pression de vapeur saturante et valeurs de reference pyIAST
TR_EN.update({
    "%d point(s) au-dessus de la pression de vapeur saturante de %s a %.2f K "
    "(Psat = %.2f bar, %s) : le fluide y est liquide et ces points ne "
    "decrivent plus l'adsorption d'un gaz.":
        "%d point(s) above the saturation pressure of %s at %.2f K "
        "(Psat = %.2f bar, %s): the fluid is liquid there and these points "
        "no longer describe gas adsorption.",
    "Retirez-les avant la conversion.": "Remove them before converting.",
    "Points au-dessus de la pression de vapeur saturante (fluide liquide, "
    "conversion sans objet) :":
        "Points above the saturation pressure (liquid fluid, conversion "
        "meaningless):",
    "Points au-dessus de la pression de vapeur saturante (fluide liquide) :":
        "Points above the saturation pressure (liquid fluid):",
    "Points au-dessus de la pression de vapeur saturante (fluide liquide) : "
    "%s. Retirez-les puis refaites l'ajustement : ils faussent les "
    "isosteres.":
        "Points above the saturation pressure (liquid fluid): %s. Remove "
        "them and refit: they distort the isosteres.",
    "IAST = pyIAST 1.4.3 sur 7 melanges de reference":
        "IAST = pyIAST 1.4.3 on 7 reference mixtures",
    "points au-dessus de Psat signales (CO2 a 273 K)":
        "points above Psat flagged (CO2 at 273 K)",
    "ecart max %.0e (analytique), %.0e (table)":
        "max deviation %.0e (analytical), %.0e (table)",
    "La table NIST ne couvre pas toutes les temperatures : les autres "
    "passent par Peng-Robinson. Preferez une seule source (CoolProp ou "
    "Peng-Robinson).":
        "The NIST table does not cover every temperature: the others use "
        "Peng-Robinson. Prefer a single source (CoolProp or Peng-Robinson).",
    "fugacite par la table NIST coherente a basse pression":
        "fugacity from the NIST table consistent at low pressure",
    "ecart ln(phi) %.1e a 0,1 bar, %.1e a 5 bar":
        "ln(phi) deviation %.1e at 0.1 bar, %.1e at 5 bar",
    "Conversion en lot - volume poreux par echantillon":
        "Batch conversion - pore volume per sample",
    "%d jeu(x) en exces, %d echantillons. Indiquez le volume poreux de "
    "chaque echantillon :":
        "%d excess dataset(s), %d samples. Enter the pore volume of each "
        "sample:",
    "Echantillon": "Sample",
    "Jeux": "Datasets",
    "Methode : %s    EOS : %s": "Method: %s    EOS: %s",
    "Convertir": "Convert",
    "Volume poreux invalide pour %s.": "Invalid pore volume for %s.",
})

# --- textes ajoutes en 3.2 ---------------------------------------------------
TR_EN.update({
    "Importer des fichiers...": "Import files...",
    "Importer en choisissant les colonnes...": "Import with column choice...",
    "Un ou plusieurs fichiers .xlsx, .xls ou .csv. Le gaz, la temperature et "
    "l'echantillon sont lus dans le nom du fichier (ex. "
    "ZTC850-CO2_303K.xlsx) ; un recapitulatif modifiable est affiche avant "
    "l'import.":
        "One or several .xlsx, .xls or .csv files. The gas, the temperature "
        "and the sample are read from the file name (e.g. "
        "ZTC850-CO2_303K.xlsx); an editable summary is shown before the "
        "import.",
    "Pour un fichier a plusieurs feuilles ou plusieurs colonnes : choisir "
    "soi-meme la feuille, les colonnes et les unites":
        "For a file with several sheets or several columns: choose the "
        "sheet, the columns and the units yourself",
    "Lire un ou plusieurs fichiers Excel ou CSV d'isothermes (Ctrl+I)":
        "Read one or several Excel or CSV isotherm files (Ctrl+I)",
    "Aucun jeu de donnees.\n\nImportez vos fichiers d'isothermes\n(bouton "
    "bleu a gauche), ou collez deux\ncolonnes depuis Excel dans le tableau.":
        "No dataset yet.\n\nImport your isotherm files\n(blue button on the "
        "left), or paste two\ncolumns from Excel into the table.",
    "Double-clic sur 'Nom du jeu', 'Gaz' ou 'T (K)' pour corriger une ligne. "
    "En jaune : a verifier (colonne Remarque).":
        "Double-click 'Dataset name', 'Gas' or 'T (K)' to correct a row. "
        "In yellow: to be checked (Note column).",
    "Remarque": "Note",
    "T par defaut": "default T",
    "nom deja pris : (2) sera ajoute": "name already used: (2) will be added",
    "%d colonnes, 2 lues": "%d columns, 2 read",
    "temperature lue dans le nom de fichier, noms de jeux uniques":
        "temperature read from the file name, unique dataset names",
    "accents du francais affiche, codes de format intacts":
        "French accents at display, format codes untouched",
    "Renseignez le volume poreux de l'echantillon (V_pore, en cm3/g).":
        "Enter the pore volume of the sample (V_pore, in cm3/g).",
    "Jeu en exces : a haute pression, ajustez plutot le jeu 'total' (onglet "
    "Conversion) pour l'IAST et la chaleur isosterique.":
        "Excess dataset: at high pressure, fit the 'total' dataset instead "
        "(Conversion tab) for IAST and the isosteric heat.",
    "\n\n%d jeu(x) en exces deja converti(s) en 'total' : non ajuste(s).":
        "\n\n%d excess dataset(s) already converted to 'total': not fitted.",
    "Comparer": "Compare",
    "Exporter": "Export",
    "Envoyer vers l'onglet Graphiques les lignes selectionnees ou, sans "
    "selection, le jeu affiche et ses courbes":
        "Send the selected rows to the Plots tab or, with no selection, the "
        "displayed dataset and its curves",
    "%d serie(s) envoyee(s) vers l'onglet Graphiques.":
        "%d series sent to the Plots tab.",
    "(propose d'apres les ajustements, a verifier)":
        "(suggested from the fits, please check)",
    "Les constituants semblent incoherents :\n\n  - %s\n\nLancer le calcul "
    "quand meme ?":
        "The components look inconsistent:\n\n  - %s\n\nRun the calculation "
        "anyway?",
    "A VERIFIER : ": "PLEASE CHECK: ",
    "%s : l'ajustement choisi est celui de %s":
        "%s: the selected fit is that of %s",
    "%s : isotherme en exces (%s)": "%s: excess isotherm (%s)",
    "%s : meme ajustement qu'un autre constituant":
        "%s: same fit as another component",
    "temperatures differentes : %s K": "different temperatures: %s K",
    "Donne toute la hauteur aux graphiques": "Gives the plots the full height",
    "Ajouter": "Add",
    "Tous les jeux de donnees (points)": "All datasets (points)",
    "Jeu et courbes affiches dans l'onglet Ajustement":
        "Dataset and curves shown in the Fitting tab",
    "Dernier calcul IAST": "Last IAST calculation",
    "Ajoute des series sans quitter l'onglet. Le bouton 'Vers Graphiques' "
    "des autres onglets fait la meme chose.":
        "Adds series without leaving the tab. The 'To Plots' button of the "
        "other tabs does the same.",
    "Aucune serie a tracer.\n\nBouton 'Ajouter' a gauche, ou 'Vers "
    "Graphiques' dans les\nonglets Ajustement, IAST et Chaleur isosterique.":
        "No series to plot.\n\n'Add' button on the left, or 'To Plots' in "
        "the\nFitting, IAST and Isosteric heat tabs.",
    "Journal": "Log",
    "Affiche ou masque l'historique des messages":
        "Shows or hides the message history",
    "Ctrl+Maj+S": "Ctrl+Shift+S",
})


# =============================================================================
# 17. ACCENTS DU FRANCAIS AFFICHE
# =============================================================================
# Le code s'ecrit sans accents (cles de TR_EN, valeurs internes, sessions) ;
# _() les ajoute a l'affichage. FR_ACCENTS donne, ecrits avec leurs accents,
# les mots et les tournures a accentuer : la forme sans accent sert de cle et
# la casse du texte est conservee. Noms de feuilles et de colonnes des
# fichiers exportes restent sans accent.
# shortcut: mot a mot, sans grammaire. Un mot ambigu (participe en -e, "a" du
# verbe avoir) se regle en ajoutant ici la tournure entiere ; a defaut il
# s'affiche sans accent ou, pour "a", avec celui de la preposition.
FR_ACCENTS = """
à, acentricité, acétylène, adaptée, adsorbée, adsorbées, affichée, affichés,
ajustée, ajustées, ajustés, aléatoires, aperçu, appliquée, après, calculée,
calculées, calculés, capacité, carrés, chargée, citée, cochés, cohérence,
cohérent, cohérente, compétitif, complète, concernées, configurées,
conseillées, conservée, contrôle, contrôlée, contrôles, corrélation, corrélés,
crée, créer, décimale, décocher, décrivent, dédiée, déduction, déduits, défaut,
défilent, défini, définie, définitivement, degré, degrés, déjà, delà,
démarrage, densité, densités, départ, départs, dépassent, dépend, déplacement,
déplacent, dérivées, dernière, déroulante, désigner, détail, détails, détecté,
détection, détermine, différentes, donnée, données, ébullition, écart,
échantillon, échantillonnée, échantillons, échec, échecs, échelle, échelles,
écrit, écrits, éditer, effectuée, énergie, enregistrée, enregistrées, envoyée,
envoyées, épaisseur, équation, équations, équivalent, équivalents, estimée,
étalement, état, éthylène, être, éviter, excès, exigées, expérimentale,
expérimentales, expérimentaux, exportée, exportées, façon, fenêtre, fixée,
français, fugacité, fumées, grisée, hélium, honnête, hydrogène, hypothèse,
ignorés, importée, imposée, incohérents, inférieur, installé, intégrale,
intégralement, intégralité, intégration, intermédiaire, interprétez,
isostères, isostérique, légende, légère, linéaire, lisibilité, lissée,
lissées, matériau, mélange, mélanges, même, mêmes, mémorisée, mesurée,
mesurées, métadonnées, méthode, méthodes, modèle, modèles, nommée, nucléaire,
numérique, numériques, oléfine, opacité, opérationnels, paramètre, paramètres,
pénalisant, péneloux, plutôt, pondération, possèdent, précédent, précédente,
précombustion, préférez, près, présents, prêt, proposée, pycnométrie, qualité,
quantité, quantités, ramène, réajuste, récapitulatif, récentes, reçoit,
récupération, redémarre, redémarrer, réduite, rééchantillonnés, réel,
référence, réglages, réglée, réinitialiser, remplacés, renseignée,
renseignées, résidu, résidus, résolution, résultat, résultats, réussi,
réussis, sélection, sélectionnée, sélectionnées, sélectionner, sélectionnez,
sélectivité, sélectivités, séparateurs, séparée, série, séries, signalés,
supérieur, surlignées, synthèse, système, tabulées, température,
températures, tirée, tracées, translatée, très, unité, unitée, unités,
utilisée, utilisées, vérification, vérifier, vérifiez, zéro,

d-a, n'a, a besoin, a échoué, n'a convergé, degré a, degrés a, côte à côte,
domaine sûr, règle de, généré le, (modifié), créé(s), ignoré(s), jeu créé,
jeu importé, importé de, jeu proposé, proposé d'après, jeu sélectionné,
ajustement sélectionné, peu adsorbé, nom affiché, texte affiché,
le jeu affiché, est affiché, est ajouté, sera ajouté, ajouté (%d points),
jeu(x) ajouté(s), est demandé, est donné, est enregistré, fichier enregistré,
jeu de données enregistré, est marqué, p0 ajusté, r2 ajusté, viriel ajusté,
non ajusté, ou ajusté, modèle ajusté, ajusté sur, type appliqué,
tableau croisé, bien déterminé, iast effectué, domaine mesuré,
mesuré à plusieurs, mesuré par, points mesurés, recommandé pour, le résumé,
résumé de, modèle signalé, modèle surligné, lot terminé, panneaux tracés,
peng-robinson utilisé, modèle utilisé, sera utilisé,
feuilles : parametres / courbes ajustees / residus, parametres      :
"""

# textes identiques dans les deux langues (donc absents de TR_EN) mais qui
# prennent un accent en francais
FR_ONLY = ["Series", "Details", "isosteres", "Equation       : %s",
           "   Equation   : %s"]


def _sans_accent(s):
    return unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode()


_FR = {_sans_accent(w): w
       for w in (x.strip() for x in FR_ACCENTS.split(",")) if w}
# les tournures d'abord (les plus longues en premier), puis n'importe quel mot
_FR_RE = re.compile(r"(?<![%\w])(?:" + "|".join(
    re.escape(k) for k in sorted(_FR, key=len, reverse=True)
    if not k.isalpha()) + r"|[A-Za-z]+)(?!\w)", re.I)


def fr_accents(s):
    """Texte francais du code -> texte affiche, avec ses accents."""
    def rep(m):
        t = m.group(0)
        return "".join(b.upper() if a.isupper() else b
                       for a, b in zip(t, _FR.get(t.lower(), t)))
    return _FR_RE.sub(rep, s)


TR_FR.update((s, fr_accents(s)) for s in list(TR_EN) + FR_ONLY)


def main():
    lang = None
    for i, a in enumerate(sys.argv):
        if a.startswith("--lang="):
            lang = a.split("=", 1)[1]
        elif a == "--lang" and i + 1 < len(sys.argv):
            lang = sys.argv[i + 1]
    if not lang:
        try:
            lang = load_settings().get("language")
        except Exception:
            lang = None
    set_language(lang or system_language())
    if "--selftest" in sys.argv:
        rep = run_selftest()
        out = [a.split("=", 1)[1] for a in sys.argv if a.startswith("--out=")]
        if out:
            with open(out[0], "w", encoding="utf-8") as fh:
                fh.write(rep)
        try:
            print(rep)
        except Exception:
            pass
        ok = " 0 echecs" in _sans_accent(rep) or " 0 failures" in rep
        sys.exit(0 if ok else 1)
    check = [a.split("=", 1)[1] for a in sys.argv if a.startswith("--check-gui=")]
    app = App()
    # session passee en argument : redemarrage de langue, ou fichier .adsp
    # ouvert avec le programme
    adsp = [a for a in sys.argv[1:]
            if a.lower().endswith(SESSION_EXT) and os.path.exists(a)]
    if adsp:
        app.after(200, lambda: app.open_session(adsp[-1]))
    if check:
        # Controle du programme compile : la fenetre s'ouvre, se decrit dans
        # un fichier JSON puis se ferme seule (rien n'est enregistre).
        dl = [a.split("=", 1)[1] for a in sys.argv if a.startswith("--check-delay=")]
        app.state("normal")                 # meme si les reglages disent "agrandie"
        app.geometry("1150x720+20+20")      # taille minimale : cas le plus serre

        def _report():
            info = dict(ok=True, version=APP_VERSION, lang=LANG,
                        coolprop=HAS_COOLPROP, title=app.title(),
                        tabs=[app.nb.tab(t, "text") for t in app.nb.tabs()],
                        size=[app.winfo_width(), app.winfo_height()])
            try:
                with open(check[0], "w", encoding="utf-8") as fh:
                    json.dump(info, fh, ensure_ascii=False, indent=1)
            finally:
                app.destroy()
        app.after(int(1000 * to_float_or(dl[0] if dl else "", 4.0)), _report)
    app.mainloop()


if __name__ == "__main__":
    main()
