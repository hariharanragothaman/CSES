/*
 *  Concept: Post Order Traversal
 */
#include "bits/stdc++.h"
using namespace std;

void solve( map<int, vector<int>>& graph, int n)
{

    // Starting Post order traversal
    deque<int> q;
    q.emplace_back(1);
    int node;
    vector<int> res_tmp;
    vector<int> postorder;

    while(q.size() > 0)
    {
        node = q.back();
        q.pop_back();
        res_tmp.push_back(node);
        if(graph[node].size() > 0)
        {
            for(auto c: graph[node])
                q.emplace_back(c);
        }
    }
    while(res_tmp.size() > 0)
    {
        postorder.emplace_back(res_tmp.back());
        res_tmp.pop_back();
    }
    /* End of post order traversal */

    vector<int> childrenCount(n+1);
    for(auto ele: postorder)
    {
        if(graph.find(ele) == graph.end())
        {
            childrenCount[ele] = 0;
        }
        else
        {
            int count = 0;
            count += graph[ele].size();
            for(auto children: graph[ele])
                count += childrenCount[children];
            childrenCount[ele] = count;
        }
    }

    for(int i=1; i<=n; i++)
        cout << childrenCount[i] << " ";
    cout << endl;
}


int main()
{
    int n;
    cin >> n;
    vector<int> arr(n+1);
    for (int i=2; i<arr.size(); i++)
        cin >> arr[i];

    map<int, vector<int>> graph;
    graph[1] = {};

    for(int j=2; j < arr.size(); j++)
        graph[arr[j]].emplace_back(j);

    solve(graph, n);

}