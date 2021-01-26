#include <bits/stdc++.h>
using namespace std;
int n,m,s, ans=99999;
vector<int> results;

int maxlist(int tmp[51]){
    int tmpans=0;
    for(int i=0;i< n; i++) tmpans = max(tmpans,tmp[i]);
    return tmpans;
}

void dfs(int power[51],int circles, int tt)
{
    // tt: time_taken
    if (circles==0){ans = min(ans, tt); return;}

    int max_v = maxlist(power);

    for(int speed=1;speed<=n;speed++){
        if (max_v<(speed*speed) || (circles-speed) < 0) break;
        
        int newlist[51];
        for(int i=0;i< n; i++) newlist[i] = power[i]-speed;

        for(int i=0;i< n; i++){
            if (newlist[i] == max_v-speed){ 
                newlist[i] = newlist[i]+speed-speed*speed; 
                break;
            }
        }
        dfs(newlist, circles-speed, tt+1);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin>>n>>m>>s;

    int value[51];
    for (int i=0;i<n;i++) value[i]=m;
    dfs(value,s,0);

    cout<<ans<<endl;
    return 0;
}