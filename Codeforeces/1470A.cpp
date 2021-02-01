#include<bits/stdc++.h>
#include<algorithm>
using namespace std;
typedef long long ll;

bool complare(int a,int b){
    return a>b;
}
ll solve(){
    ll ans=0,n,m,bought=0;
    cin>>n>>m;
    int c[m+1],k[n];
    for (int i=0;i<n;++i) cin>>k[i];
    for (int i=1;i<=m;++i) cin>>c[i];
    sort(k, k+n, complare);
    for (int i=0;i<n;++i){
        if (k[i]>bought) {
            ans+=c[++bought];
        }
        else{
            ans+=c[k[i]];
        }
    }
    return ans;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin>>t;    
    for (int i=0; i<t; i++) printf("%lld\n",solve());
    return 0;
}
/*
2
5 4
2 3 4 3 2
3 5 12 20
5 5
5 4 3 2 1
10 40 90 160 250

30
190

1
1 10
5
2 3 9 30 566 1337 31337 70775 111111 413413
*/