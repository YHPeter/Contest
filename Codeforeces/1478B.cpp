#include <bits/stdc++.h>
#define forn(i, n) for (int i = 0; i < int(n); i++)

using namespace std;

int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	forn(_, t){
		int q,d;
        cin>>q>>d;
        long long li[q];
        for(long long i = 0; i < q; i++) cin>>li[i];

        for(auto x: li){
            while(true){
                if(x<10 && x!=d){
                    printf("NO\n");
                    break;
                }
                x-=d;
                if(x%10==0 || x%d==0){
                    printf("YES\n");
                    break;
                }
            }
        }
        
	}
	return 0;
}

