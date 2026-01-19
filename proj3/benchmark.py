
import random
import time
import subprocess
import csv
import sys

# Configuration
INSTANCES = []
for n in range(5, 65, 5): # 5, 10, ..., 60 (12 instances)
    INSTANCES.append(n)

OUTPUT_CSV = "benchmark_results.csv"
OUTPUT_IMG = "experiment_graph.png"
MAIN_SCRIPT = "main.py"

def generate_input(n):
    """
    Generates a random tournament input for N teams.
    We'll simulate a partially played season (approx 50-70% played).
    """
    matches = []
    played_count = 0
    all_matches = []
    
    # Generate all possible matches
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j: continue
            all_matches.append((i, j))
    
    total_games = len(all_matches)
    matches_to_play = int(total_games * 0.6) # 60% played
    
    played_matches = random.sample(all_matches, matches_to_play)
    
    input_str = f"{n} {len(played_matches)}\n"
    
    for h, a in played_matches:
        # Random result: 1=Home, 2=Away, 0=Draw
        r = random.choice([h, a, 0]) 
        # But wait, input format is H A R. R is the team ID or 0.
        # So it's correctly chosen from [h, a, 0]
        input_str += f"{h} {a} {r}\n"
        
    return input_str, n, len(played_matches)

def estimate_complexity(input_str, n):
    """
    Parses input and estimates actual LP variables and constraints 
    AFTER pruning logic as implemented in main.py.
    """
    lines = input_str.strip().split('\n')
    header = lines[0].split()
    n_in = int(header[0])
    m_in = int(header[1])
    
    scores = [0] * (n + 1) # 1-based index
    played_set = set()
    
    # Parse games
    for i in range(1, len(lines)):
        parts = list(map(int, lines[i].split()))
        if len(parts) < 3: continue
        h, a, r = parts
        played_set.add((h, a))
        if r == h: scores[h] += 3
        elif r == a: scores[a] += 3
        else: scores[h]+=1; scores[a]+=1
            
    # Calculate Remaining Matches and Potential
    remaining = []
    potential = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j: continue
            if (i, j) not in played_set:
                remaining.append((i, j))
                potential[i] += 3
                potential[j] += 3
                
    leader_score = max(scores[1:])
    
    # We solve for EACH team i. 
    # The complexity is the sum of complexity for all N LPs? 
    # Or maximum single LP? usually Total work.
    # But graph asks for "soma das restrições + variáveis".
    # Since we solve N LPs sequentially, total time depends on total instances.
    # However, standard complexity analysis usually refers to the size of ONE instance.
    # Let's count the AVERAGE size of the LP for a team, times N?
    # Or just Total Variables/Constraints processed across all N iterations.
    # Given we plot "Time vs Size", Total Time vs Total Size makes sense.
    
    total_vars = 0
    total_constrs = 0
    
    for team_id in range(1, n + 1):
        # 1. Pruning Check 1 (Impossible)
        if scores[team_id] + potential[team_id] < leader_score:
            continue # Pruned substantially
            
        # 2. Pruning Check 2 (No Matches)
        my_matches = [m for m in remaining if m[0] == team_id or m[1] == team_id]
        # logic in main.py: `if not matches: ...` -> checking remaining list passed
        # Remaining list passed to `solve_for_team` is ALL remaining matches?
        # Yes, `matches` arg is `remaining_matches`.
        
        if not remaining:
            continue
            
        # Variables: 3 per match in `remaining_matches`
        # Wait, `match_vars` iterates `idx, (h, a) in enumerate(matches)`
        # `matches` is the full `remaining_matches` list.
        # So Vars = 3 * len(remaining_matches)
        
        num_vars = 3 * len(remaining)
        
        # Constraints:
        # 1. Structural: w+t+l=1 (One per match)
        num_constr_struct = len(remaining)
        
        # 2. Score Comparisons: MyScore >= OtherScore
        num_constr_comp = 0
        
        # Calculate gained points expressions involved...
        # The loop `for other in range(1, n+1)`
        for other in range(1, n + 1):
            if other == team_id: continue
            
            # Pruning Logic
            if scores[team_id] >= scores[other] + potential[other]:
                continue
            
            num_constr_comp += 1
            
        current_lp_vars = num_vars
        current_lp_constrs = num_constr_struct + num_constr_comp
        
        total_vars += current_lp_vars
        total_constrs += current_lp_constrs
        
    return total_vars, total_constrs

results = []

print("Running benchmarks...")
with open(OUTPUT_CSV, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["N", "M_Played", "Total_Vars", "Total_Constraints", "Time_Sec", "Size_Metric"])
    
    for n in INSTANCES:
        inp, n_real, m_played = generate_input(n)
        
        # Estimate Size
        vars_count, constr_count = estimate_complexity(inp, n)
        size_metric = vars_count + constr_count
        
        # Measure Time
        start = time.time()
        # Run main.py as subprocess
        proc = subprocess.run([sys.executable, MAIN_SCRIPT], input=inp, text=True, capture_output=True)
        end = time.time()
        elapsed = end - start
        
        print(f"N={n}: Time={elapsed:.4f}s, Size={size_metric} (V={vars_count}, C={constr_count})")
        
        writer.writerow([n, m_played, vars_count, constr_count, elapsed, size_metric])
        results.append((n, elapsed, size_metric))

print(f"Benchmark finished. Data saved to {OUTPUT_CSV}")

