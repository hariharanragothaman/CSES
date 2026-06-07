#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl "\n"

void prefix_sum(vector<int>& prefix_array, int& left, int& right)
{
    cout << prefix_array[right+1] - prefix_array[left] << endl;
}

int32_t main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

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
