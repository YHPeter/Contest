#include<bits/stdc++.h>
using namespace std;
int n,m,a[100002],ll,rr,mid;

bool check(int minh){
    int value=0,j=0;
    for (int i = 0; i < n; i++)
    {
        while(j<m && value<minh) {
            value = value+a[j];
            j++;
        }
        if (value<minh) return false;
        value = value/2;
    }
    return true;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin>>n>>m;
    for (int i = 0; i < m; i++) {
        cin>>a[i];
        rr = rr+a[i];
    }
    while(rr>ll+1){
        mid = (rr+ll)/2;
        if(check(mid)) ll=mid;
        else rr=mid;
    }
    cout<<ll<<endl;
}