import subprocess
import sys

# Test cases provided by user
tests = [
    ("ImpossibleCatchup", "3 4\n1 2 2\n2 1 2\n1 3 2\n3 1 2", "-1\n0\n0"),
    ("DesperateCatchup", "3 3\n1 2 2\n1 3 3\n2 3 0", "2\n0\n0"),
    ("CleanSlate", "3 0", "0\n0\n0"),
    ("AlreadyWon", "3 4\n1 2 1\n2 1 1\n1 3 1\n3 1 1", "0\n-1\n-1"),
]

print("Running Logic Checks...")
failed = False
for name, inp, exp in tests:
    try:
        res = subprocess.run([sys.executable, 'main.py'], input=inp, text=True, capture_output=True)
        out = res.stdout.strip()
        
        # Normalize for comparison
        out_lines = [l.strip() for l in out.splitlines() if l.strip()]
        exp_lines = [l.strip() for l in exp.splitlines() if l.strip()]
        
        if out_lines == exp_lines:
            print(f"✅ {name}: {out_lines}")
        else:
            print(f"❌ {name}: Expected {exp_lines}, Got {out_lines}")
            failed = True
    except Exception as e:
        print(f"❌ {name}: Exception {e}")
        failed = True

if failed:
    sys.exit(1)
print("All Logic Checks Passed.")
