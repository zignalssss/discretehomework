//O(2^n)
#include <iostream>
using namespace std;
int TillingWalkway(int n){
	int a[n+1];
	if(n <= 2)
		return n;
	a[1] = 1;
	a[2] = 2;
	for(int i = 3;i<n+1;i++){
		a[i] = a[i-1]+a[i-2];
	}
	return a[n];
}
int main(){
	int data;
	cin >> data;
	cout << TillingWalkway(data);
	return 0;
}
