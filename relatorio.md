# Relatório do Projecto - Entregas Caracol Lda

## 1. Descrição da Solução
O problema consiste em calcular o número de caminhos distintos entre todos os pares de cruzamentos $(A, B)$ num mapa de sentido único (Grafo Acíclico Dirigido – DAG) e atribuir rotas a camiões com base nesse valor.

A solução, implementada em C++, é totalmente iterativa e evita abordagens exponenciais/subexpoenciais. Os passos são:

1. **Ordenação Topológica (Kahn)**
   - Lineariza o grafo para garantir que, ao visitar um nó $u$, todos os predecessores já foram processados.
   - Complexidade: $O(N + E)$.

2. **Programação Dinâmica por Lotes**
    - Os nós origem são processados em blocos de até 128 vértices (`BATCH_SIZE`).
    - Para cada lote inicializa-se um arranjo serializado `batch_counts[u * BATCH_SIZE + k]` que acumula o número de caminhos entre a origem $(start\_base + k)$ e o nó $u$.
   - Um vetor `batch_reachable` e um mecanismo de tokens evitam limpar toda a matriz entre lotes; apenas as fatias usadas são reinicializadas.
   - A propagação segue a ordem topológica, somando contagens módulo $M$ e marcando como alcançáveis os destinos.

3. **Atribuição de Camiões e Saída**
   - Para cada par $(S, T)$ alcançável, calcula-se $truck(S,T) = 1 + (\text{caminhos}(S,T) \bmod M)$.
   - As rotas de camiões em $[m_1, m_2]$ são guardadas em vetores de pares, posteriormente ordenados lexicograficamente.

### Pseudocódigo de alto nível
```
KahnTopoOrder(G):
    compute in_degree
    queue q = vertices with in_degree 0
    topo = []
    while q not empty:
        u = pop(q); topo.append(u)
        for v in adj[u]:
            if --in_degree[v] == 0: push(q, v)
    return topo

Solve(G):
    topo = KahnTopoOrder(G)
    for each batch B of sources in topo order:
        init_batch_slices(B)
        for u in topo starting at first element of B:
            if u not touched by B: continue
            record deliveries for reachable pairs (source in B, u)
            propagate counts from u to each v in adj[u]
    sort and print routes per truck
```

## 2. Análise Teórica

### Complexidade Temporal
A ordenação topológica é $O(N+E)$. A propagação por lotes executa, para cada origem, um percurso sobre o subgrafo alcançável: em média é $O(N+E)$ por lote, resultando numa complexidade global

$$O(N \times (N + E))$$

No extremo denso ($E \approx N^2$) isto comporta-se como $O(N^3)$; em grafos esparsos aproxima-se de $O(N^2)$. Os testes empíricos confirmam que a solução é adequada aos limites esperados e evita crescimento exponencial/subexpoencial.

### Complexidade Espacial
- **Grafo (Lista de Adjacências)**: $O(N + E)$.
- **Estruturas Auxiliares (DP)**: Vetores `batch_counts`, `batch_reachable`, `visit_token`, `topo_order` ocupam $O(N \times \text{BATCH\_SIZE})$; com `BATCH_SIZE = 128` isto permanece linear na prática.
- **Armazenamento de Rotas (Output)**: No pior caso, todos os pares $(A, B)$ são válidos. Existem $N(N-1)/2$ pares possíveis. Logo, o espaço para armazenar a saída é $O(N^2)$.

Complexidade Espacial Total: $O(N^2 + E)$.

## 3. Avaliação Experimental

![Tempo vs N³](performance_graph.png)

### Resultados Experimentais
Os tempos foram medidos num MacBook Pro (macOS, CPU Apple M-series) executando `./project` sobre DAGs gerados por `python3 gen_test.py N` (densidade padrão de 0.3). Cada instância é alimentada diretamente no binário, e o tempo é obtido com `time.perf_counter`. Os valores completos estão em `timings.csv`.

| $N$ | Tempo (s) | Ratio ($T_N / T_{N/2}$) |
| :--- | :--- | :--- |
| 100 | 0.006 | - |
| 200 | 0.016 | 2.6x |
| 400 | 0.055 | 3.4x |
| 800 | 0.224 | 4.1x |
| 1600 | 0.964 | 4.3x |
| 3200 | 4.320 | 4.5x |

**Análise**: Conforme $N$ duplica, o tempo cresce entre 3x–4.5x, refletindo o termo $O(N \times (N + E))$. Os grafos gerados tornam-se densos à medida que $N$ cresce, logo $E \propto N^2$ e o comportamento aproxima-se de $O(N^3)$, tal como previsto. Ainda assim, a solução processa facilmente instâncias até $N=3200$, cumprindo folgadamente o limite temporal.

Os testes automáticos incluem os exemplos oficiais, casos limite (grafo mínimo, componentes desconexas, múltiplas instâncias no mesmo ficheiro, cenários de $M$ modular) e grafos aleatórios de maior dimensão, assegurando robustez e correção do output.
