from functools import lru_cache

# --- Partition numbers P(n) via pentagonal recurrence ---
@lru_cache(maxsize=None)
def P(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    total = 0
    k = 1
    while True:
        pent1 = k*(3*k-1)//2
        pent2 = k*(3*k+1)//2
        if pent1 > n:
            break
        sign = (-1)**(k+1)
        total += sign * P(n - pent1)
        if pent2 <= n:
            total += sign * P(n - pent2)
        k += 1
    return total

# --- Partitions into at most k parts ---
@lru_cache(maxsize=None)
def P_at_most_k(n, k):
    if n == 0:
        return 1
    if n < 0 or k <= 0:
        return 0
    return P_at_most_k(n, k-1) + P_at_most_k(n - k, k)

# --- Middle section sum M(n) ---
def middle_section(n):
    """
    M(n) = sum_{y=2}^{n//2-1} sum_{j=1}^{y+1} P(n-y-1-j, j)
    Direct numeric calculation, exactly like the table for S(n)
    """
    half = n // 2
    M = 0
    for y in range(2, half - 1):
        k = y + 1
        for j in range(1, k + 1):
            i_val = n - y - 1 - j
            if i_val >= 0:
                M += P_at_most_k(i_val, j)
    return M

# --- Full formula P(n) - 2 ---
def P_via_formula(n):
    half = n // 2
    prefix_sum = sum(P(i) for i in range(1, half + 1))  # sum of first half
    M = middle_section(n)                                # middle section sum
    tail = half                                          # last element
    formula_sum = prefix_sum + M + tail
    return formula_sum, prefix_sum, M, tail

# --- Test ---
for n in [20, 30, 40, 50]:
    formula_sum, prefix, M, tail = P_via_formula(n)
    actual_P = P(n)
    print(f"\n=== n = {n} ===")
    print(f"P(n) via pentagonal recurrence: {actual_P}")
    print(f"P(n) - 2 via formula:           {formula_sum}")
    print(f"Check match? {actual_P - 2 == formula_sum}")
    print(f"Breakdown: prefix_sum={prefix}, M(n)={M}, tail={tail}")
