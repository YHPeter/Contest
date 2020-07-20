// YACS 2020.5 乙组 #4

#include<bits/stdc++.h>
#include <set>
using namespace std;
int n,m,k,cur;
map<int,set<int>> tt;

int main()
{
    cin>>n>>m>>k;
    for (int i = 0; i < n; ++i) {
        set<int> s{};
        for (int j = 0; j < m; ++j) {
            cin>>cur;
            s.insert(cur);
        }
        if (s.size()==m) tt[i] = s;
        else {
            cout<<"NO"<<endl;
            return 0;
        } 
    }
    for (int i = 0; i < 200; ++i){
        // if (i)
        for (int j = i+1; j < n; ++j){
            vector<int> oo;
            set_intersection(tt[i].begin(),tt[i].end(),tt[j].begin(),tt[j].end(), back_inserter(oo));
            if (oo.size()!=1) {
                cout<<"NO"<<endl;
                return 0;
            }
        }
    }
    cout<<"YES"<<endl;
    return 0;
}



// sample answer from https://iai.sh.cn/contribution/209
#include<bits/stdc++.h>
using namespace std;
int n,m,k,edge[11000],num[110];
bool e[10010][10010];
int check2() 
{
	for(int i = 1;i <= m;++i)
		for(int j = 1;j <= m;++j)
			if(i == j)continue;
			else if(num[i] != num[j] && e[num[i]][num[j]] == 0) e[num[i]][num[j]] = 1;
			else return 0;
	return 1;
}

int check0(int sum) 
{
	for(int i = 1;i <= m;++i) sum -= edge[num[i]];
	for(int i = 1;i <= m;++i) edge[num[i]]++;
	return (sum == 0);
}

int main()
{	
	cin>>n>>m>>k;
    for(int i = 1;i <= n;++i) {
    	for(int j = 1;j <= m;++j) cin>>num[j];
		if(!check2() || !check0(i - 1)) {
			cout<<"NO"<<endl;
			return 0;
		}
	}
	cout<<"YES"<<endl;
    return 0;
}