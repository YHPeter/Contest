#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < int(n); i++)

using namespace std;

int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	forn(_, t){
		int n, m;
		string s;
		cin >> n >> m;
		cin >> s;
		vector<int> sul(1, 0), sur(1, 0);
		for (int i = n - 1; i >= 0; --i){
			int d = s[i] == '+' ? 1 : -1;
			sul.push_back(min(0, sul.back() + d));
			sur.push_back(max(0, sur.back() + d));
		}
		reverse(sul.begin(), sul.end());
		reverse(sur.begin(), sur.end());
		vector<int> prl(1, 0), prr(1, 0), pr(1, 0);
		forn(i, n){
			int d = s[i] == '+' ? 1 : -1;
			pr.push_back(pr.back() + d);
			prl.push_back(min(prl.back(), pr.back()));
			prr.push_back(max(prr.back(), pr.back()));
		}
        for(auto i: sul) cout<<i<<" "; cout<<endl;
        for(auto i: sur) cout<<i<<" "; cout<<endl;
        for(auto i: prl) cout<<i<<" "; cout<<endl;
        for(auto i: prr) cout<<i<<" "; cout<<endl;
        for(auto i: pr) cout<<i<<" "; cout<<endl;
/*
0 -1 0 0 0
2 1 2 1 0
0 0 0 0 0
0 1 1 1 2
0 1 0 1 2

[0, 0, 0, -1, 0] 
[0, 1, 2, 1, 2] 
[0, 0, 0, 0, 0] 
[0, 1, 1, 1, 2] 
[0, 1, 0, 1, 2]
*/

        forn(i, m){
            int l, r;
            cin >> l >> r;
            --l;
            int l1 = prl[l], r1 = prr[l];
            int l2 = sul[r] + pr[l], r2 = sur[r] + pr[l];
            printf("%d\n", max(r1, r2) - min(l1, l2) + 1);
        }
        
	}
	return 0;
}

/*
1
4 10
+-++

2
4 10
+-++
1 1
1 2
2 2
1 3
2 3
3 3
1 4
2 4
3 4
4 4
8 4
-+--+--+
1 8
2 8
2 5
1 1


1
2
4
4

3
3
4
2
3
2
1
2
2
2

*/