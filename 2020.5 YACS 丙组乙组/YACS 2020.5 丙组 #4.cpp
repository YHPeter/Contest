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

// c++ 题解的方法： https://iai.sh.cn/contribution/116
#include<bits/stdc++.h>
using namespace std;
int s,t,ans;
int main()
{
	cin>>s>>t;
	while(t > s) {
		if(t % 2 == 1) t--;
		else if(t / 2 >= s)t /= 2;
		else break;
		ans++;
	}
	
	cout<<ans + (t - s)<<endl;
	return 0;
}