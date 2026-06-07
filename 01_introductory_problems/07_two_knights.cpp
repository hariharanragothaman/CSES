#include <bits/stdc++.h>
using namespace std;

#define lli long long int
#define li long int
#define ld long double

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    lli k;
    cin >> k;
    for (lli n = 1; n <= k; n++)
    {
        cout << n * n * (n * n - 1) / 2 - 4 * (n - 1) * (n - 2) << endl;
    }
    return 0;
}
