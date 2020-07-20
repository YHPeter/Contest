// sample answer from https://iai.sh.cn/contribution/214
#include<bits/stdc++.h>
using namespace std;
int n,m,k,num[1 << 25];
long long ans,inv_33 = 1,mod;

void S_search(int dep,int state)
{
	if(dep == 0) num[state]++;
	else for(int i = 1;i <= 26;++i) S_search(dep - 1,((state * 33) ^ i) & mod);
}

void E_search(int dep,int state) {
	if(dep == 0) ans += num[state];
	else for(int i = 1;i <= 26;++i) E_search(dep - 1,((state ^ i) * inv_33) & mod);
}

int main()
{
	cin>>m>>k>>n;
	mod = (1 << m) - 1;
	while(((inv_33 * 33) & mod) != 1) inv_33 = (inv_33 * 33) & mod; 
	S_search(n / 2,0);
	E_search(n - (n / 2),k);
	cout<<ans<<endl;
}