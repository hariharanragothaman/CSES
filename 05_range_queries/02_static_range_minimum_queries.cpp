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

/*
 * There are datastructures that support static, but we will just go with segment tree
 * It's easy to understand, and at a later point we can implement the other datastrcutres
 */

class SegmentTree
{
private:
    vector<int> segment_tree;
    int n;
public:
    void build_tree(vector<int>& arr)
    {
        n = arr.size();
        segment_tree.resize(2*n);
        for(int i=0; i<n; i++)
            segment_tree[i+n] = arr[i];

        for(int i=n-1; i>0; i--)
            // The operation here should be replaced by the function of intent
            segment_tree[i] = min(segment_tree[i*2], segment_tree[i*2+1]);

    }

    void update(int position, int value)
    {
        position += n;
        segment_tree[position] = value;
        while(position > 1)
        {
            position = position >> 1;
            // The operation here should be replaced by the function of intent
            segment_tree[position] = min(segment_tree[position*2], segment_tree[position*2+1]);
        }
    }

    int query(int left, int right)
    {
        left = left + n;
        right = right + n;
        int result = 0;

        while(left <= right)
        {
            if(left % 2 == 1)
            {
                if(result == 0)
                    result = segment_tree[left];
                else
                    // The operation here should be replaced by the function of intent
                    result = min(result, segment_tree[left]);
            }
            if(right % 2 == 0)
            {
                if(result == 0)
                    result = segment_tree[right];
                else
                    // The operation here should be replaced by the function of intent
                    result = min(result, segment_tree[right]);

            }
            left = (left + 1) >> 1;
            right = (right - 1) >> 1;
        }
        return result;
    }

};

int32_t main()
{
    ENABLEFASTIO();
    int n, q;
    cin >> n >> q;
    vector<int> arr(n, 0);
    for(int i=0; i<n; i++) cin >> arr[i];

    SegmentTree seg_obj;
    seg_obj.build_tree(arr);

    int left, right;
    while(q--)
    {
        cin >> left >> right;
        left = left-1;
        right = right -1;
        int res = seg_obj.query(left, right);
        cout << res << endl;
    }

    return 0;
}


