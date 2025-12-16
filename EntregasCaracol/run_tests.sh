#!/bin/bash

set -euo pipefail

make -s

printf '%s\n' 'Running tests...'
printf '%s\n' '--------------------------------'

for input in tests/test*.in; do
    [ -e "$input" ] || continue
    testname=$(basename "${input%.in}")
    output="tests/${testname}.out"
    myoutput="tests/my_${testname}.out"

    if [ ! -f "$output" ]; then
        printf 'Warning: no expected output for %s\n' "$input"
        continue
    fi

    start=$(date +%s%N)
    ./project < "$input" > "$myoutput"
    end=$(date +%s%N)
    duration=$(((end - start) / 1000000))

    if diff -w "$myoutput" "$output" >/dev/null; then
        printf '[PASS] %s (%dms)\n' "$testname" "$duration"
        rm -f "$myoutput"
    else
        printf '[FAIL] %s\n' "$testname"
        printf 'Expected vs Actual (first 10 lines):\n'
        diff "$myoutput" "$output" | head -n 10
    fi
done

printf '%s\n' '--------------------------------'
printf '%s\n' 'Done.'
