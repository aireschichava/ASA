import subprocess
import time
import os
import sys

# Define instances N values (More than 10 instances)
# We go up to 2400 to get a good spread, keeping it quick enough.
N_values = [100, 200, 300, 400, 500, 600, 800, 1000, 1200, 1400, 1600, 2000, 2200]

results = []

print("Running experiments...", file=sys.stderr)

for n in N_values:
    # 1. Generate Input
    with open("temp.in", "w") as f_in:
        subprocess.run(["python3", "gen_test.py", str(n)], stdout=f_in, check=True)
    
    # 2. Parse K from input file
    with open("temp.in", "r") as f_read:
        lines = f_read.readlines()
        try:
            k = int(lines[3].strip())
        except IndexError:
            k = 0

    # 3. Run Project and Measure Time
    start_time = time.perf_counter()
    with open("temp.in", "r") as f_in, open(os.devnull, "w") as f_out:
        subprocess.run(["./project"], stdin=f_in, stdout=f_out, check=True)
    end_time = time.perf_counter()
    
    elapsed = end_time - start_time
    print(f"Done N={n}, K={k}, Time={elapsed:.4f}s", file=sys.stderr)
    
    results.append((n, k, elapsed))

# Remove temp file
if os.path.exists("temp.in"):
    os.remove("temp.in")

# Output for the tool to read
print("RAW_DATA_START")
print(results)
print("RAW_DATA_END")

# Output Markdown Table
print("\n| N (Vértices) | K (Arestas) | Tempo (s) |")
print("| :--- | :--- | :--- |")
for n, k, t in results:
    print(f"| {n} | {k} | {t:.4f} |")
