# ASA Project Report – Aminoacid Chain Optimisation

## Executive Summary
This report documents the structure, implementation details, and validation status of the first ASA project submission. The project delivers a dynamic-programming solver that computes the optimal activation order for an aminoacid chain, accompanied by a random test-instance generator. Compilation and execution were verified locally with the provided sample input.

## Project Overview
The repository targets the aminoacid chain optimisation task defined in the ASA syllabus. The solution is implemented in modern C++17 and comprises:
- **Solver:** `proj1/projeto_ASA.cpp`
- **Instance generator:** `proj1/gerador_p1.cpp`
- **Sample artefacts:** `proj1/input.txt` and `proj1/out.txt`

A pre-compiled binary and the default GitLab README template remain in the root of the repository.

## Solver Implementation
### Input Handling
The solver reads the chain length `n`, a sequence of `n` potentials, and a class string. Sentinel nodes of type `T` and unit potential are prepended and appended to simplify boundary interactions.

### Dynamic Programming Approach
A two-dimensional table `m[i][j]` stores the maximum potential attainable by removing the sub-chain in interval `[i, j]`. For each interval length the algorithm examines every split index `k`, solves the left and right subproblems, and adds the interaction contribution of `(i-1, k)` and `(k, j+1)` using the fixed 5×5 affinity matrix. The auxiliary table `s[i][j]` records the split achieving the best score.

### Deterministic Tie-Breaking
When multiple splits yield the same potential, the solver prefers the lexicographically smaller removal order. It compares post-order traversal sequences derived from candidate splits to enforce determinism.

### Output
The program prints the maximum potential on the first line and the chosen activation order (1-based positions) on the second line. Using the sample input in the repository, the solver outputs `20` and `1`.

## Instance Generator
`proj1/gerador_p1.cpp` accepts `<N> <Pmax> [seed]` and emits:
1. The chain length `N`.
2. A line with `N` potentials sampled uniformly in `[1, Pmax]`.
3. A line with a random class string over the alphabet `P, N, A, B`.

The optional seed argument enables reproducible test cases for stress testing and benchmarking.

## Validation
The solver was compiled with:
```
g++ -std=c++17 -O3 -Wall projeto_ASA.cpp -o solver
```
and executed against `proj1/input.txt`:
```
./solver < input.txt
```
The output matches the documented `proj1/out.txt`, confirming correct behaviour on the sample scenario.

## Repository Assessment
- **Strengths:** Clear separation between solver and generator, efficient `O(n^3)` dynamic programming solution, deterministic tie-breaking, and reproducible sample data.
- **Limitations:** The generator omits several standard headers and may fail on stricter toolchains; the repository includes a compiled binary; the README remains the GitLab boilerplate; no automated tests or build scripts are provided.


## Conclusion
The submission satisfies the core requirements of the ASA aminoacid chain project: it delivers a performant solver with deterministic outputs and an accompanying data generator. Addressing the listed recommendations would further enhance maintainability and reproducibility for evaluation.
