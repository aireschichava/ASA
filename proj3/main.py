from pulp import *
import sys
import os
import contextlib

# High recursion limit for deep recursion in library code
sys.setrecursionlimit(100000)

@contextlib.contextmanager
def suppress_stdout_stderr():
    """
    A context manager that redirects stdout and stderr to devnull
    at the file descriptor level. This silences C extensions and subprocesses.
    """
    try:
        # Open devnull
        with open(os.devnull, 'w') as fnull:
            # Save original file descriptors
            old_stdout = os.dup(1)
            old_stderr = os.dup(2)
            try:
                # Redirect 1 and 2 to fnull
                os.dup2(fnull.fileno(), 1)
                os.dup2(fnull.fileno(), 2)
                yield
            finally:
                # Restore original file descriptors
                os.dup2(old_stdout, 1)
                os.dup2(old_stderr, 2)
                # Close the saved copies
                os.close(old_stdout)
                os.close(old_stderr)
    except Exception:
        yield

def solve_for_team(team_id, n, matches, scores, current_leader_score, potential_points):
    """
    Solve LP for a specific team.
    Returns: min wins or -1
    """

    # Optimization: Prune if mathematically impossible to catch current leader
    if scores[team_id - 1] + potential_points[team_id - 1] < current_leader_score:
        return -1

    # No remaining matches? Check strict points
    if not matches:
        return 0 if scores[team_id - 1] >= current_leader_score else -1

    prob = LpProblem(f"MinWins_{team_id}", LpMinimize)
    
    match_vars = {}
    
    # Create variables
    for idx, (h, a) in enumerate(matches):
        w = LpVariable(f"w{idx}", cat=LpBinary)
        t = LpVariable(f"t{idx}", cat=LpBinary)
        l = LpVariable(f"l{idx}", cat=LpBinary)
        match_vars[(h, a)] = (w, t, l)
        prob += w + t + l == 1

    # Objective: Minimize wins for team_id
    section_wins = []
    
    for (h, a), (w, t, l) in match_vars.items():
        if h == team_id:
            section_wins.append(w)
        elif a == team_id:
            section_wins.append(l)
            
    prob += lpSum(section_wins)

    # Constraints: Team ID points >= Other points
    gained_points = {t: [] for t in range(1, n + 1)}
    
    for (h, a), (w, t, l) in match_vars.items():
        gained_points[h].append(3 * w + t)
        gained_points[a].append(3 * l + t)
        
    for other in range(1, n + 1):
        if other == team_id:
            continue
            
        # Optimization: Constraint Pruning
        # If I am already guaranteed to finish above 'other' (my current > their max potential),
        # then this constraint is always satisfied.
        if scores[team_id - 1] >= scores[other - 1] + potential_points[other - 1]:
            continue

        prob += (scores[team_id - 1] + lpSum(gained_points[team_id])) >= \
                (scores[other - 1] + lpSum(gained_points[other]))

    # Solver Strategy: Use default solver with deep silencing
    try:
        with suppress_stdout_stderr():
             # Try GLPK first (no CMD, let PuLP find it) or default CBC
             prob.solve()
    except Exception:
        return -1

    if LpStatus[prob.status] == "Optimal":
        obj_val = value(prob.objective)
        # Handle edge case: empty objective (team not in any remaining matches)
        if obj_val is None:
            return 0
        return int(round(obj_val))
    return -1

def main():
    try:
        input_data = sys.stdin.read().split()
    except Exception:
        return

    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    scores = [0] * n
    played_set = set()
    
    # Process played games
    for _ in range(m):
        try:
            h = int(next(iterator))
            a = int(next(iterator))
            r = int(next(iterator))
            
            if h < 1 or h > n or a < 1 or a > n:
                continue
                
            played_set.add((h, a))
            
            if h == r:
                scores[h-1] += 3
            elif a == r:
                scores[a-1] += 3
            else:
                scores[h-1] += 1
                scores[a-1] += 1
        except StopIteration:
            break

    # Identify remaining matches
    remaining_matches = []
    potential_points = [0] * n 
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j: 
                continue
            if (i, j) not in played_set:
                remaining_matches.append((i, j))
                potential_points[i-1] += 3 
                potential_points[j-1] += 3 

    current_leader_score = max(scores) if scores else 0

    # Solve for each team
    for i in range(1, n + 1):
        try:
            val = solve_for_team(i, n, remaining_matches, scores, current_leader_score, potential_points)
            print(val)
        except Exception:
            print("-1")

if __name__ == '__main__':
    main()
