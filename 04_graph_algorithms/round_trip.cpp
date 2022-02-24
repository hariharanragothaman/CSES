#include <bits/stdc++.h>
using namespace std;

/* 
To find the eulerian path
A graph has eulerian path only if:
a. For each node indegree and outdegree is the same  (OR)
b. For each node, indegree and outdegree is the same, except exactly 2 nodes.
    out[x] = in[x] + 1 (or) out[y] = in[y] - 1
    
For condition a. when both indegree and outdegree is the same, all eulerian paths are also eulerian circuits - 
where in starting index and ending index is the same...

A node with out[i] == in[i] + 1 must be the starting point of an eulerian path if there exists one...
*/

/*

An undirected graph has Eulerian cycle if following two conditions are true. 
….a) All vertices with non-zero degree are connected. 
	We don’t care about vertices with zero degree because they don’t belong to Eulerian Cycle or Path (we only consider all edges). 
….b) All vertices have even degree.

An undirected graph has Eulerian Path if following two conditions are true. 
….a) Same as condition (a) for Eulerian Cycle 
….b) If zero or two vertices have odd degree and all other vertices have even degree. 
Note that only one vertex with odd degree is not possible in an undirected graph (sum of all degrees is always even in an undirected graph)


*/

bool check_for_euler_circuit()
{

}

bool check_for_euler_path()
{

}

int32_t main()
{
	unordered_map<int, int>
	int cities, roads;
	cin >> cities >> roads;
	int i = 0;
	int a, b;
	while(i < roads)
	{
		cin >> a >> b;
		i++;
	}
	return 0;
}
