#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl "\n"

/*
 *  For each product you need to make
 *  ans / k[i] jumps to make a product
 *  So we can binary search for the ans across the entire sample space.
 */

bool check(int pivot, vector<int> arr, int n, int k)
{
    int cnt = 0;
    int so_far = 0;

    for(int i=0; i<n; i++)
    {
        if(arr[i] > pivot)
            return false;
        // This is the one that's actually doing the splitting
        if(so_far + arr[i] > pivot)
        {
            so_far = 0; // so_far how many splits we are.. caluclation
            cnt++;
        }
        so_far += arr[i];
    }
    if(so_far)
        cnt++;
    return cnt <= k;
}

int32_t main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    int k;
    cin >> n >> k;

    vector<int> arr(n, 0);
    for(int i=0; i<n; i++) cin >> arr[i];

    int low = 0;
    int high = 1e18;
    int ans = high;
    while(low <= high)
    {
        int pivot = (low + high) >> 1;
        if(check(pivot, arr, n, k))
        {
            ans = pivot;
            high = pivot-1;
        }
        else
        {
            low = pivot+1;
        }
    }

    cout << ans << endl;

    return 0;
}
