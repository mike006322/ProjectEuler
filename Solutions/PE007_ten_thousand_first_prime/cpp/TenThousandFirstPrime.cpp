#include <iostream>
#include <vector>
#include <set>
#include <math.h>

//https://www.hackerrank.com/contests/projecteuler/challenges/euler007

using namespace std;

vector<long> SieveOfEratosthenese(int n) {
	// Return list of primes less than n
	vector<long> res;
	res.push_back(2);
	int i = 3;
	set<long> marked;
	while (i <= sqrt(n)) {
		if (marked.find(i) == marked.end()) {
			res.push_back(i);
			long j = 0;
			while (j <= n / i) {
				marked.insert(i + j * i);
				j++;
			}
		}
		i += 2;
	}
	while (i <= n) {
		if (marked.find(i) == marked.end())
			res.push_back(i);
		i += 2;
	}
	return res;
}

int main() {
	vector<long> First10000Primes = SieveOfEratosthenese(104729);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int n;
		cin >> n;
		cout << First10000Primes[n-1] << endl;
	}
}
