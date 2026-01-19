# Official Solution: Group II, Question 1

## a. Standard Form Formulation
To convert to standard form, we ensure RHS is positive and add slack variables to make inequalities into equalities.

**Original Constraints (Fixed Signs):**
1.  $-x_1 + x_2 \le 2$
2.  $x_1 + 2x_2 \le 7$
3.  $2x_1 + x_2 \le 8$

**Standard Form:**
**Maximize** $Z = -2x_1 + x_2$
**Subject to:**
$$
\begin{cases}
-x_1 + x_2 + s_1 = 2 \\
x_1 + 2x_2 + s_2 = 7 \\
2x_1 + x_2 + s_3 = 8 \\
x_1, x_2, s_1, s_2, s_3 \ge 0
\end{cases}
$$

---

## b. Dual Formulation
We use the corrected (canonical) inequalities to form the Dual.
*   Primal Objectives $(-2, 1)$ become Dual RHS.
*   Primal RHS $(2, 7, 8)$ become Dual Objectives.
*   Primal $\le$ constraints become Dual variables $\ge 0$.
*   Primal Max becomes Dual Min.

**Minimize** $W = 2y_1 + 7y_2 + 8y_3$
**Subject to:**
$$
\begin{cases}
-y_1 + y_2 + 2y_3 \ge -2 \\
y_1 + 2y_2 + y_3 \ge 1 \\
y_1, y_2, y_3 \ge 0
\end{cases}
$$

---

## c. Geometric Solution

### 1. Vertices of Feasible Region
We plot the lines and find the polygon vertices by intersecting the boundaries:
*   **Point A (0, 2):** Intersection of Y-axis ($x_1=0$) and Line 1 ($-x_1+x_2=2$).
*   **Point B (1, 3):** Intersection of Line 1 ($-x_1+x_2=2$) and Line 2 ($x_1+2x_2=7$).
    *   Sum equations: $3x_2 = 9 \Rightarrow x_2=3$. Then $-x_1+3=2 \Rightarrow x_1=1$.
*   **Point C (3, 2):** Intersection of Line 2 ($x_1+2x_2=7$) and Line 3 ($2x_1+x_2=8$).
    *   Solve system: $x_1=3, x_2=2$.
*   **Point D (4, 0):** Intersection of X-axis ($x_2=0$) and Line 3 ($2x_1=8$).
*   **Point E (0, 0):** Origin.

### 2. Testing Objective Value ($Z = -2x_1 + x_2$)
*   At (0, 0): 0
*   At (0, 2): $-2(0) + 2 = \mathbf{2}$  **(MAXIMUM)**
*   At (1, 3): $-2(1) + 3 = 1$
*   At (3, 2): $-2(3) + 2 = -4$
*   At (4, 0): $-8$

### Final Answer:
*   **Maximum Value:** 2
*   **Coordinates:** $(x_1, x_2) = (0, 2)$
*   **Bounding Equations:** $-x_1 + x_2 \le 2$, $x_1 + 2x_2 \le 7$, $2x_1 + x_2 \le 8$, $x_1, x_2 \ge 0$.
