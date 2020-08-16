#include<bits/stdc++.h>
#include <iostream>
using namespace std;
string n,h,tmp;
int ans,hl,nl;
set<string> checked;
map<string,int> sta;
map<string,int> curCount;

map<string,int> counter (string str) {
    map<string,int> ini = {{"q",0}, {"w",0}, {"e",0}, {"r",0}, {"t",0}, {"y",0}, {"u",0}, {"i",0}, {"o",0}, {"p",0}, {"a",0}, {"s",0}, {"d",0}, {"f",0}, {"g",0}, {"h",0}, {"j",0}, {"k",0}, {"l",0}, {"z",0}, {"x",0}, {"c",0}, {"v",0}, {"b",0}, {"n",0}, {"m",0}, {"#",0}};
    for (int i = 0; i < str.size(); i++){
        string tar;
        tar = str[i];
        ini[tar]++;
    }
    return ini;
}

int main(){
    ios_base::sync_with_stdio(0);
    std::cin.tie(0);
    std::cin>>n;
    std::cin>>h;
    h = "#"+h;
    hl = h.size();
    nl = n.size();
    sta = counter(n);
    tmp = h.substr(0,nl);
    curCount = counter(tmp);
    for (int i = 1; i <= hl-nl; i++){
        string q,w;
        q = h[i-1];
        w = h[i+nl-1];
        curCount[q]--;
        curCount[w]++;
        tmp = h.substr(i,nl);
        // cout<<tmp<<endl;
        if (checked.find(tmp) == checked.end() && curCount==sta){
            ans++;
            checked.insert(tmp);
        }
    }
    cout<<ans<<endl;
    return 0;
}