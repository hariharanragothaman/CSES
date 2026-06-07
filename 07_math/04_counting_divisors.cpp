/**
 * File              : counting_divisors.cpp
 * Author            : cppygod
 * Date              : 30.04.2022
 * Last Modified Date: 30.04.2022
 * Last Modified By  : cppygod
 */
#include<bits/stdc++.h>
using namespace std;

#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)


const int maxn = 2e5+10;
bool have_gondola_yet[maxn];

int find_all_divisors(int n)
{
    set<int> factors;
    int s = sqrt(n);
    for(int i = 1;i <= s;i++)
    {
        if (n%i==0)
        {
            if (n/i == i) // check if divisors are equal
                factors.insert(i);
            else
            {
                factors.insert(i);
                factors.insert(n/i);
            }
        }
    }
    factors.insert(n);
    return factors.size();
}

int main(){
    ENABLEFASTIO();
    int T;
    cin >> T;
    int x;
    int result;

    while(T--)
    {
        cin >> x;
        result = find_all_divisors(x);
        cout << result << endl;
    }
    return 0;
}
