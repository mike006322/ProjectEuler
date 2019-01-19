#include <iostream>
#include <math.h>

//https://www.hackerrank.com/contests/projecteuler/challenges/euler003

using namespace std;

long LargestPrimeFactor(long n) {
	long max = n;
	if (n % 2 == 0) {
		while (n % 2 == 0)
			n /= 2;
	}
	long i = 3;
	long res = 1;
	while (i <= sqrt(max) + 1) {
		if (n % i == 0) {
			res = i;
			n /= i;
		}
		else
			i += 2;
	}
	if (n > 2)
		return n;
	else
		return res;
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		long n;
		cin >> n;
		cout << LargestPrimeFactor(n) << endl;
	}
}
