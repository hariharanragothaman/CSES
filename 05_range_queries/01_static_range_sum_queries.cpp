#include "bits/stdc++.h"
using namespace std;
#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define endl "\n"
#define int long long

//#define LOCAL
#ifdef LOCAL
ifstream  i_data("../io/data.in");
ofstream  o_data("../io/data.out");
#define cin  i_data
#define cout o_data
#else
// Submit to Online Judge
#endif


void prefix_sum(vector<int>& prefix_array, int& left, int& right)
{
    cout << prefix_array[right+1] - prefix_array[left] << endl;
}

int32_t main()
{
    ENABLEFASTIO();
    int n, q;
    cin >> n >> q;
    vector<int> arr(n, 0);
    for(int i=0; i<n; i++) cin >> arr[i];

    vector<int> prefix_array(n+1, 0);
    for(int i=1; i<n+1; i++)
    {
        prefix_array[i] = prefix_array[i-1] + arr[i-1];
    }

    int left, right;
    while(q--)
    {
        cin >> left >> right;
        left = left-1;
        right = right -1;
        prefix_sum(prefix_array, left, right);
    }

    return 0;
}


