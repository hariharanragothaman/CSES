#include <bits/stdc++.h>
using namespace std;

int hamming(int a, int b)
{
    return __builtin_popcount(a ^ b);
}

int main()
{
    int n, k;
    cin >> n >> k;
    string s;

    vector<int> A(n, 0);
    for(int i=0; i<n; i++)
    {
        cin >> s;
        reverse(s.begin(), s.end());
        for(int j=0; j<k; j++)
            A[i] += (s[j] == '1') * (1 << j);
    }

    int ans = 32;
    for(int i=0; i<n; i++)
        for (int j=i+1; j<n; j++)
            ans = min(ans, hamming(A[i], A[j]));

    cout << ans << endl;
    return 0;
}
