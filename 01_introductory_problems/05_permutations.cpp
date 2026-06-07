#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    if(n==1)
        cout << 1 << endl;
    else if(n==4)
    {
        vector<int> res = {2, 4, 1, 3};
        for(auto c: res) cout << c << " ";
        cout << endl;
    }
    else if(n < 5)
    {
        cout << "NO SOLUTION" << endl;
    }
    else
    {
        vector<int> odd, even;
        for(int i=n; i>0; i--)
        {
            if(i&1)
                odd.push_back(i);
            else
                even.push_back(i);
        }
        for(auto c: odd)
            cout << c << " ";
        for(auto c: even)
            cout << c << " ";
        cout << endl;
    }
    return 0;
}
