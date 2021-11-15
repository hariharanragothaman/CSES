//
// Created by Hariharan Ragothaman on 11/14/21.
//

#include "bits/stdc++.h"
using namespace std;
#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define endl "\n"
#define int long long

//#define LOCAL
#ifdef LOCAL
ifstream  i_data("../io/data.in");
ofstream  o_data("../io/data.out");
#define cin  i_data
#define cout o_data
#else
// Submit to Online Judge
#endif


int32_t main()
{
    ENABLEFASTIO();
    int n;
    cin >> n;
    vector<int> arr(n, 0);
    for(int i=0; i<n; i++) cin >> arr[i];

    // To find the longest sequence of successive songs where each song is unique
    // Classic sliding window implementation

    int left = 0;
    int right = 0;
    set <int> s;
    int max_length = 0;

    while(right < n)
    {
        // Expand the window...
//        if(find(s.begin(), s.end(), arr[right]) == s.end())
        if(!s.count(arr[right]))
        {
            s.insert(arr[right]);
            max_length = max(max_length, right-left+1);
        }
        // Contract the window - if it's alread there in the set
        else
        {
            for(int i=left; i<right; i++)
            {
                if(arr[i] == arr[right])
                    left = i+1;
            }
            max_length = max(max_length, right-left+1);
        }

        right += 1;
    }
    cout << max_length;
    return 0;
}
