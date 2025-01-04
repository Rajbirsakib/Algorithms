#include <bits/stdc++.h>
using namespace std;
int lcs(int len1, int len2, string a, string b){
    if(len1==0 || len2==0) return 0;
    else if(a[len1-1]==b[len2-1]) return 1+lcs(len1-1,len2-1,a,b);
    else return max(lcs(len1-1,len2,a,b), lcs(len1,len2-1,a,b));
}
int main(){
    string a,b;
    cin>>a>>b;
    int len1=a.size(), len2=b.size();
    cout<<"Length of longest common subsequence: "<<lcs(len1,len2,a,b)<<endl;
    return 0;
}
