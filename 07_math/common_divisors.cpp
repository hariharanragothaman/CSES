/**
 * File              : common_divisors.cpp
 * Author            : cppygod
 * Date              : 23.01.2022
 * Last Modified Date: 30.04.2022
 * Last Modified By  : cppygod
 */
#include<bits/stdc++.h>
using namespace std;
#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)


// This whole solution just goes to prove, that function calls are not free
// Also another learning point here is that - we need to initialize stuff to zero. Always remember that!

set<int> find_all_divisors(int& n)
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
    return factors;
}

int main()
{
    ENABLEFASTIO();
    int n;
    cin >> n;

    vector<int> arr(n);
    for(int i=0; i<n; i++) cin >> arr[i];

    set<int> result;
    vector<int> cnt(1000001, 0);

    /*
     *  The initial logic we had was - find all the factors for each number
     *  Put them into a total set
     *  When you find a number that is already in the 'set' then recompute the max answer.
     *      this almost becomes n^3.
     *
     *  Alternatively we can traverse from reverse & do something - Intuition
     *  So - we can maintain a count.
     */

    for(auto c: arr)
    {
        result = find_all_divisors(c);
        for(auto f: result)
        {
            cnt[f]++;
        }
    }

    for(int i=1000000; i>=1; i--)
    {
        if (cnt[i] >= 2)
        {
            cout << i << endl;
            break;
        }
    }
    return 0;
}
