# AI Coding Agent Instructions for ASA Projects

## Project Overview
This repository contains academic projects for the "Análise e Síntese de Algoritmos" (ASA) course at Instituto Superior Técnico. It includes two main algorithmic implementations:
- **Project 1** (`proj1/`): Dynamic programming for optimal aminoacid chain activation order
- **Project 2** (`EntregasCaracol/`): DAG path counting with batch optimization for truck route assignments

## Architecture & Data Flow
- **Core Algorithms**: C++ implementations using dynamic programming and graph traversal
- **Performance Testing**: Python scripts generate test cases, measure execution times, and plot results
- **Input/Output**: All programs read from stdin/write to stdout for Mooshak compatibility
- **Graph Representation**: Adjacency lists with in-degree tracking for topological sort

## Critical Developer Workflows

### Building & Running
```bash
# Project 2 (Entregas Caracol)
make  # or: g++ -std=c++17 -O3 -Wall main.cpp -o project
./project < tests/test1.in

# Project 1 (Aminoacid Chain)
g++ -std=c++17 -O3 -Wall proj1/projeto_ASA.cpp -o solver
./solver < proj1/input.txt
```

### Testing
```bash
# Run all tests with timing
./run_tests.sh

# Generate random test inputs
python3 gen_test.py 1000  # Project 2
g++ proj1/gerador_p1.cpp -o generator && ./generator 50 100 42  # Project 1
```

### Performance Analysis
```bash
# Full experiment suite (measures timing for multiple N values)
python3 full_experiment.py > timings.csv

# Plot results
python3 plot_graph.py  # generates performance_graph.png
```

## Project-Specific Patterns

### C++ Optimizations
- **Fast I/O**: Always use `ios_base::sync_with_stdio(false); cin.tie(NULL);`
- **Batch Processing**: Process nodes in blocks of 128 for cache locality (see `main.cpp` lines 75-150)
- **Lazy Reset**: Use visit tokens instead of clearing arrays (avoids O(N) resets)
- **Modular Arithmetic**: `if (val >= M) val -= M;` instead of `%` for performance
- **Memory Layout**: Serialize 2D arrays as 1D vectors for better cache usage

### Dynamic Programming Conventions
- **Table Structure**: `m[i][j]` stores optimal value for subproblem [i,j]
- **Split Tracking**: `s[i][j]` records the optimal split point k
- **Tie Breaking**: Choose lexicographically smallest removal order
- **Sentinel Nodes**: Virtual nodes at chain ends (type 'T', potential 1)

### Python Experimentation
- **Test Generation**: `gen_test.py` creates DAGs with controllable density
- **Timing Measurement**: Use `time.perf_counter()` for high-precision timing
- **Data Output**: Scripts print "RAW_DATA_START/END" markers for parsing

## Key Files & Directories
- `EntregasCaracol/main.cpp`: Core path counting algorithm with batch optimization
- `proj1/projeto_ASA.cpp`: DP solution for aminoacid chain
- `tests/`: Input files (.in) and expected outputs (.out)
- `full_experiment.py`: Automated performance benchmarking
- `plot_graph.py`: Log-log performance visualization
- `reports/`: HTML/Markdown documentation with LaTeX math

## Integration Points
- Python scripts invoke C++ binaries via subprocess
- Test runner (`run_tests.sh`) compares outputs with `diff -w`
- Performance data flows from experiments → CSV → plotting scripts
- All components use stdin/stdout for data exchange

## Common Pitfalls
- **Graph Cycles**: Always verify topological sort succeeds (N nodes in order)
- **Modulo Operations**: Handle negative results from modular arithmetic
- **Memory Limits**: O(N²) DP tables may exceed limits for large N
- **I/O Performance**: Fast I/O is critical for large test cases (N=3200)</content>
<parameter name="filePath">/Users/aireschichava/Tecnico-projects/ASA/.github/copilot-instructions.md