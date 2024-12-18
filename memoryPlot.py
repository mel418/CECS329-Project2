import matplotlib.pyplot as plt

# Data for Input Size and Memory Usage
input_sizes = [100, 200, 300]
memory_usage = [6.11, 6.63, 25.18]  # in MB

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(input_sizes, memory_usage, marker='o', label='Memory Usage')

# Labels and Title
plt.xlabel('Input Size (Number of Elements)', fontsize=12)
plt.ylabel('Memory Usage (MB)', fontsize=12)
plt.title('Memory Usage vs Input Size', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Show Plot
plt.show()
