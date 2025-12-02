//g++ -std=c++11 -O3 -Wall solution.cpp -lm -o solution
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int n;
struct Node {
  int pot;
  int type;
};

vector<Node> chain;
vector<vector<long long>> m;
vector<vector<int>> s;

// tabela de afinidades
int affinity[5][5] = {
  {1, 3, 1, 3, 1}, 
  {5, 1, 0, 1, 1}, 
  {0, 1, 0, 4, 1}, 
  {1, 3, 2, 3, 1}, 
  {1, 1, 1, 1, 1}  
};

// ordenado lexicograficamente e numericamente tmb (vai dar jeito mais tarde mas n importa mt)
int get_type_id(char c) {
  if (c == 'P') return 0;
  if (c == 'N') return 1;
  if (c == 'A') return 2;
  if (c == 'B') return 3;
  return 4; // devolve "T" (isto) n deve acontecer
}

long long get_pot(int left, int k, int right) {
  long long p_left = chain[left].pot;
  long long p_k = chain[k].pot;
  long long p_right = chain[right].pot;
  
  int t_left = chain[left].type;
  int t_k = chain[k].type;
  int t_right = chain[right].type;

  return (p_left * affinity[t_left][t_k] * p_k) + (p_k * affinity[t_k][t_right] * p_right);
}

// devolver caminho usando recursao e a tabela de caminhos
void get_path(int i, int j, vector<int>& path) {
  if (i > j) return;
  int k = s[i][j];

  get_path(i, k - 1, path);
  get_path(k + 1, j, path);

  path.push_back(k);
}

bool is_better(int i, int j, int k1, int k2) {
  // escolher o melhor caminho (menor lexicograficamente ==> menor numero)
  vector<int> p1, p2;
  
  s[i][j] = k1;
  get_path(i, j, p1);
  
  s[i][j] = k2;
  get_path(i, j, p2);
  
  return p1 < p2;
}

void func() {
  int size = n + 2;
  // preparar a tabela de caminho e potencias
  m.assign(size, vector<long long>(size, 0));
  s.assign(size, vector<int>(size, 0));

  for (int L = 1; L <= n; L++) {
    for (int i = 1; i <= n - L + 1; i++) {
        int j = i + L - 1;
        // calcular a maxima potencia para cada caminho
        m[i][j] = -1; 

      for (int k = i; k <= j; k++) {
          // calcular a potencia
          long long pot = m[i][k-1] + m[k+1][j] + get_pot(i-1, k, j+1);

          // guardar a maior potencia e melhor caminho
          if (pot > m[i][j]) {
            m[i][j] = pot; // guardar a potencia
            s[i][j] = k; // guardar o caminho
          } 
          else if (pot == m[i][j]) {
          // no caso de ter varios caminhos possiveis escolher o lexicograficamente menor
          if (is_better(i, j, k, s[i][j])) {
            s[i][j] = k;
          }
        }
      }
    }
  }
}

// chegar ao caminho usando recursão e tabela de caminhos
void print_solution(int i, int j) {
  if (i > j) return;
  int k = s[i][j];
  print_solution(i, k - 1);
  print_solution(k + 1, j);
  cout << k << (k == s[1][n] && j == n ? "" : " ");
}

int main() {
  // Ler os inputs
  std::ios::sync_with_stdio(0);
  std::cin.tie(0);

  if (!(cin >> n)) return 0;

  // por a cadeia com inicio e fim "T"

  chain.resize(n + 2);

  chain[0] = {1, 4}; 

  for (int i = 1; i <= n; i++) {
      cin >> chain[i].pot;
  }

  chain[n + 1] = {1, 4}; 

  string classes;
  cin >> classes;
  for (int i = 0; i < n; i++) {
      chain[i+1].type = get_type_id(classes[i]);
  }

  func();

  cout << m[1][n] << endl;
  
  vector<int> final_path;
  get_path(1, n, final_path);
  
  for(size_t i = 0; i < final_path.size(); i++) {
      cout << final_path[i] << (i == final_path.size() - 1 ? "" : " ");
  }

  cout << endl;

  return 0;
}