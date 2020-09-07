#include<bits/stdc++.h>
using namespace std;
int s[100001],n,l,ans=0;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin>>n>>l;
    for (int i = 0; i < n; i++)
    {
        cin>>s[i];
    }
    for (int i = 0; i < n; i++)
    {
        int start = s[i];
        int j = 1;
        while ((i+j)<n && s[i+j]-start<=l){
            j++;
            ans++;
        }
    }
    cout<<ans<<endl;
    
}