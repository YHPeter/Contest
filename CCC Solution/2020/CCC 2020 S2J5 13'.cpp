#include<bits/stdc++.h>
using namespace std;
int row,cloumn,max_ad;
map<int,set<int>> adj;
int n,c;
set<int> visited;

void search(int cur, set<int> vis){
    if(cur==1) {
        cout<<"yes"<<endl; 
        exit(0);
    }
    if (adj.find(cur)==adj.end()) return;
    for(int i: adj[cur]){
        if(vis.count(i)==0){
            vis.insert(i);
            search(i,vis);
            vis.erase(i);
        }
    }
}

int main() {
    cin>>row>>cloumn;
    max_ad = row*cloumn;
    for (int i = 1; i <= row; i++) {
        for (int j = 1; j <= cloumn; j++) {
            cin>>n;
            c = i*j;
            if (c<=max_ad && n<=max_ad) adj[n].insert(c);
        }
    }
    visited.insert(max_ad);
    search(max_ad,visited);
    cout<<"no"<<endl;
    return 0;
}