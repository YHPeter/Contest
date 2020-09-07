#include<bits/stdc++.h>
using namespace std;
int n,ans,dou[100010],curs;
vector<int> ni;

int findmax(int begin,int tile){
    int cur = dou[begin],max_ = dou[tile];
    for (int i = begin; i < tile; i++)
    {
        cur = max(0,cur)+dou[i];
        max_ = max(max_,cur);
    }
    return max_;
}
int findmin(int begin,int tile){
    int cur = dou[begin],min_ = dou[tile],sum;
    for (int i = begin; i < tile; i++)
    {
        cur = min(0,cur)+dou[i];
        min_ = min(min_,cur);
        sum = sum+ dou[i];
    }
    return sum-min_;
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin>>n;
    for (int i = 0; i < n; i++)
    {   
        cin>>curs;
        if(curs<0) ni.push_back(i);
        dou[i] = curs;
    }
    ans = max(findmax(0,n),findmin(0,n))-n;//很神奇！！！官网跑出来的结果全多了n，只能减n保全对
    cout<<ans<<endl;
    return 0;
}