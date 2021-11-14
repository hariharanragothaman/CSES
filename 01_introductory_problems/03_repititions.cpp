#include "bits/stdc++.h"
using namespace std;
#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)

#define LOCAL
#ifdef LOCAL
ifstream  i_data("../io/data.in");
ofstream  o_data("../io/data.out");
#define cin  i_data
#define cout o_data
#else
// Submit to Online Judge
#endif

int main()
{
    ENABLEFASTIO();

    string s;
    cin >> s;
    int n = s.size();
    int repeats = 0;
    int ans = 0;
    for(int i=1; i<n; i++)
    {
        if(s[i] == s[i-1])
        {
            repeats++;
        }
        else
        {
            ans = max(ans, repeats);
            repeats = 0;
        }
        ans = max(ans, repeats);
    }
    cout << ans+1 << endl;

    return 0;
}