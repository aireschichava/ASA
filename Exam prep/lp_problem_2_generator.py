
import matplotlib.pyplot as plt
import numpy as np

# Define the feasible region constraints
# x1, x2 >= 0
x1 = np.linspace(0, 15, 400)

# Constraint 1: -x1 + x2 <= 5 => x2 <= x1 + 5
y1 = x1 + 5

# Constraint 2: 2x1 + x2 <= 20 => x2 <= 20 - 2x1
y2 = 20 - 2 * x1

# Constraint 3: x1 <= 8 (Vertical line)
# This doesn't map to y = f(x) easily for illing, but we handle it in the fill logic

# Plotting
plt.figure(figsize=(10, 10))

# Plot lines
plt.plot(x1, y1, label=r'$-x_1 + x_2 = 5$', color='blue')
plt.plot(x1, y2, label=r'$2x_1 + x_2 = 20$', color='red')
plt.axvline(x=8, label=r'$x_1 = 8$', color='green')

# Fill feasible region
# We need y <= y1 AND y <= y2 AND x <= 8 AND y >= 0
y_upper = np.minimum(y1, y2)
# Create a mask for x <= 8
mask = (x1 <= 8)
y_feasible = np.maximum(0, y_upper) # Ensure y >= 0

plt.fill_between(x1, 0, y_feasible, where=mask & (y_upper >= 0), color='gray', alpha=0.3, label='Feasible Region')

# Plot vertices
vertices = [
    (0, 0),
    (0, 5),   # Intersect x1=0, -x1+x2=5
    (5, 10),  # Intersect -x1+x2=5 and 2x1+x2=20
    (8, 4),   # Intersect 2x1+x2=20 and x1=8
    (8, 0)    # Intersect x1=8, x2=0
]

# Calculate Z for each vertex
for px, py in vertices:
    z = 3*px + py
    plt.plot(px, py, 'ko')
    plt.text(px + 0.2, py + 0.2, f'({px},{py})\nZ={z}', fontsize=11, weight='bold')

# Set axis limits
plt.xlim(-1, 12)
plt.ylim(-1, 22)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlabel('$x_1$', fontsize=12)
plt.ylabel('$x_2$', fontsize=12)
plt.title('Feasible Region Optimization\nMax Z = 3x1 + x2', fontsize=14)
plt.legend()

# Save the plot
plt.savefig('lp_problem_2.png')
