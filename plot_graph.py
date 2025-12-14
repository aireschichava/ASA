import matplotlib.pyplot as plt
import pandas as pd

# Data from timings.csv
data = {
    'N': [100, 200, 400, 800, 1600, 3200],
    'Time': [0.006, 0.016, 0.055, 0.224, 0.964, 4.320]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.plot(df['N'], df['Time'], marker='o', linestyle='-', color='b', label='Execution Time')
plt.title('Execution Time vs N (Log-Log Scale)')
plt.xlabel('N (Number of Intersections)')
plt.ylabel('Time (seconds)')
plt.xscale('log')
plt.yscale('log')
plt.grid(True, which="both", ls="-")
plt.legend()
plt.savefig('performance_graph.png')
print("Graph saved to performance_graph.png")
