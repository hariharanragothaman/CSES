/* BEGIN HEADER FILES AND OTHER OPTIZATIONS */
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC optimize("inline")
#include <iostream>
#include <fstream>
#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <chrono>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

// For Hash
#include <functional>

// For all useful constants
#include <climits>

// Data-Structures and related stuff.
#include <map>
#include <set>
#include <stack>
#include <random>
#include <deque>
#include <queue>   // Includes Priority Queue
#include <vector>
#include <unordered_map>
#include <unordered_set>


// Some basic typedef's for comfort
typedef vector<int> vi;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

// #defines for bounds comfort
#define double long double

// #defines for comfort
#define f first
#define mp make_pair
#define pb push_back
#define eb emplace_back

// Binary Search comforts
#define lb lower_bound
#define ub upper_bound


// begin deepsigh
//#define min(x,y) ({ __typeof__(x) __var0 = x; __typeof__(y) __var1 = y; __var0 < __var1 ? __var0 : __var1; })
//#define max(x,y) ({ __typeof__(x) __var0 = x; __typeof__(y) __var1 = y; __var0 < __var1 ? __var1 : __var0; })
//static const int ENABLEFASTIO = []() { std::ios::sync_with_stdio(false); std::cin.tie(nullptr); std::cout.tie(nullptr); return 0; }();
// end deepsigh

// BEGIN NO SAD
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
// END NO SAD

/* END HEADER FILES AND OTHER OPTIZATIONS */

/*
Some General Advice

REMEMBER CLEAR GLOBAL STATE
REMEMBER READ THE PROBLEM STATEMENT AND DON'T SOLVE A DIFFERENT PROBLEM
remember hidden T factor of 1e2
read the bounds for stupid cases
did you restart your editor
pushing back vectors is garbage, pre-initialize them
function calls are not free
*/

int main()
{
    int  n;
    cin >> n;
    vi A(n);
    for(int i=0; i<n; i++)
        cin >> A[i];
    map<int, int> hmap;

    for(int i=0; i<n; i++)
    {
        hmap[A[i]] += 1;
    }

    cout << hmap.size();
    return 0;

}