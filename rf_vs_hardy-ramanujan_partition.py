from mpmath import mp, mpf, sqrt, exp, pi, nint
from sympy.functions.combinatorial.numbers import partition

# ---------------- CONFIGURE HIGH-PRECISION ----------------
mp.dps = 1000  # decimal digits

# ---------------- INPUT ----------------
n = int(input("Enter n: "))

# ---------------- CORE FUNCTIONS ----------------
def theta(n):
    n = mpf(n)
    return ((1 + 1/(n-1))**(n-1) - 1) / (mp.e - 1)

def ramanujan_P(n):
    n = mpf(n)
    return 1/(4*n*sqrt(3)) * exp(pi * sqrt(2*n/3))

def a(n_a):
    A, B, p = mpf('1.30733384'), mpf('-0.56746428'), mpf('0.52889032')
    return A + B / n_a**p

def b(n_b):
    B0, C, D = mpf('0.23510967'), mpf('-22.59651803'), mpf('0.56042269')
    return B0 / (n_b + C) + D

def k(n):
    n = mpf(n)
    return a(n) + b(n)*sqrt(n)

def RF(n):
    n = mpf(n)
    return (1 / (1 - 1/n)) * (1 + theta(n)**k(n) * ramanujan_P(n))

# ---------------- COMPUTATION ----------------
Pn = mpf(partition(n))   # exact
RFn = RF(n)
RAn = ramanujan_P(n)

# ---- round to nearest integer ----
RFn_round = nint(RFn)
RAn_round = nint(RAn)

# ---- relative errors ----
err_rf = mp.fabs(Pn - RFn_round) / Pn
err_ra = mp.fabs(Pn - RAn_round) / Pn

# ---------------- OUTPUT ----------------
print("\n=== RESULT ===\n")
print(f"P(n)        = {Pn}")
print(f"RF(n)       = {RFn_round}")
print(f"RA(n)       = {RAn_round}")

print("\n--- Relative Errors ---")
print(f"RF error    = {float(err_rf):.6e}")
print(f"RA error    = {float(err_ra):.6e}")
