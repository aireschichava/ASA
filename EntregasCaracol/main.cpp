#include <algorithm>
#include <iostream>
#include <limits>
#include <queue>
#include <vector>

using namespace std;

int main() {
  // Fast I/O
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int N, M, m1, m2, K;
  // Parse input until EOF. N is the number of intersections.
  while (cin >> N) {
    // Read total trucks (M), range of trucks to report (m1, m2), and number of
    // roads (K)
    cin >> M >> m1 >> m2 >> K;

    vector<vector<int>> adj(N + 1);
    vector<int> in_degree(N + 1, 0);

    // Build the graph using adjacency list.
    // Also compute in-degrees for topological sort.
    for (int i = 0; i < K; ++i) {
      int u, v;
      cin >> u >> v;
      adj[u].push_back(v);
      in_degree[v]++;
    }

    // 1. Topological Sort (Kahn's Algorithm)
    // A topological sort is required to process nodes in a valid dependency
    // order (DAG).
    vector<int> topo_order;
    topo_order.reserve(N);
    queue<int> q;
    for (int i = 1; i <= N; ++i) {
      if (in_degree[i] == 0) {
        q.push(i);
      }
    }

    while (!q.empty()) {
      int u = q.front();
      q.pop();
      topo_order.push_back(u);

      for (int v : adj[u]) {
        in_degree[v]--;
        if (in_degree[v] == 0) {
          q.push(v);
        }
      }
    }

    // Verify that the graph is a DAG (Directed Acyclic Graph)
    if (static_cast<int>(topo_order.size()) != N) {
      cerr << "Cycle detected in input graph.\n";
      return 0;
    }

    // Map each node to its position in the topological order for quick lookups.
    vector<int> topo_pos(N + 1, 0);
    for (int i = 0; i < N; ++i) {
      topo_pos[topo_order[i]] = i;
    }

    // 2. Count Paths with Batch Optimization
    // We process start nodes in blocks to improve cache locality.
    // Instead of doing 1 pass per start node, we do 1 pass per BATCH of start
    // nodes.

    // Using vector for path counts of the batch: [N + 1][batch_size] serialized
    const int BATCH_SIZE = 128;
    vector<int> batch_counts;
    batch_counts.resize((N + 1) * BATCH_SIZE);

    vector<char> batch_reachable;
    batch_reachable.resize((N + 1) * BATCH_SIZE);

    // Optimization: Lazy reset using token
    vector<int> visit_token(N + 1, 0);
    int current_token = 0;

    vector<vector<pair<int, int>>> truck_routes(max(0, m2 - m1 + 1));

    for (int start_base = 1; start_base <= N; start_base += BATCH_SIZE) {
      int batch_end = min(N, start_base + BATCH_SIZE - 1);
      int current_batch_size = batch_end - start_base + 1;

      if (++current_token == numeric_limits<int>::max()) {
        fill(visit_token.begin(), visit_token.end(), 0);
        current_token = 1;
      }

      // Initialize start nodes
      // We do NOT clear the whole array. We clear only when we first touch a
      // node.
      for (int i = 0; i < current_batch_size; ++i) {
        int start_node = start_base + i;

        // Mark start node as visited/touched
        visit_token[start_node] = current_token;

        // Initialize slice
        int idx = start_node * BATCH_SIZE;

        fill(batch_counts.begin() + idx,
             batch_counts.begin() + idx + current_batch_size, 0);
        fill(batch_reachable.begin() + idx,
             batch_reachable.begin() + idx + current_batch_size, 0);

        batch_counts[idx + i] = 1 % M;
        batch_reachable[idx + i] = 1;
      }

      // Determine the earliest topological position among the start nodes in
      // this batch. We only need to start processing from this point in the
      // topological order.
      int min_topo_idx = N;
      for (int i = 0; i < current_batch_size; ++i) {
        min_topo_idx = min(min_topo_idx, topo_pos[start_base + i]);
      }

      // Process nodes in topological order to propagate path counts
      for (int idx = min_topo_idx; idx < N; ++idx) {
        int u = topo_order[idx];

        if (visit_token[u] != current_token)
          continue;

        int base_idx = u * BATCH_SIZE;

        // If this node is reachable, calculate the truck ID and record the
        // route when the destination differs from the start node and the
        // truck falls inside the requested range.
        for (int k = 0; k < current_batch_size; ++k) {
          int s_node = start_base + k;
          if (s_node != u && batch_reachable[base_idx + k]) {
            int truck_id = 1 + batch_counts[base_idx + k];
            if (truck_id >= m1 && truck_id <= m2) {
              truck_routes[truck_id - m1].push_back({s_node, u});
            }
          }
        }

        // Propagate path counts to neighbors
        for (int v : adj[u]) {
          int v_base = v * BATCH_SIZE;

          // If v not visited in this batch, initialize it
          if (visit_token[v] != current_token) {
            visit_token[v] = current_token;
            fill(batch_counts.begin() + v_base,
                 batch_counts.begin() + v_base + current_batch_size, 0);
            fill(batch_reachable.begin() + v_base,
                 batch_reachable.begin() + v_base + current_batch_size, 0);
          }

          // Propagate reachability and path counts from node 'u' to its
          // neighbor 'v' for each start node 's_node' within the current batch.
          // If 'u' is reachable from 's_node', then 'v' also becomes reachable
          // from 's_node' (batch_reachable[v_base + k] = 1). The number of
          // paths from 's_node' to 'v' is incremented by the number of paths
          // from 's_node' to 'u' (batch_counts[v_base + k] +=
          // batch_counts[base_idx + k]), ensuring the result wraps around M
          // (modulo M).
          for (int k = 0; k < current_batch_size; ++k) {
            if (batch_reachable[base_idx + k]) {
              batch_reachable[v_base + k] = 1;
              int val = batch_counts[v_base + k] + batch_counts[base_idx + k];
              if (val >= M)
                val -= M;
              batch_counts[v_base + k] = val;
            }
          }
        }
      }
    }
    // Print the routes for each truck within the requested range [m1, m2].

    for (int t = m1; t <= m2; ++t) {
      cout << "C" << t;

      if (!truck_routes.empty()) {
        vector<pair<int, int>> &routes = truck_routes[t - m1];
        if (!routes.empty()) {
          sort(routes.begin(), routes.end());
          for (const auto &p : routes) {
            // Some judges are strict about whitespace; emit "A,B".
            cout << " " << p.first << "," << p.second;
          }
        }
      }
      cout << "\n";
    }
  }

  return 0;
}
