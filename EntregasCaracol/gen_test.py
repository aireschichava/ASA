import random
import sys

def generate_dag(n, m_trucks, density=0.3):
    print(f"{n}")
    print(f"{m_trucks}")
    # m1, m2 range
    m1 = 1
    m2 = m_trucks
    print(f"{m1} {m2}")
    
    edges = []
    # Force DAG: edge only from u to v where u < v
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if random.random() < density:
                edges.append((i, j))
                
    print(f"{len(edges)}")
    for u, v in edges:
        print(f"{u} {v}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 100
    generate_dag(n, 10)
