#include <bits/stdc++.h>
using namespace std;
int n, temp[100002], p[100002];
long long ans;

void merge_sort(int l,int r)
{
    if(l==r) return;

    int mid=l+((r-l)>>1);
    merge_sort(l,mid);
    merge_sort(mid+1,r);

    for(int i=l;i<=r;++i) temp[i]=p[i];

    int i1=l,i2=mid+1;
    for(int i=l;i<=r;++i)
    {
        if(i1>mid) p[i]=temp[i2++];
        else if(i2>r)  p[i]=temp[i1++];
        else if(temp[i1]<=temp[i2]) p[i]=temp[i1++];
        else if(temp[i1]>temp[i2]){ans+=mid-i1+1;p[i]=temp[i2++];}
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>n;
    int a[n], b[n];
    for(int i=0;i<n;i++)cin>>a[i];
    for(int i=0;i<n;i++)cin>>b[i];

    std::map<int,int> keytable;
    for (int i=0;i<n;i++) keytable[a[i]] = i;
    for (int i=0;i<n;i++) p[i] = keytable[b[i]];

    merge_sort(0,n-1);
    cout<<ans<<endl;
    return 0;
}