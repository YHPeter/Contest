#include<bits/stdc++.h>
using namespace std;
int s[100001],n,l,ans;

int main()
{
    cin>>n>>l;
    ans = 0;
    for (int i = 0; i < n; i++)
    {
        cin>>s[i];
    }
    sort(s,s+n);
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
    return 0;
}