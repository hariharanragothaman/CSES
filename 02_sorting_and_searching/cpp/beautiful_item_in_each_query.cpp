//
// Created by Hariharan Ragothaman on 11/13/21.
//
// Reference: https://leetcode.com/problems/most-beautiful-item-for-each-query/
#include "bits/stdc++.h"
using namespace std;

vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries)
{
    vector<int> ans = {};
    map<int, int> hmap;

    // It's amazing that unordered_map gets initialized
    for(auto c: items)
    {
        hmap[c[0]] =  max(c[1], hmap[c[0]]);
    }

    int mx = 0;
    for(auto& c: hmap)
    {
        if(c.second > mx)
            mx = c.second;
        else if(c.second <=mx)
            c.second = mx;
    }
    cout << "The hashmap is:" << endl;
    for(auto c: hmap)
        cout << c.first << " " << c.second << endl;

    cout << "Printing the keys.." << endl;
    vector<int> keys = {};
    for(auto c: hmap)
        keys.push_back(c.first);

    for(auto c: keys)
        cout << c << " ";
    cout << endl;

    for(auto q: queries)
    {
        // This part is wasting time - since we know that 6 is the largest element.
        // so we binary search and find where to insert 10 - so that we get till that?
        cout << "The query is: " << q << endl;
        int idx = upper_bound(keys.begin(), keys.end(), q) - keys.begin();
        cout << "The index is:" << idx << endl;
        if(idx == 0)
            ans.emplace_back(0);
        else
            ans.emplace_back(hmap[keys[idx-1]]);
    }

    return ans;
}

int main()
{
    vector<vector<int>> nums = {{193,732},{781,962},{864,954},{749,627},{136,746},{478,548},{640,908},{210,799},{567,715},
                        {914,388},{487,853},{533,554},{247,919},{958,150},{193,523},{176,656}, {395,469},{763,821},{542,946},{701,676}};
    vector<int> queries = {885,1445,1580,1309,205,1788,1214,1404,572,1170,989,265,153,151,1479,1180,875,276,1584};
    vector<int> res = maximumBeauty(nums, queries);
}