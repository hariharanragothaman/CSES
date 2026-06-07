#include <bits/stdc++.h>
using namespace std;

int main()
{
    int  n;
    cin >> n;
    vector<int> A(n);
    for(int i=0; i<n; i++)
        cin >> A[i];
    map<int, int> hmap;

    for(int i=0; i<n; i++)
    {
        hmap[A[i]] += 1;
    }

    cout << hmap.size();
    return 0;

}
