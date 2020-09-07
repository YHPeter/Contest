#include<bits/stdc++.h>
using namespace std;
int n,T,ans,sellor[10001][2];

int main()
{
    cin>>n>>T;
    for (int i = 0; i < n; i++)
    {   
        cin>>sellor[i][0]>>sellor[i][1];
    }
    int dp[n][T];
    memset(dp,0,sizeof(dp));
    for (int i = 0; i < n; i++)
    {   
        for (int t = 0; t < T; t++)
        {
            if(T-sellor[i][0]*t-sellor[i][1]<0){
                dp[i][t] = dp[i-1][t-1];
            }
            else{
                int x;
                if(i-1<0 || t - sellor[i][0]*t-sellor[i][1] - 1 <0) x = 0;
                else x = dp[i - 1][t - sellor[i][0]*t-sellor[i][1] - 1];
                dp[i][t] = max(x + 1,dp[i - 1][t]);
            }
        }
    }
    int ans = dp[n-1][T-1]+1;
    cout<<ans<<endl;
    return 0;
}