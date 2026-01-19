
# Learning Style and Key Patterns for User

## Learning Style
- **Visual & Intuitive:** The user learns best through visual analogies (e.g., "Robot Finger" for flow verification, "Building Walls" for DP).
- **Example-Driven:** Prefers walking through a concrete example (like "D(4,4)=3") rather than abstract math definitions.
- **Plain Text Preference:** Strongly dislikes raw LaTeX math symbols; understanding breaks down when formatting codes appear.
- **De-mystification:** Needs "Exam Phrasing" translated into "Plain English" logic. Once the translation is done (e.g., "Error in BFS" -> "Swap variable in formula"), the user grasps the solution instantly.
- **Pattern Recognition:** Effective at identifying patterns once they are explicitly pointed out (e.g., spotting 0-indexing issues, recognizing heuristics).

## Important Exam Patterns & Heuristics Discovered
### Linear Programming (LP)
- **Constraint Ignoring:** User has a dangerous tendency to ignore "large number" constraints (e.g., `2x + y <= 20` vs `x <= 8`).
    - *Correction:* Must draw lines to see slope; steep lines with large RHS often "cut" the feasible region.
- **Strong Duality:** If asked for Dual solution "from the Primal", copy the Objective Value directly. No new math needed.
- **Graphing:** Always verify intercepts on *both* axes.
- **Standard Form:** Easier to draw; convert to `<=` for maximization before plotting.

### Network Flow (Edmonds-Karp)
- **Complexity Trick:** `Total = (Augmentations) * (Search Cost)`.
    - `Augmentations` is always `V*E`.
    - If exam says "BFS is V^2", just multiply `(V*E) * (V^2)`.
- **Invalid State Detection:** "The Leaking Bucket".
    - Visit nodes one by one (ignore Source/Sink).
    - `Flow IN` must equal `Flow OUT`.
    - Focus on "busy" nodes first.

### Dynamic Programming (Grid Problems)
- **Local Definition:** `D(i,j)` usually means "Best solution ENDING at (i,j)".
- **Square Building Logic:** `1 + min(Top, Left, Diagonal)`.
    - Using `min` because the shape is limited by its shortest side.
- **Interpretation:** "1-indexed Grid" vs "0-indexed DP Matrix" usually implies a padding row/col of zeros.
- **Initialization:** If formula uses `i-1`, code must manually set Row 0/Col 0 to avoid crashes.

## Actionable Strategy
1.  **Read:** Breakdown Portuguese phrasing into "Variable Assignments".
2.  **Visualize:** Draw/Scan graphs physically (finger tracing).
3.  **Sanity Check:** Test boundaries (0s, border cases) before writing formulas.
