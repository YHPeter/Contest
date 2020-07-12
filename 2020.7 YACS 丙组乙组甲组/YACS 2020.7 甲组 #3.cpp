// YACS 2020.7 甲组 #3
#include<bits/stdc++.h>
using namespace std;
string s,new_s;
int num,ind=0,ans=0;


int main()
{
    cin>>s;
    int new_list[600000];
    s = '#'+s;
    int n = s.size();
    for(int i = 1; i < n; ++i){
        if (s[i] == s[i-1]){
            num+=1;
        }
        else{
            new_s+=s[i];
            new_list[ind++] = {num};
            num = 1;
        }
    }
    new_list[ind++] = {num};
    for (int i = 0; i < n; ++i) new_list[i] = {new_list[i+1]};
    s = new_s;
    int start=0,end=0,g_start=0,len=0,i=0;
    while(i<n){
        start=i,end=i;
        while(i<n-1 && s[end]==s[end+1])
            end++;
        i=end+1;
        while(start-1>=0 && end+1<n && s[start-1]==s[end+1]){
            start--;
            end++;
        }
        if(len<end-start+1){
            len=end-start+1;
            g_start=start;
        }
    }
    int x = g_start + len;
    for(int i = g_start; i < x; ++i) ans+=new_list[i];
	cout<<ans<<endl;
    // <<s.substr(g_start,len)
	return 0;
}