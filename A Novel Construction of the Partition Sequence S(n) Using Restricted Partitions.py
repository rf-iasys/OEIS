import math
import matplotlib.pyplot as plt
import numpy as np

n = 20  # You can change to 500 or any n

# --- Partition numbers function using dynamic programming ---
def partition_numbers_up_to(n):
    p = [0] * (n + 1)
    p[0] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            p[j] += p[j - i]
    return p

# --- Partitions into at most k parts ---
def partitions_at_most_k(n, k):
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(k + 1):
        dp[i][0] = 1
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= i:
                dp[i][j] += dp[i][j - i]
    return dp

# --- Build sequence S_n ---
half = math.floor(n / 2)
p = partition_numbers_up_to(half)
prefix = p[1:half + 1]

num_elements = n - 2 - math.floor((n + 2) / 2)
ys = range(2, 2 + num_elements)

# --- Build middle table with OEIS reference and sequence annotation ---
elements = []
middle_table = []  # Table to record middle elements

for idx, y in enumerate(ys, start=1):
    k = y + 1
    # --- Build middle table with OEIS reference, sequence annotation, and safe-k check ---
    elements = []
    middle_table = []  # Table to record middle elements

    for idx, y in enumerate(ys, start=1):
        k = y + 1

        # --- ASSERT: never calculate partitions with parts > floor(n/2) ---
        safe_k = k <= half
        if not safe_k:
            raise ValueError(f"Attempting to calculate partitions with k={k} > floor(n/2)={half}")

        dp = partitions_at_most_k(n, k)
        seq = dp[k][1:n + 1]  # Python slicing: skip 0
        value = seq[n - y - 2]
        
        # OEIS index correction: since seq[0] = dp[k][1], OEIS index = DP idx + 1
        oeis_idx = n - y - 2 + 1
        
        elements.append(value)
        middle_table.append({
            "Middle idx": idx,
            "y": y,
            "k = y+1": k,
            "DP idx (Python)": n - y - 2,
            "OEIS idx": oeis_idx,
            "Value": value,
            "Sequence description": f"Number of partitions of n into at most {k} parts",
            "Safe k": safe_k
        })
        
elements = elements[::-1]
elements.append(half)
final_sequence = prefix + elements

# --- Print middle table with OEIS index, annotation, and Safe k check ---
print("\nMiddle S(n) elements table with OEIS references and safe-k check:")
print("-" * 120)
print(f"{'Middle idx':>10} | {'y':>3} | {'k=y+1':>5} | {'DP idx':>7} | {'OEIS idx':>8} | {'Value':>5} | {'Sequence description':<45} | {'Safe k':>6}")
print("-" * 120)
for row in middle_table[::-1]:  # reversed to match final S(n) order
    print(f"{row['Middle idx']:>10} | {row['y']:>3} | {row['k = y+1']:>5} | {row['DP idx (Python)']:>7} | {row['OEIS idx']:>8} | {row['Value']:>5} | {row['Sequence description']:<45} | {str(row['Safe k']):>6}")
print("-" * 120)

# --- X-axis for plotting ---
x = np.arange(1, len(final_sequence) + 1)

# --- Mode (k_mode) approximation ---
k_mode = (math.sqrt(6 * n) / math.pi) * math.log(math.sqrt(6 * n) / math.pi)
seq_peak_index = n - k_mode - 2
y_max = max(final_sequence)
x_max_all = [i for i, v in enumerate(final_sequence) if v == y_max]
x_max = x_max_all[0] + 1

# --- Console reporting ---
sum_seq = sum(final_sequence)
Pn = partition_numbers_up_to(n)[n]

print(f"\nSequence S({n}) construction")
print("="*50)
print(f"Full S({n}) sequence (length {len(final_sequence)}):")
print(final_sequence)
print(f"\nSum of S({n}) = {sum_seq}")
print(f"P({n}) - 2 = {Pn - 2}")
print(f"\nPosition x_max = {x_max}")
print(f"Approximate mode k_mode ≈ {k_mode:.2f}, x_max approx ≈ {seq_peak_index:.2f}")
print(f"\nPeak value y_max = {y_max} (OEIS A002569)")
print("="*50)

# --- Plot the sequence ---
plt.figure(figsize=(12, 6))
plt.plot(
    x, final_sequence,
    marker='o',
    markersize=3,
    linestyle='-',
    color='purple',
    label='Sequence'
)
plt.scatter(x_max, y_max, color='black', s=10, zorder=5)
plt.text(x_max + 0.5, y_max, f"y_max={y_max}\nOEIS A002569", color='black')
plt.axvline(x=x_max, color='black', linestyle='--', label=f"k_mode ≈ {k_mode:.2f}")
plt.text(x_max + 0.5, max(final_sequence)*0.8, f"k_mode ≈ {k_mode:.2f} x_max approx ≈ {x_max}", color='black')
plt.title(f"Sequence for n={n} with middle S(n) table")
plt.xlabel("Position in sequence")
plt.ylabel("Value (number of partitions)")
plt.grid(True)
plt.legend()
plt.show()
