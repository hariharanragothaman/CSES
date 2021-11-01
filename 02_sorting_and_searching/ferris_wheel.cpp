//
// Created by Hariharan Ragothaman on 10/31/21.
//
#include<bits/stdc++.h>
using namespace std;

#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC optimize("inline")
#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)


const int maxn = 2e5+10;
bool have_gondola_yet[maxn];

void solve()
{
    int children, maximumWeight;
    cin >> children >> maximumWeight;
    vector<int> arr(children);
    for(int i=0; i < children; i++) cin >> arr[i];

    sort(arr.begin(), arr.end());

    int count = 0;
    int left = 0;
    int right = children - 1;

    while (left < right)
    {
        if(arr[left] + arr[right] <= maximumWeight)
        {
            count++;
            have_gondola_yet[left] = have_gondola_yet[right] = true;
            right--;
            left++;
        }
        else
        {
            right--;
        }
    }

    for(int i=0; i < children; i++)
    {
        count += have_gondola_yet[i] == false;
    }

    cout << count << endl;
}

int main(){
    ENABLEFASTIO();
    solve();
    return 0;
}
