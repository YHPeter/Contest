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
            cout<<"No"<<endl;
            return 0;
        } 
    }
    for (int i = 0; i < n; ++i){
        cout<<i<<"-"<<endl;
        for (int j = 0; j < n; ++j){
            vector<int> yy;
            auto ll = set_intersection(tt[i].begin(),tt[i].end(),tt[j].begin(),tt[j].end(),yy.begin());
            yy.resize(ll-yy.begin());
            if (yy.size()!=1) {
                cout<<"No"<<endl;
                return 0;
            }
        }
    }
    cout<<"Yes"<<endl;
    return 0;
}