**Network Construction (Construction of Graph G):**

1.  **Nodes (Vertices):**
    *   Create a global `Source` node ($S$) and a global `Sink` node ($T$).
    *   Create a node $P_k$ for each Country ($k = 1 \dots m$).
    *   Create a node $F_j$ for each Factory ($j = 1 \dots n$).
    *   Create a node $C_i$ for each Child ($i = 1 \dots t$).

2.  **Edges (Arcs) & Capacities:**
    *   **Layer 1 (Source $\to$ Country):**
        *   Add edge $S \to P_k$ for every country.
        *   Capacity = $pmax_k$ (The environmental production limit of the country).

    *   **Layer 2 (Country $\to$ Factory):**
        *   Add edge $P_k \to F_j$ if Factory $F_j$ is located in Country $P_k$.
        *   Capacity = $fmax_j$ (The max stock of that specific factory).

    *   **Layer 3 (Factory $\to$ Child):**
        *   Add edge $F_j \to C_i$ if Factory $F_j$ is in the child's `wishes` list.
        *   Capacity = 1 (A single connection represents the potential transfer of 1 toy).

    *   **Layer 4 (Child $\to$ Sink):**
        *   Add edge $C_i \to T$ for every child.
        *   Capacity = 1 (This enforces the constraint that each child receives at most ONE toy total).

**Answer:**
Calculate the **Max Flow** from $S$ to $T$. The value of the Max Flow corresponds to the maximum number of children whose wish can be satisfied.
