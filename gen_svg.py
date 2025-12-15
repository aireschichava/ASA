import math

# Data format: (N, K, Time)
# Excluding N=100 outlier
data = [
    (200, 5937, 0.0172),
    (300, 13620, 0.0326),
    (400, 24075, 0.0595),
    (500, 37572, 0.0930),
    (600, 53856, 0.1348),
    (800, 96280, 0.2466),
    (1000, 149645, 0.3608),
    (1200, 215511, 0.5350),
    (1400, 294370, 0.7506),
    (1600, 384045, 0.9868),
    (2000, 599803, 1.6834),
    (2200, 724530, 1.9516)
]

width = 600
height = 400
margin = 80

# Transform X to Theoretical Complexity: N * (N + K)
points = [(n * (n + k), t) for n, k, t in data]

# Find bounds
min_x = points[0][0]
max_x = points[-1][0] * 1.05
min_y = 0
max_y = points[-1][1] * 1.1

def transform(x, y):
    # Linear scaling
    px = margin + (x - min_x) / (max_x - min_x) * (width - 2 * margin)
    py = height - margin - (y - min_y) / (max_y - min_y) * (height - 2 * margin)
    return px, py

svg = [f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">']
svg.append(f'<rect width="100%" height="100%" fill="white"/>')

# Axes
svg.append(f'<line x1="{margin}" y1="{height-margin}" x2="{width-margin}" y2="{height-margin}" stroke="black" stroke-width="2"/>') # X
svg.append(f'<line x1="{margin}" y1="{height-margin}" x2="{margin}" y2="{margin}" stroke="black" stroke-width="2"/>') # Y

# Points and Line
points_svg = []
for i, (x_val, y_val) in enumerate(points):
    px, py = transform(x_val, y_val)
    points_svg.append(f'{px},{py}')
    svg.append(f'<circle cx="{px}" cy="{py}" r="4" fill="#0072BD"/>') # Blue dots
    
    # Label specific N values for context (first, middle, last)
    if i == 0 or i == len(points)//2 or i == len(points)-1:
        n_val = data[i][0]
        svg.append(f'<text x="{px}" y="{py-10}" font-family="Arial" font-size="10" text-anchor="middle">N={n_val}</text>')

svg.append(f'<polyline points="{" ".join(points_svg)}" fill="none" stroke="#0072BD" stroke-width="2"/>')

# X Axis Labels (Scientific Notation)
ticks_x = 4
for i in range(ticks_x + 1):
    val = min_x + (max_x - min_x) * (i / ticks_x)
    px, _ = transform(val, min_y)
    svg.append(f'<line x1="{px}" y1="{height-margin}" x2="{px}" y2="{height-margin+5}" stroke="black"/>')
    # Format: 1.5e9
    label = f"{val:.1e}"
    svg.append(f'<text x="{px}" y="{height-margin+20}" font-family="Arial" font-size="10" text-anchor="middle">{label}</text>')

# Y Axis Labels
ticks_y = 5
for i in range(ticks_y + 1):
    val = (i / ticks_y) * max_y
    _, py = transform(min_x, val)
    svg.append(f'<line x1="{margin}" y1="{py}" x2="{margin-5}" y2="{py}" stroke="black"/>')
    svg.append(f'<text x="{margin-10}" y="{py+4}" font-family="Arial" font-size="12" text-anchor="end">{val:.1f}</text>')

# Titles and Axis Names
svg.append(f'<text x="{width/2}" y="{height-5}" font-family="Arial" font-size="12" text-anchor="middle">Theoretical Complexity: N * (N + K)</text>')
svg.append(f'<text x="{20}" y="{height/2}" font-family="Arial" font-size="12" text-anchor="middle" transform="rotate(-90 20, {height/2})">Time (s)</text>')
svg.append(f'<text x="{width/2}" y="{30}" font-family="Arial" font-size="16" text-anchor="middle">Time vs Complexity (Linear)</text>')

svg.append('</svg>')

with open('performance_graph.svg', 'w') as f:
    f.write('\n'.join(svg))

print("Generated performance_graph.svg")
