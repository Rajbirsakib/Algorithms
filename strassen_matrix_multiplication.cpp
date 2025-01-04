#include <bits/stdc++.h>
using namespace std;
int n;
void str(int a[100][100],int b[100][100], int n){
    int c[100][100];
    if(n<=2){
        int p=(a[0][0]+a[1][1])*(b[0][0]+b[1][1]);
        int q=(a[1][0]+a[1][1])*b[0][0];
        int r=a[0][0]*(b[0][1]-b[1][1]);
        int s=a[1][1]*(b[1][0]-b[0][0]);
        int t=(a[0][0]+a[0][1])*b[1][1];
        int u=(a[1][0]-a[0][0])*(b[0][0]+b[0][1]);
        int v=(a[0][1]-a[1][1])*(b[1][0]+b[1][1]);
        c[0][0]=p+s-t+v;
        c[0][1]=r+t;
        c[1][0]=q+s;
        c[1][1]=p+r-q+u;
        cout<<c[0][0]<<" "<<c[0][1]<<endl;
        cout<<c[1][0]<<" "<<c[1][1]<<endl;
    }
}
int main(){
    int n;
    cin>>n;
    int a[100][100],b[100][100];
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>a[i][j];
        }
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>b[i][j];
        }
    }
    str(a,b,n);
    return 0;
}
