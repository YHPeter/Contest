// YACS 2020.7 丙组 #4
#include<bits/stdc++.h>
using namespace std;
int ans,n,k,t;
int a[20000]={0},arr[20000][20000]={0};
int main() 
{   
	cin>>n>>k;
    for(int i = 0; i < n; i++){
        cin>>t;
        arr[i][i] = {t % k};
        }

    for(int i = 0; i < n; i++){
        for(int j = i; j < n; j++) {
            if (j!=i) arr[i][j] = {(arr[i][j-1]+arr[j][j])%k};
            if (arr[i][j]==0) ans+=1;
        }
    }
	cout<<ans<<endl;
	return 0;
}

// smapel answer from https://iai.sh.cn/contribution/235
#include<bits/stdc++.h>
using namespace std;
int n,k,x,sum[200100];
int main()
{	 
	cin>>n>>k;
	
	for(int i = 1;i <= n;++i) {
		cin>>x;
		sum[i] = (sum[i - 1] + x) % k;
	}
	
	for(int r = 1;r <= n;++r)
		for(int l = 1;l <= r;++l)
			if(sum[r] == sum[l - 1])ans++;
			
	cout<<ans<<endl;
	
	return 0;
}