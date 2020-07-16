#include<bits/stdc++.h>
using namespace std;

int s,t,dp[100000000];

int main()
{
    cin>>s>>t;
    dp[s]=0;
    dp[s+1]=1;
    for (int i = s+1; i <= t+1; ++i){
        int x = floor(i/2);
        if (i%2==0) dp[i] = min(dp[i-1],dp[x]+1);
        else dp[i] = dp[i-1]+1;
    }
    cout<<dp[t]<<endl;
    return 0;
}
