#include <iostream>
#include <vector>
#include <set>
#include <math.h>

//https://www.hackerrank.com/contests/projecteuler/challenges/euler005

using namespace std;

vector<int> SieveOfEratosthenese(int n) {
	// Return list of primes less than n
	vector<int> res;
	res.push_back(2);
	int i = 3;
	set<int> marked;
	while (i <= sqrt(n)) {
		if (marked.find(i) == marked.end()) {
			res.push_back(i);
			int j = 0;
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

long long SmallestMultiple(int n) {
	//Find all primes less than n
	//For each prime, multiply the result by the highest power of the prime less than or equal to n
	if (n == 1)
		return 1;
	long long res = 1;
	vector<int> primes = SieveOfEratosthenese(n);
	for (auto p : primes) {
		int i = 1;
		while (pow(p, i + 1) <= n) 
			i++;
		res *= pow(p, i);
	}
	return res;
}

int main() {
	int t;
	cin >> t;
	for (int a0 = 0; a0 < t; a0++) {
		int n;
		cin >> n;
		cout << SmallestMultiple(n) << endl;
	}
}