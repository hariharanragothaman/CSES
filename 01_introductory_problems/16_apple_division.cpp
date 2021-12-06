//
// Created by Hariharan Ragothaman on 11/12/21.
//

/*
 *  Trick reference: https://stackoverflow.com/questions/41028859/looping-over-a-bitmask
 *
 */
#include "bits/stdc++.h"
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    cin >> n;
    vector<long long int> arr(n, 0);

    long long int total = 0;
    for(int i=0; i<n; i++)
    {
        cin >> arr[i];
        total += arr[i];
    }

    long long int ans = INT_MAX;
    long long int current = 0;
    // Going through all combinations
    for(long long int msk=0; msk < (1<<n); msk++)
    {
        long long int s = 0;
        // Going through the length of the combination generated
        for(long long int j=0; j<n; j++) {
            // The if basically checks - position that have '1'
            // in the current combination
            if (msk & (1 << j)) {
                s += arr[j];
            }
            current = abs((total - s)-s);
            ans = min(ans, current);
        }
    }

    cout  << ans << endl;
    return 0;
}