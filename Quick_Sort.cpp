#include<bits/stdc++.h>
using namespace std;
int part(int arr[],int lb,int ub){
    int pivot=arr[lb];
    int start=lb,end=ub;
    while(start<end){
        while(start<=ub && arr[start]<=pivot) start++;
        while(end>lb && arr[end]>pivot) end--;
        if(start<end){
            swap(arr[start],arr[end]);
        }
    }
    swap(arr[lb],arr[end]);
    return end;
}
void quicksort(int arr[],int lb,int ub){
    if(lb<ub){
        int loc=part(arr,lb,ub);
        quicksort(arr,lb,loc-1);
        quicksort(arr,loc+1,ub);
    }
}
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    quicksort(arr,0,n-1);
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}
