#include <iostream>
#include <math.h>
#include <vector>
#include <set>
#include <map>

//https://www.hackerrank.com/contests/projecteuler/challenges/euler012

using namespace std;

vector<long> fastSieveOfEratosthenes(long n) {
	vector<bool> sieve((int)n / 2, true);
	for (int i = 3; i < sqrt(n) + 1; i += 2) {
		if (sieve[i / 2]) {
			for (int j = i * i / 2; j < sieve.size(); j += i) {
				sieve[j] = false;
			}
		}
	}
	vector<long> res;
	res.push_back(2);
	for (long i = 1; i < n / 2; i++) {
		if (sieve[i])
			res.push_back(2 * i + 1);
	}
	return res;
}

int countDivisors(int n, vector<long> primes) {
	//counts divisors using a vector of primes
	int i = 0;
	int res = 1;
	while (primes[i] <= n) {
		long p = primes[i];
		int count = 0;
		while (n%p == 0) {
			count++;
			n /= p;
		}
		if (count > 0)
			res *= count + 1;
		i++;
	}
	return res;
}

map<int, long> triangleNumberWithNDivisors(long n) {
	int i = 1;
	long triangle = 1;
	int divisors = 1;
	int m = 1;
	map<int, long> table;
	table[0] = triangle;
	vector<long> primes = fastSieveOfEratosthenes(100000);
	while (divisors <= n) {
		i++;
		triangle += i;
		divisors = countDivisors(triangle, primes);
		if (divisors > m) {
			for (int j = m; j < divisors; j++)
				table[j] = triangle;
			m = divisors;
		}
	}
	return table;
}

int main() {
	map<int, long > table = triangleNumberWithNDivisors(1000);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int n;
		cin >> n;
		cout << table[n] << endl;
	}

}
