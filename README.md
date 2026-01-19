# ASA – Análise e Síntese de Algoritmos

> **Analysis and Synthesis of Algorithms**  
> Instituto Superior Técnico, University of Lisbon  
> **Authors:** Aires Nélio Chichava, Samuel Gomes de Andrade

This repository contains the projects developed for the **Analysis and Synthesis of Algorithms (ASA)** course. The projects cover various algorithmic domains including **Dynamic Programming**, **Graph Algorithms**, and **Linear Programming**.

---

## 📚 Projects Overview

| Project | Title | Topic | Tech Stack |
| :--- | :--- | :--- | :--- |
| **Project 1** | Aminoacid Chain Optimisation | Dynamic Programming | C++ |
| **Project 2** | Entregas Caracol Lda. | Graph Theory (DAGs) | C++ |
| **Project 3** | Football Championship Scenarios | Linear Programming | Python (PuLP) |

---

## 🧬 Project 1: Aminoacid Chain Optimisation

### Overview
This project solves the "Optimal Activation Order" problem for an amino acid chain using **Dynamic Programming**. The goal is to determine the sequence of removals that maximizes the total potential energy produced.

### Key Features
- **Algorithm**: $O(n^3)$ Dynamic Programming approach.
- **Optimization**: Handles custom affinity matrices and potential values.
- **Tie-Breaking**: Lexicographical order enforcement.

### Building and Running
```bash
# Compile
g++ -std=c++17 -O3 -Wall proj1/projeto_ASA.cpp -o solver

# Run
./solver < proj1/input.txt
```

---

## 🐌 Project 2: Entregas Caracol Lda.

### Overview
This project models a distribution network as a **Directed Acyclic Graph (DAG)** to optimize logistics. It calculates delivery routes for a fleet of trucks based on the number of distinct paths between intersections (nodes).

### Key Features
- **Algorithm**: Topological Sort + DP Path Counting.
- **Complexity**: $O(N(N+E))$ with batch processing optimization.
- **Performance**: Handles >3000 nodes and 1.5M edges in under 5s.

### Building and Running
```bash
# Compile
cd EntregasCaracol
make

# Run
./project < tests/test1.in
```

### Architecture
```
[Input Graph] -> [Topological Sort] -> [Batch Path Counting] -> [Route Assignment] -> [Output]
```

---

## ⚽ Project 3: Football Championship Scenarios

### Overview
This project uses **Linear Programming (LP)** to analyze football championship outcomes. Given the current standings and remaining matches, it determines the minimum number of wins required for each team to theoretically win the championship.

### Key Features
- **Algorithm**: Linear Programming formulation (minimization objective).
- **Library**: `PuLP` (Python).
- **Optimization**: Constraint pruning for impossible catch-up scenarios.

### Building and Running
```bash
# Requirements
pip install pulp

# Run
python3 proj3/main.py < proj3/input.txt
```

---

## 📝 License
This is an academic project developed for the **Análise e Síntese de Algoritmos** course at Instituto Superior Técnico.
