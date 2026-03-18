import urllib.request
import math

# Check if a number is prime
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# Compute primorial m#
def primorial(m):
    p = 1
    for i in range(2, m + 1):
        if is_prime(i):
            p *= i
    return p

# Cache primorials to speed up
primorial_cache = {}

def get_primorial(x):
    if x not in primorial_cache:
        primorial_cache[x] = primorial(x)
    return primorial_cache[x]

results = {}

n_max = 5000

# -------- Main computation --------
for n in range(2, n_max + 1):

    n_fact = math.factorial(n)
    n_prim = get_primorial(n)

    k = 1
    while True:
        k_prim = get_primorial(k)

        if n_fact < k_prim + n_prim:
            results[n] = k
            break

        k += 1

# -------- Print original table --------
for n in results:
    print(f"n = {n}, first k = {results[n]}")

# -------- Extract OEIS-style sequences --------
prev_k = None
oeis_n = []
oeis_k = []

for n in sorted(results):
    k = results[n]
    if k != prev_k:
        oeis_n.append(n)
        oeis_k.append(k)
        prev_k = k

print("\nOEIS-style n sequence:")
print(",".join(map(str, oeis_n)))

print("\nCorresponding k values:")
print(",".join(map(str, oeis_k)))

print("\nPairs (n, k):")
for n, k in zip(oeis_n, oeis_k):
    print(f"({n}, {k})")

# -------- Fetch OEIS A085302 data --------
url = "https://oeis.org/A085302/b085302.txt"

oeis_data = []

req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(req) as response:
    for line in response:
        line = line.decode("utf-8").strip()

        # Skip comments
        if not line or line.startswith("#"):
            continue

        parts = line.split()
        if len(parts) >= 2:
            value = int(parts[1])
            oeis_data.append(value)

# -------- Direct comparison --------
print("\n--- Direct comparison (your n vs OEIS A085302 values) ---")

match = True
min_len = min(len(oeis_n), len(oeis_data))

for i in range(min_len):
    if oeis_n[i] != oeis_data[i]:
        print(f"Mismatch at position {i+1}: yours={oeis_n[i]}, oeis={oeis_data[i]}")
        match = False
        break

if match:
    print("✅ Perfect match with OEIS A085302!")

# -------- Full strict comparison --------
print("\n--- Full strict comparison (your n vs OEIS A085302) ---")

match = True

for i, (a, b) in enumerate(zip(oeis_n, oeis_data), start=1):
    if a != b:
        print(f"❌ Mismatch at position {i}: yours={a}, oeis={b}")
        match = False
        break

if match:
    print("✅ PERFECT MATCH: All your values align with OEIS A085302 (no misalignment).")
    print(f"Checked {len(oeis_n)} values successfully.")

# -------- Optional: sanity check lengths --------
if len(oeis_data) > len(oeis_n):
    print(f"\nOEIS has {len(oeis_data) - len(oeis_n)} extra values (ignored, as expected).")
