#include <bits/stdc++.h>
using namespace std;
int lcs(string a, string b, int len1, int len2, string &lcs_result){
    int LCS[len1+1][len2+1];
    for(int i=0;i<=len1;i++){
        for(int j=0;j<=len2;j++){
            if(i==0 || j==0) LCS[i][j]=0;
            else if(a[i-1]==b[j-1]) LCS[i][j]=1+LCS[i-1][j-1];
            else LCS[i][j]=max(LCS[i-1][j],LCS[i][j-1]);
        }
    }
    int i=len1,j=len2;
    while(i>0 && j>0){
        if (a[i-1]==b[j-1]){
            lcs_result=a[i-1]+lcs_result;  // Add the matched character to the LCS string
            i--; j--;
        }
        else if(LCS[i-1][j] > LCS[i][j-1]) i--;  // Move up if the LCS value above is greater
        else j--;  // Move left if the LCS value left is greater

    }
    return LCS[len1][len2];
}
int main(){
    string a,b;
    cin>>a>>b;
    int len1=a.size(), len2=b.size();
    string lcs_result = "";

    cout<<"Length of longest common subsequence: "<<lcs(a,b,len1,len2,lcs_result)<<endl;
    cout << "The LCS is: " << lcs_result << endl;
    return 0;
}
