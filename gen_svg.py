import math

data = [
    (100, 0.006),
    (200, 0.016),
    (400, 0.055),
    (800, 0.224),
    (1600, 0.964),
    (3200, 4.320)
]

width = 600
height = 400
margin = 60

# We transform X to N^3
points = [(n**3, t) for n, t in data]

min_x = 0
max_x = 3200**3 * 1.05 # slightly larger than max for padding
min_y = 0
max_y = 4.5

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
    # Label N values
    n_val = data[i][0]
    # Adjust label position to avoid overlap
    dy = -15 if i != 0 else -15
    svg.append(f'<text x="{px}" y="{py+dy}" font-family="Arial" font-size="10" text-anchor="middle">N={n_val}</text>')

svg.append(f'<polyline points="{" ".join(points_svg)}" fill="none" stroke="#0072BD" stroke-width="2"/>')

# X Axis Labels
ticks_x = 4
for i in range(ticks_x + 1):
    val = (i / ticks_x) * max_x
    px, _ = transform(val, min_y)
    svg.append(f'<line x1="{px}" y1="{height-margin}" x2="{px}" y2="{height-margin+5}" stroke="black"/>')
    label = f"{val/1e10:.1f}e10" if val != 0 else "0"
    svg.append(f'<text x="{px}" y="{height-margin+20}" font-family="Arial" font-size="12" text-anchor="middle">{label}</text>')

# Y Axis Labels
ticks_y = 5
for i in range(ticks_y + 1):
    val = (i / ticks_y) * max_y
    _, py = transform(min_x, val)
    svg.append(f'<line x1="{margin}" y1="{py}" x2="{margin-5}" y2="{py}" stroke="black"/>')
    svg.append(f'<text x="{margin-10}" y="{py+4}" font-family="Arial" font-size="12" text-anchor="end">{val:.1f}</text>')

# Titles
svg.append(f'<text x="{width/2}" y="{height-5}" font-family="Arial" font-size="12" text-anchor="middle">N^3</text>')
svg.append(f'<text x="{15}" y="{height/2}" font-family="Arial" font-size="12" text-anchor="middle" transform="rotate(-90 15, {height/2})">Time (s)</text>')
svg.append(f'<text x="{width/2}" y="{30}" font-family="Arial" font-size="16" text-anchor="middle">Time vs N^3 (Linear)</text>')

svg.append('</svg>')

with open('performance_graph.svg', 'w') as f:
    f.write('\n'.join(svg))

print("Generated performance_graph.svg")
