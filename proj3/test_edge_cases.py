#!/usr/bin/env python3
import subprocess

tests = [
    ("Ex1", "3 1\n1 2 2", "1\n0\n1"),
    ("Ex2", "3 4\n1 2 2\n2 1 2\n1 3 3\n3 1 3", "-1\n0\n0"),
    ("Ex3", "3 3\n1 2 2\n1 3 3\n2 3 0", "2\n0\n0"), # Draw case
    ("TeamWonAll", "3 3\n1 2 1\n1 3 1\n2 3 2", "0\n1\n2"),
]

print("Running minimal check...")
for name, inp, exp in tests:
    res = subprocess.run(['python3', 'main.py'], input=inp, text=True, capture_output=True)
    out = res.stdout.strip()
    if out == exp:
        print(f"✅ {name}")
    else:
        print(f"❌ {name}: Expected {exp.replace('\n', ',')}, Got {out.replace('\n', ',')}")
        print(f"Stderr: {res.stderr}")

print("Done.")
