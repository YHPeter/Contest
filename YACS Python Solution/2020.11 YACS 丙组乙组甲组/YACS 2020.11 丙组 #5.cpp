#include<bits/stdc++.h>
#include <algorithm>
using namespace std;

int gstart=0,gend=0,ll,rr,ans,n;

vector<vector<int>> x;

bool startstol(vector<int> a,vector<int> b) //start from small to large
{ 
    return a[0] < b[0];
} 
bool endltos(vector<int> a,vector<int> b) //end from large to small
{ 
    return a[1] > b[1];
} 

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>n>>ans;

    for (int i = 0; i < n; i++)
    {   
        vector<int> tmp(2, 0);
        cin>>tmp[1]>>tmp[0];
        if (tmp[1]>tmp[0]) x.push_back(tmp);
    }

    sort(x.begin(),x.end(),endltos);
    sort(x.begin(),x.end(),startstol);

    vector<int> tmp(2, 0);
    tmp[0] = ans;
    tmp[1] = ans;
    x.push_back(tmp);

    for(int i=0; i<x.size(); i++) {
        ll = x[i][0];
        rr = x[i][1];
        if(ll>=gend){
            ans = ans+(gend-gstart)*2;
            gstart = ll;
            gend = rr;
        }
        else gend = max(gend,rr);
    }
    cout<<ans<<endl;
    
    return 0;
}