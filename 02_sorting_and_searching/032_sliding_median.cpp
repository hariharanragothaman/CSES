//
// Created by Hariharan Ragothaman on 11/14/21.
//

/**********  SLIDING WINDOW  ***********/

#include "bits/stdc++.h"
#include <ext/pb_ds/assoc_container.hpp> // Common file
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
#include <functional> // for less

#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define endl "\n"
#define int long long

#define LOCAL
#ifdef LOCAL
ifstream  i_data("../io/data.in");
ofstream  o_data("../io/data.out");
#define cin  i_data
#define cout o_data
#else
// Submit to Online Judge
#endif


/*
 *  Intiution explanation
 *  We want to compute something, here median,
 *  for every window of elements....
 */
typedef tree<int, null_type, less<int>, rb_tree_tag,tree_order_statistics_node_update> new_data_set;
int32_t main()
{
    ENABLEFASTIO();
    int n;
    int k;
    cin >> n >> k;

    vector<int> arr(n, 0);
//    multiset<int> ss;
    new_data_set ss;


    for(int i=0; i<n; i++)
        cin >> arr[i];

    vector<int> result;

    // Adding the first k numbers into the multiset
    for(int i=0; i<k; i++)
        ss.insert(arr[i]);

    int median = 0;
    for(int i=k; i<n; i++)
    {
        // calculating the median
        if(n&1)
        {
            median = *ss.find_by_order(k/2);
            result.emplace_back(median);
        }
        else
        {
            median = (*ss.find_by_order(k/2) + *ss.find_by_order(k/2-1)) >> 1;
            result.emplace_back(median >> 1);
        }
        ss.erase(ss.find(arr[i-k])); // erasing the first element
        ss.insert(arr[i]); // adding the new element into the set
    }

    for(auto c: result)
        cout << c << " ";
    cout << endl;
    return 0;
}


