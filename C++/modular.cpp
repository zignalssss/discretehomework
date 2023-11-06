#include <iostream>
#include <cmath>
using namespace std;
struct modular{
	int g;
	int s;
	int t;
};
struct modular Ex_gcd(int a,int b){
	struct modular prime,primev2;
	int g,s,t;
	if(b == 0){
		struct modular gcd;
		gcd.g = a;
		gcd.s = 1;
		gcd.t = 0;
		return gcd;
	}
	prime = Ex_gcd(b,a%b);
	g = prime.g;
	s = prime.t;
	t = prime.s - (floor(a/b))*prime.t;
	primev2.g = g;
	primev2.s = s;
	primev2.t = t;
	return primev2;
}
int main(){
	struct modular div;
	int g,s,t,result;
	int a,b,n;
	cin >> a >> b >> n;
	div = Ex_gcd(n,b);
	g = div.g;
	s = div.s;
	t = div.t;
	if(t < 0){
		t += n;
	}
	result = (a*t)%n;
	cout << result;
	return 0;
}
