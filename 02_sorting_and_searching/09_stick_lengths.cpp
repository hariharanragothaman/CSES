#include <bits/stdc++.h>
using namespace std;

// GODSPEED

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> arr(n);
    for(int i=0; i<n; i++) cin>> arr[i];
    sort(arr.begin(), arr.end());

    int median = n%2 ? arr[n/2] : (arr[n/2] + arr[n/2-1]) / 2;

    long long result = 0;
    for(int i=0; i<n; i++)
    {
        result += abs(median-arr[i]);
    }
    cout << result;
    return 0;
}
