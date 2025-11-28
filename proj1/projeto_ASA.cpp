// g++ -std=c++11 -O3 -Wall project_test.cpp -lm -o project_test
#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <string>
#include <unordered_map>
using namespace std;

int n;

struct node {
  int _potential;
  int _class;
};

// a lista é ma idea
struct pacote {
  int _pos;
  int _energy_l, _energy_r;
  list<int> path;
};

// struct pacote {
//   int _pos;
//   int _energy_l, _energy_r;
//   vector<int> last; // [i, j, index] para encontrar o ultimo, e dps no fim reconstruo
// };

vector<node> chain;
string class_str;

vector<vector<list<pacote>>> sol;

vector<int> afinity = {
1 ,3, 1, 3,
5, 1, 0, 1,
0, 1, 0, 4,
1, 3, 2, 3,
};

void get_variables(){
  cin >> n;

  chain.resize(n);

  for (int i = 0; i< n; i++){
    cin >> chain[i]._potential;
  }
  
  cin >> class_str;

  for (int i = 0; i < n; i++){
    switch (class_str[i])
    {
    case 'P':
      chain[i]._class = 0;
      break;
    case 'N':
      chain[i]._class = 1;
      break;
    case 'A':
      chain[i]._class = 2;
      break;
    case 'B':
      chain[i]._class = 3;
      break;
    default:
      // n sei como dar handle
      break;
    }
  }
}

int get_afinity(int a, int b){
  return afinity[a*4 + b];
}

void print_pacotes(pacote p){
  cout << 
  "\tENERGY_L:" << p._energy_l << " " << 
  "ENERGY_R:" << p._energy_r << " " <<
  "NODE:" << chain[p._pos]._potential << " " << chain[p._pos]._class << " "
  "PATH:";
  for (auto x: p.path){
    cout << x << " ";
  }
  cout << "\n";
}

int main() {
  std::ios::sync_with_stdio(0);
  std::cin.tie(0);

  get_variables();

  sol.resize(n, vector<list<pacote>>(n));

  int energy = 0;

  list<int> path;
  
  for (int i = 0; i < n; i++){
    cout << "i:" << i << "\n";
    for (int j = 0; j < n - i; j++){
      cout << "j:" << j << "\n";
      if (i == 0){
        sol[j][j].push_back(pacote{j,0,0,{}});
        continue;
      }
            
      energy = 0;
      
      for (int k = 1; k < i + 1; k++){                
        list<pacote> list1 = sol[j][j + i - k];
        list<pacote> list2 = sol[j + i - k + 1][j + i];

        cout << "list1:" << "\n";

        for(auto p: list1){
          print_pacotes(p);
        }

        cout << "list2:" << "\n";

        for(auto p: list2){
          print_pacotes(p);
        }

        cout << "result:" << "\n";
        
        for(pacote p1: list1){
          for (pacote p2: list2){

            list<int> path_aux, path1, path2;
            path_aux.insert(path_aux.end(), p1.path.begin(), p1.path.end());
            path_aux.insert(path_aux.end(), p2.path.begin(), p2.path.end());
            
            path1 = path_aux;
            path1.push_back(p1._pos);
            path2 = path_aux;
            path2.push_back(p2._pos);
            
            pacote left{
              p2._pos,
              p1._energy_l + chain[p1._pos]._potential, 
              p1._energy_r + chain[p1._pos]._potential * chain[p2._pos]._potential * 
              get_afinity(chain[p1._pos]._class, chain[p2._pos]._class),
              path1
            };

            pacote right{
              p1._pos,
              p2._energy_l + chain[p1._pos]._potential * chain[p2._pos]._potential * 
              get_afinity(chain[p1._pos]._class, chain[p2._pos]._class),
              p2._energy_r + chain[p2._pos]._potential,
              path2
            };
            
            sol[j][i+j].push_back(right);
            sol[j][i+j].push_back(left);
            
            print_pacotes(left);
            print_pacotes(right);
            
            if (i == n - 1){
              int new_energy_r = right._energy_l + right._energy_r + chain[right._pos]._potential * 2;
              int new_energy_l = left._energy_l + left._energy_r + chain[left._pos]._potential * 2;
              int maxed = max(new_energy_l, new_energy_r);

              if (maxed > energy){
                energy = maxed;
                if (new_energy_l > new_energy_r){
                  path = path1;
                  path.push_back(p2._pos);
                } else {
                  path = path2;
                  path.push_back(p1._pos);
                }
              }
            }
          }
        }
      }
    }
  }
  cout << energy << "\n";
  for (auto x: path){
    cout << x + 1 << " ";
  }
  return 0;
}