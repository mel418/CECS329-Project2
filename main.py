import random
import time
import tracemalloc

def subset_sum(S, t):
    """
    Determines if there exists a subset of S that sums to t.
    """
    memo = {}

    def helper(index, target):
        if target == 0:
            return True
        if index == len(S) or target < 0:
            return False
        if (index, target) in memo:
            return memo[(index, target)]
        # Include or exclude the current element
        include = helper(index + 1, target - S[index])
        exclude = helper(index + 1, target)
        memo[(index, target)] = include or exclude
        return memo[(index, target)]

    return helper(0, t)

# Generate random input
random.seed(42)  # For reproducibility
S = [random.randint(1, 100) for _ in range(100)]  # 100 random integers between 1 and 100
t = sum(random.sample(S, 10))  # Randomly choose 10 elements and sum them as the target

# Measure runtime
start_time = time.time()
tracemalloc.start()
result = subset_sum(S, t)
current, peak = tracemalloc.get_traced_memory()
end_time = time.time()

# Compute runtime and memory usage
runtime = end_time - start_time
tracemalloc.stop()

# Output results
print(f"Set: {S}")
print(f"Target: {t}")
print(f"Does subset sum exist? {result}")
print(f"Runtime: {runtime:.6f} seconds")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
