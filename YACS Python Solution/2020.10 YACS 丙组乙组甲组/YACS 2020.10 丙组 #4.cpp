#include<bits/stdc++.h>
using namespace std;
int a[2000002],b[2000002],n,minprice,maxprofit;


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);    
    cin>>n;
    for (int i = 0; i < n; i++) cin>>a[i];
    for (int i = 0; i < n; i++) cin>>b[i];

    minprice = a[0];
    maxprofit = 0;

    for (int i = 1; i < n; i++)
    {
        minprice = min(minprice, a[i]);
        maxprofit = max(maxprofit, b[i] - minprice);
    }
    cout<<maxprofit<<endl;
    return 0;
}