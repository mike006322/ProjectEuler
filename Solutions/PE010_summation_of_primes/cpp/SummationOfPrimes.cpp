#include <iostream>
#include <vector>
#include <math.h>

//https://www.hackerrank.com/contests/projecteuler/challenges/euler010

using namespace std;

vector<long> primeSums(long n) {
	// Return bool vector of size = n + 1
	// index i is the sum of primes less than i
	// uses Sieve of Eratosthenes to find primes
	vector<long> table;
	for (long i = 0; i < n + 1; i++)
		table.push_back(1);
	long i = 3;
	while (i <= sqrt(n)) {
		if (table[i]) {
			long j = 1;
			while (i + j * i <= n) {
				table[i + j * i] = 3;
				j++;
			}
		}
		i += 2;
	}
	table[1] = 0;
	table[0] = 0;
	long s = 0;
	if (n > 1) {
		s = 2;
		table[2] = 2;
	}
	else s = 0;
	for (long i = 3; i < n + 1; i++) {
		if (i % 2 == 0)
			table[i] = 3;
		if (table[i] == 1) {
			s += i;
			table[i] = s;
		}
		else table[i] = s;
	}
	return table;
}

int main() {
	vector<long> sums = primeSums(1000000);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		long n;
		cin >> n;
		cout << sums[n] << endl;
	}
}
