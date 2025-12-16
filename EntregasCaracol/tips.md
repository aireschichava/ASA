O Segundo Projeto de Análise e Síntese de Algoritmos (ASA) do ano letivo 2025/2026, intitulado "Entregas Caracol Lda.", foca-se na **contagem eficiente do número de caminhos** num grafo dirigido acíclico (DAG) e na atribuição de rotas a uma frota de camiões com base nessa contagem.

### O que é Requerido no Projeto

O problema baseia-se num mapa de estradas representado por um grafo dirigido, onde os cruzamentos são os nós, e as estradas são arcos de sentido único. O mapa é caracterizado pela ausência de caminhos circulares, o que o torna um Grafo Acíclico Dirigido (DAG).

O objetivo é **calcular quais as entregas que cada camião fará**.

**A Atribuição de Camiões**
O número do camião responsável por uma entrega entre um ponto $A$ e um ponto $B$ é determinado pelo número de caminhos distintos entre $A$ e $B$, seguindo a fórmula:
$$ \text{NúmeroCamiãoParaCaminho}(A, B) = 1 + (\#\text{caminhos}(A, B) \pmod M) $$
Onde $M$ é o número total de camiões disponíveis.

**Input e Output**
O programa recebe os seguintes parâmetros de *input*:
1. Um inteiro $N$ (número de cruzamentos, $\ge 2$).
2. Um inteiro $M$ (número de camiões, $\ge 2$).
3. Dois inteiros $m_1$ e $m_2$, que definem a gama de camiões para os quais as rotas devem ser calculadas.
4. Um inteiro $K$ (número de ligações diretas).
5. $K$ linhas descrevendo os caminhos orientados $(a_i, b_i)$.

O *output* deve ser formatado para cada camião no intervalo $[m_1, m_2]$. Cada linha começa com 'C' seguido do número do camião, e depois todos os pares $(A, B)$ atribuídos a esse camião, por ordem lexicográfica. Os pares são separados por vírgula e espaço.

### Como Implementar o Projeto

A solução eficiente para este problema num DAG requer a aplicação de **Programação Dinâmica** (PD) em conjunto com a **Ordenação Topológica** do grafo.

A abordagem recomendada é dividida em etapas:

1.  **Ordenação Topológica:**
    *   É essencial linearizar o grafo para garantir que, ao processar um nó de origem $u$, as contagens de caminhos possam ser propagadas de forma segura para os seus vizinhos $v$.
    *   A solução pode utilizar um algoritmo como o **Algoritmo de Kahn** (mencionado no relatório) para obter esta ordem.
    *   A complexidade desta etapa é $O(N + E)$, onde $N$ é o número de nós e $E$ o número de arestas.

2.  **Contagem de Caminhos (Programação Dinâmica):**
    *   O algoritmo itera sobre cada nó $S$ (origem) de 1 a $N$.
    *   Para cada origem $S$, o número de caminhos para todos os destinos alcançáveis $T$ é calculado.
    *   Utiliza-se um vetor auxiliar, como `count_paths`, onde `count_paths[v]` armazena o número de caminhos de $S$ até $v$.
    *   A propagação da contagem é feita seguindo a ordem topológica: para cada nó $u$, adiciona-se o valor `count_paths[u]` a `count_paths[v]` para todos os vizinhos $v$ de $u$.
    *   Uma otimização de espaço crucial é a reutilização do vetor `count_paths` em cada iteração de nó origem, mantendo o uso de memória da PD em $O(N)$ para as estruturas auxiliares.

3.  **Atribuição e Armazenamento:**
    *   Após calcular o número de caminhos para um par $(S, T)$, calcula-se o número do camião como $1 + (\text{caminhos}(S, T) \pmod M)$.
    *   Apenas são armazenadas as rotas se o camião estiver dentro do intervalo $[m_1, m_2]$.

**Complexidade do Algoritmo**

A complexidade temporal total é dominada pela etapa de contagem de caminhos, que executa $N$ vezes a travessia do grafo (uma para cada nó origem).

*   A complexidade teórica é dada por **$O(N \times (N + E))$**.
*   No pior caso (grafo denso, onde $E \approx N^2$), a complexidade aproxima-se de **$O(N^3)$**.
*   Em grafos esparsos, a complexidade aproxima-se de $O(N^2)$.

**Notas de Implementação**

Recomenda-se a implementação de **algoritmos iterativos** (em vez de recursivos) para evitar o esgotamento do limite da pilha (stack limit) nos testes de maior dimensão. Embora o C++ seja a linguagem de preferência, as submissões em Java/Python são aceites, mas desaconselhadas por poderem não passar todos os testes.

O processo de resolução é análogo a planear uma viagem de metro numa cidade que só avança, sem voltas. O *chef* de planeamento, para cada ponto de partida, percorre a cidade na ordem correta (topológica) e, ao chegar a um cruzamento, ele sabe quantos caminhos existem até ali. Ele adiciona essa contagem a todos os próximos cruzamentos, garantindo que o número total de rotas é calculado de forma cumulativa e eficiente.