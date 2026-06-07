#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl "\n"
#define all(x) x.begin(), x.end()

#if __cplusplus >= 201103L
#endif

#if __cplusplus >= 201103L
#endif

/**********************************************************************************************************************/

/**********************************************************************************************************************/

#define s second

/**********************************************************************************************************************/

#define  mset(a,x)      memset(a,x,sizeof(a))
#define  debv(a)        for(auto it: a)cout<<it<<" ";newl;
#define  deb1(a)        cout<<a<<"\n";
#define  deb2(a,b)      cout<<a<<" "<<b<<"\n";
#define  deb3(a,b,c)    cout<<a<<" "<<b<<" "<<c<<"\n";
#define  deb4(a,b,c,d)  cout<<a<<" "<<b<<" "<<c<<" "<<d<<"\n";

/**********************************************************************************************************************/

// Sub-routine comforts

#define  uniq(a)  a.resize(unique(a.begin(), a.end()) - a.begin());
#define present(container, element) (container.find(element) != container.end())
#define cpresent(container, element) (find(all(container), element) != container.end())
   
/**********************************************************************************************************************/

// Templates

template < typename T1, typename T2 > struct pair {
    T1 first;
    T2 second;
};

/*********************************************FREQUENTLY USED SUBROUTINES *********************************************/

vector<int> sieve(int n)
{
    int*arr = new int[n + 1]();
    vector<int> vect;
    for (int i = 2; i <= n; i++)
        if (arr[i] == 0)
        {
            vect.push_back(i);
            for (int j = 2 * i; j <= n; j += i)arr[j] = 1;
        }
    return vect;
}

long long gcd(long long a, long long b) 
{
    if (b > a) 
    {
        return gcd(b, a);
    }
    if (b == 0) 
    {
        return a;
    }
    return gcd(b, a % b);
}

long long expo(long long a, long long b, long long mod) 
{
    long long res = 1;
    while (b > 0) 
    {
        if (b & 1)res = (res * a) % mod;
        a = (a * a) % mod;
        b = b >> 1;
    }
    return res;
}

void extendgcd(long long a, long long b, long long*v) 
{
    if (b == 0) {
        v[0] = 1;    //pass an arry of size 3
        v[1] = 0;
        v[2] = a;
        return ;
    }
    extendgcd(b, a % b, v);
    long long x = v[1];
    v[1] = v[0] - v[1] * (a / b);
    v[0] = x;
    return;
}

bool revsort(long long a, long long b) 
{
    return a > b;
}

void swap(int &x, int &y) 
{
    int temp = x;
    x = y;
    y = temp;
}

bool sortBySecond(const std::pair<int,int> &a, const std::pair<int,int> &b)
{
    return (a.second < b.second);
}

template<typename T>
std::vector<T> slices(std::vector<T> const &v, int m, int n)
{
    auto first = v.cbegin() + m;
    auto last = v.cbegin() + n + 1;
    std::vector<T> vec(first, last);
    return vec;
}

/********************************************END OF CUSTOMIZATIONS*****************************************************/

void solve()
{
	int x, n; 
	cin >> x >> n; ;
	int p; 
        set<int> S; 	
	S.insert(0);
	S.insert(x);

	multiset<int> R; 
	R.insert(0);
	R.insert(x);

	for(int i=0; i<n; i++)
	{
		cin >> p;
		auto pos = S.upper_bound(p);
		auto pos2 = pos; 
		pos2--;

		auto left = p - *pos2;
		auto right = *pos - p;
		int total = left + right;

		R.erase(R.find(total));
		R.insert(left);
		R.insert(right);
		S.insert(p);

		auto ans = R.end();
		--ans;
		cout << *ans << " ";
	}
}

int32_t main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}
