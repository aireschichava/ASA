Aqui está o conteúdo do PDF transformado em Markdown:

## [cite_start]INSTITUTO SUPERIOR TÉCNICO [cite: 1]
[cite_start]Análise e Síntese de Algoritmos [cite: 2]
[cite_start]2025/2026 [cite: 2]
[cite_start]2° Projecto [cite: 3]
[cite_start]Data enunciado: 5 de Dezembro de 2025 [cite: 4]
[cite_start]Data Limite de Entrega: 19 de Dezembro de 2025 [cite: 4]

## [cite_start]Descrição do Problema [cite: 5]
[cite_start]A empresa Entregas Caracol Lda. tem uma frota de camiões que fazem entregas entre um centro de distribuição no ponto $A$ e um centro de distribuição no ponto $B$ ($B$ diferente de $A$), numa certa área geográfica[cite: 6]. [cite_start]Cada centro de distribuição corresponde a um cruzamento no mapa, existem $N$ cruzamentos, e não existem pontes nem túneis na área de distribuição[cite: 7]. [cite_start]Todas as estradas na área de entrega são de sentido único e sabe-se que não existe nenhum caminho circular que permita regressar ao ponto de onde se partiu ou a um ponto por onde se passou anteriormente[cite: 8].

[cite_start]As frequentes obras nas estradas obrigam-nos a planear cada entrega com um algoritmo que depende do número de caminhos diferentes que existem entre o ponto $A$ e o ponto $B$[cite: 9]. [cite_start]Os camiões são numerados entre 1 e $M$, em cada dia, o número do camião que faz a entrega entre o ponto $A$ e o ponto $B$ é determinado calculando o número de caminhos diferentes para essa entrega, módulo $M$, mais um[cite: 9].
[cite_start]$$NumeroCamiaoParaCaminho(A,B) = 1+\#caminhos (A, B) \pmod M$$ [cite: 10]
[cite_start]Dado um mapa de estradas da área, representado na forma de um grafo [cite: 11][cite_start], a empresa Entregas Caracol Lda. quer calcular, eficientemente, quais as entregas que cada camião fará[cite: 12].

## [cite_start]Input [cite: 13]
[cite_start]O ficheiro de entrada contém toda a informação sobre o mapa da área[cite: 14]. [cite_start]Assim, o ficheiro de entrada é definido da seguinte forma[cite: 15]:

* [cite_start]Uma linha contendo um inteiro $N(\ge2)$ correspondendo ao número de cruzamentos[cite: 16].
* [cite_start]Uma linha contendo um inteiro $M(\ge2)$ correspondendo ao número de camiões[cite: 18].
* [cite_start]Uma linha contendo dois inteiros, $m_{1}$ e $m_{2}$, que representam a gama dos números de camiões para os quais se pretendem calcular as rotas[cite: 19].
* [cite_start]Uma linha contendo um inteiro $K(\ge1)$ correspondendo ao número de ligações directas entre cruzamentos[cite: 20].
* [cite_start]$K$ linhas, cada uma com dois inteiros $1\le a_{i}\le N$ e $1\le b_{i}\le N,$ que representam um caminho, orientado, entre os cruzamentos $a_{i}$ e $b_{i}$[cite: 21].

## [cite_start]Output [cite: 22]
[cite_start]O programa deverá imprimir para cada camião, entre $m_{1}$ e $m_{2}$, quais as rotas de entrega que lhe estão atribuídas[cite: 23]. [cite_start]Cada linha do output inicia-se com um '$C$' seguido do número do camião e um espaço, seguido por todos os pares $A,B$ por ordem lexicográfica[cite: 24]. [cite_start]Os elementos de cada par devem ser separados por uma vírgula e os pares são separados por um espaço e não devem ser incluídos os pares entre os quais não podem existir entregas[cite: 25].

---

| Exemplo 1 | Exemplo 2 |
| :--- | :--- |
| **Input** | **Input** |
| 5 | 7 |
| 3 | 4 |
| 1 3 | 2 4 |
| 8 | 10 |
| 1 4 | 1 5 |
| 1 3 | 1 2 |
| 1 2 | 1 6 |
| 4 3 | 2 6 |
| 4 2 | 2 3 |
| 3 2 | 2 7 |
| 2 5 | 3 7 |
| 3 5 | 3 4 |
| | 5 6 |
| | 6 7 |
| **Output** | **Output** |
| C1 1,5 4,5 | C2 1,2 1,3 1,4 1,5 1,7 2,3 2,4 2,6 3,4 3,7 5,6 5,7 6,7 |
| C2 1,2 1,4 2,5 3,2 4,3 | C3 |
| C3 1,3 3,5 4,2 | C4 1,6 2,7 |

---

## [cite_start]Implementação [cite: 28]
[cite_start]A implementação do projecto deverá ser feita preferencialmente usando a linguagem de programação C++[cite: 29]. [cite_start]Submissões nas linguagens Java/Python também serão aceites, embora fortemente desaconselhadas[cite: 30]. [cite_start]Alunos que o escolham fazer devem estar cientes de que submissões em Java/Python podem não passar todos os testes mesmo implementando o algoritmo correcto[cite: 31]. [cite_start]Mais se observa que soluções recursivas podem esgotar o limite da pilha quando executadas sobre os testes de maior tamanho, pelo que se recomenda a implementação de algoritmos iterativos[cite: 32]. [cite_start]O tempo necessário para implementar este projecto é inferior a 15 horas[cite: 33].

[cite_start]**Parâmetros de compilação:** [cite: 34]

* [cite_start]C++: `g++-std=c++11 -O3 -Wall file.cpp -lm` [cite: 35]
* [cite_start]C: `gcc -O3 -ansi -Wall file.c -lm` [cite: 36]
* [cite_start]Javac: `javac File.java` [cite: 37]
* [cite_start]Java: `java -Xss32m -Xmx256m -classpath` [cite: 38]
* [cite_start]Python: `python3 file.py` [cite: 39]
* [cite_start]Rust: `rustc -C opt-level=3 --edition=2021 file.rs` [cite: 41]

## [cite_start]Submissão do Projecto [cite: 42]
[cite_start]A submissão do projecto deverá incluir um relatório resumido e um ficheiro com o código fonte da solução[cite: 43]. [cite_start]Informação sobre as linguagens de programação possíveis está disponível no website do sistema Mooshak[cite: 44]. [cite_start]A linguagem de programação é identificada pela extensão do ficheiro[cite: 45]. [cite_start]Por exemplo, um projecto escrito em C deverá ter a extensão `.c`[cite: 46]. [cite_start]Após a compilação, o programa resultante deverá ler do standard input e escrever para o standard output[cite: 47]. [cite_start]Informação sobre as opções e restrições de compilação podem ser obtidas através do botão help do sistema Mooshak[cite: 48]. [cite_start]O comando de compilação não deverá produzir output, caso contrário será considerado um erro de compilação[cite: 49].

* [cite_start]**Relatório:** deverá ser submetido através do sistema Fénix no formato PDF com não mais de 2 páginas, fonte de 12pt, e 3cm de margem[cite: 50]. [cite_start]O relatório deverá incluir uma descrição da solução, a análise teórica e a avaliação experimental dos resultados[cite: 51]. [cite_start]O relatório deverá incluir qualquer referência que tenha sido utilizada na realização do projecto[cite: 52]. [cite_start]Relatórios que não sejam entregues em formato PDF terão nota 0[cite: 53]. [cite_start]Atempadamente será divulgado um *template* do relatório[cite: 53].
* [cite_start]**Código fonte:** deve ser submetido através do sistema Mooshak e o relatório (em formato PDF) deverá ser submetido através do Fénix[cite: 54]. [cite_start]O código fonte será avaliado automaticamente pelo sistema Mooshak ([http://acp.tecnico.ulisboa.pt/~mooshak/](http://acp.tecnico.ulisboa.pt/~mooshak/))[cite: 55]. [cite_start]Os alunos são encorajados a submeter, tão cedo quanto possível, soluções preliminares para o sistema Mooshak e para o Fénix[cite: 56]. [cite_start]Note que apenas a última submissão será considerada para efeitos de avaliação[cite: 58]. [cite_start]Todas as submissões anteriores serão ignoradas: tal inclui o código fonte e o relatório[cite: 59].

## [cite_start]Avaliação [cite: 60]
[cite_start]O projecto deverá ser realizado em grupos de um ou dois alunos e será avaliado em duas fases[cite: 61]. [cite_start]Na primeira fase, durante a submissão, cada implementação será executada num conjunto de testes, os quais representam 85% da nota final[cite: 62]. [cite_start]Na segunda fase, o relatório será avaliado[cite: 63]. [cite_start]A nota do relatório contribui com 15% da nota final[cite: 63].

### [cite_start]Avaliação Automática [cite: 64]
[cite_start]A primeira fase do projecto é avaliada automaticamente com um conjunto de testes, os quais são executados num computador com o sistema operativo GNU/Linux[cite: 65]. [cite_start]É essencial que o código fonte compile sem erros e respeite os standards de entrada e saída indicados anteriormente[cite: 66]. [cite_start]Os projectos que não respeitem os formatos especificados serão penalizados e poderão ter nota 0, caso falhem todos os testes[cite: 67]. [cite_start]Os testes não serão divulgados antes da submissão[cite: 68]. [cite_start]No entanto, todos os testes serão disponibilizados após o *deadline* para submissão do projecto[cite: 68]. [cite_start]Além de verificar a correcção do *output* produzido, o ambiente de avaliação restringe a memória e o tempo de execução disponíveis[cite: 69].

[cite_start]A maior parte dos testes executa o comando `diff` da forma seguinte[cite: 70]:
[cite_start]`diff output result` [cite: 71]

[cite_start]O ficheiro `result` contém o *output* gerado pelo executável a partir do ficheiro *input*[cite: 72]. [cite_start]O ficheiro `output` contém o *output* esperado[cite: 73]. [cite_start]Um programa passa num teste e recebe o valor correspondente, quando o comando `diff` não reporta quaisquer diferenças (i.e., não produz qualquer *output*)[cite: 73]. [cite_start]O sistema reporta um valor entre 0 e 170[cite: 74]. [cite_start]A nota obtida na classificação automática poderá sofrer eventuais cortes caso a análise do código demonstre recurso a soluções ajustadas a *inputs* concretos ou *outputs* aleatórios/constantes[cite: 75].

### [cite_start]Detecção de Cópias [cite: 76]
[cite_start]A avaliação dos projectos inclui um procedimento para detecção de cópias[cite: 77]. [cite_start]A submissão de um projecto implica um compromisso de que o trabalho foi realizado exclusivamente pelos alunos[cite: 78]. [cite_start]A violação deste compromisso ou a tentativa de submeter código que não foi desenvolvido pelo grupo implica a reprovação na unidade curricular, para todos os alunos envolvidos (incluindo os alunos que disponibilizaram o código)[cite: 79]. [cite_start]Qualquer tentativa de fraude, directa ou indirecta, será comunicada ao Conselho Pedagógico do IST, ao coordenador de curso, e será penalizada de acordo com as regras aprovadas pela Universidade e publicadas em "Diário da República"[cite: 80].

---

Se tiver alguma dúvida sobre o projeto ou precisar de ajuda com outro documento, por favor, me diga!