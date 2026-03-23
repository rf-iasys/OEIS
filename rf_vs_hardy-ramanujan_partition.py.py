"""
rf_vs_hardy-ramanujan_partition.py

High-precision exploration of integer partition numbers P(n).
Compares:
  - RF(n):  Formula with fitted k(n) parameter
  - RA(n): Classical Hardy-Ramanujan asymptotic formula

Features:
  - Uses mpmath for 100-digit precision
  - Can compute P(n) for extremely large n (up to hundreds of thousands or more)
  - Reports relative errors of RF(n) and RA(n) versus actual P(n)
  - k(n) parameter follows a power-law plus hyperbolic model: a(n_max) + b(n_max)√n
  - Fitted constants: A, B, p, B0, C, D

Author: Rui Ferreira - rui.ferreira@iasys.eu
Date: 2026
"""

from mpmath import mp, mpf, sqrt, exp, pi
from sympy.functions.combinatorial.numbers import partition
import matplotlib.pyplot as plt

# ---------------- CONFIGURE HIGH-PRECISION ----------------
mp.dps = 1000  # decimal digits

# ---------------- PARAMETERS ----------------
n_max_final = 4096000   # max n_max used for k(n)
n_list = [50, 100, 200, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000, 1024000, 2048000, 4096000]

# ---------------- CORE FUNCTIONS ----------------
def theta(n):
    """ correction function for RF formula."""
    n = mpf(n)
    return ((1 + 1/(n-1))**(n-1) - 1) / (mp.e - 1)

def ramanujan_P(n):
    """Classic Ramanujan approximation for P(n)."""
    n = mpf(n)
    return 1/(4*n*sqrt(3)) * exp(pi * sqrt(2*n/3))

# ---- your fitted models ----
def a(n_max):
    """Power-law parameter for k(n). A, B, and p formulas remain undisclosed."""
    A, B, p = mpf('1.30733384'), mpf('-0.56746428'), mpf('0.52889032')
    return A + B / n_max**p

def b(n_max):
    """Hyperbolic parameter for k(n). B0, C, and D formulas remain undisclosed."""
    B0, C, D = mpf('0.23510967'), mpf('-22.59651803'), mpf('0.56042269')
    return B0 / (n_max + C) + D

def k(n, n_max):
    """Final k(n) function for RF formula."""
    n = mpf(n)
    return a(n_max) + b(n_max)*sqrt(n)

def RF(n, n_max):
    """ formula (RF) for the partition function P(n)."""
    n = mpf(n)
    k_n = k(n, n_max)
    return (1 / (1 - 1/n)) * (1 + theta(n)**k_n * ramanujan_P(n))

# ---------------- COMPUTE RELATIVE ERRORS ----------------
rel_err_RF = []
rel_err_RA = []

for n in n_list:
    Pn = mpf(partition(n))          # exact partition number
    RFn = RF(n, n_max_final)        # formula
    RAn = ramanujan_P(n)            # Hardy-Ramanujan formula

    rel_err_RF.append(abs(RFn - Pn)/Pn)
    rel_err_RA.append(abs(RAn - Pn)/Pn)

# ---------------- PLOT ----------------
plt.figure(figsize=(10,6))
plt.loglog(n_list, rel_err_RF, label='RF formula', marker='o', color='green')
plt.loglog(n_list, rel_err_RA, label='Ramanujan approximation', marker='x', color='red', linestyle='--')

plt.xlabel('n')
plt.ylabel('Relative Error')
plt.title('Relative Error of Partition Function Approximations (log-log)')
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()

# ---------------- PRINT TABLE ----------------
print(f"{'n':>10} | {'RelErr RF':>25} | {'RelErr RA':>25}")
print("-"*65)

for n in n_list:
    Pn = mpf(partition(n))        # exact partition from SymPy
    rf = RF(n, n_max_final)       # RF formula
    ra = ramanujan_P(n)           # Hardy–Ramanujan approximation

    err_rf = mp.fabs(Pn - rf) / Pn
    err_ra = mp.fabs(Pn - ra) / Pn

    # Convert mpf to float for formatting
    print(f"{n:10d} | {float(err_rf):25.12e} | {float(err_ra):25.12e}")
