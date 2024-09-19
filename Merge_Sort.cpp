#include<bits/stdc++.h>
using namespace std;
void marge(int arr[],int low,int mid,int high){
    int n1=mid-low+1;
    int n2=high-mid;
    int arr1[n1],arr2[n2];
    for(int i=0;i<n1;i++) arr1[i]=arr[low+i];
    for(int i=0;i<n2;i++) arr2[i]=arr[mid+1+i];
    int i=0,j=0,k=low;
    while(i<n1 && j<n2){
        if(arr1[i]<arr2[j]){
            arr[k]=arr1[i]; k++; i++;
        }
        else{
            arr[k]=arr2[j]; k++; j++;
        }
    }
    while(i<n1){
        arr[k]=arr1[i]; k++; i++;
    }
    while(j<n2){
        arr[k]=arr2[j]; k++; j++;
    }
}
void margesort(int arr[],int low,int high){
    if(low<high){
        int mid=(low+high)/2;
        margesort(arr,low,mid);
        margesort(arr,mid+1,high);
        marge(arr,low,mid,high);
    }
}
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    margesort(arr,0,n-1);
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}
