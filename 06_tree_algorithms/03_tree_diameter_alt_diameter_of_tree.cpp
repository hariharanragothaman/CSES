/**
 * File              : diameter_of_tree.cpp
 * Author            : cppygod
 * Date              : 12.02.2022
 * Last Modified Date: 12.02.2022
 * Last Modified By  : cppygod
 */
#include "bits/stdc++.h"
using namespace std;

void getDiameter(map<int, vector<int>>&g, int& nodes)
{
    cout << "Entering function to get diameter of node" << endl;
    /* We need to do DFS twice */

    deque<pair<int, int>> q;
    q.emplace_back(make_pair(1, 0));
    set<int> visited;
    int current_max_length = 0;
    pair<int, int> node_and_length;
    int arbitrary_node = 1;


    /* First time DFS to find the arbitrary node  */
    while(q.size() > 0)
    {
        node_and_length = q.back();
        q.pop_back();

        visited.insert(node_and_length.first);
        if(node_and_length.second > current_max_length)
        {
            current_max_length = node_and_length.second;
            arbitrary_node = node_and_length.first;
        }

        for(auto child: g[node_and_length.first])
        {
            if (visited.find(child) == visited.end())
            {
                cout << "The node is " << node_and_length.first << endl;
                q.emplace_back(make_pair(child, node_and_length.second + 1));
            }
            cout << child << endl;
        }
        cout << "The arbitrary node is:" << arbitrary_node << endl;
    }

}

int main()
{
    int nodes;
    cin >> nodes;
    int edges = nodes - 1;
    int u, v;
    map<int, vector<int>> g;
    while(edges)
    {
        cin >> u >> v;
        g[u].emplace_back(v);
        edges--;
    }
     getDiameter(g, nodes);
}
