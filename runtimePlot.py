import matplotlib.pyplot as plt

# Data
input_sizes = [100, 200, 300]
runtimes = [0.152812, 0.265898, 1.516171]

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(input_sizes, runtimes, marker='o', label='Runtime')

# Labels and Title
plt.xlabel('Input Size (|S|)', fontsize=12)
plt.ylabel('Runtime (seconds)', fontsize=12)
plt.title('Runtime vs Input Size', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Show Plot
plt.show()
