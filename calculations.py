import math
import sys
def S_even(N):
    """
    Computes the partial sum:
      Seven(N) = sum{n=1..N} [2π - 2n sin(π/n)]
    """
    total = 0.0
    for n in range(1, N+1):
        term = 2math.pi - 2.0nmath.sin(math.pi/n)
        total += term
    return total
def S_odd(N):
    """
    Computes the partial sum:
      Sodd(N) = sum{n=1..N} [2π/n - 2 sin(π/n)]
    """
    total = 0.0
    for n in range(1, N+1):
        term = (2math.pi)/n - 2.0math.sin(math.pi/n)
        total += term
    return total
# Set maximum N, controlling how far you sum:
maxN = 500000   # Increase if you want more precision (time permitting).
reportStep = 50000  # Print progress every 50k steps, for example.
Se = 0.0
So = 0.0
for n in range(1, maxN+1):
    # Accumulate each term incrementally:
    Se += 2math.pi - 2.0nmath.sin(math.pi/n)
    So += (2math.pi)/n - 2.0math.sin(math.pi/n)
    # Check progress at intervals:
    if n % reportStep == 0:
        ratio = So / Se
        diff  = Se - So
        print(f"n={n:7d}: S_even={Se:18.12f}, S_odd={So:18.12f}, ratio={ratio:14.12f}, diff={diff:14.12f}")
