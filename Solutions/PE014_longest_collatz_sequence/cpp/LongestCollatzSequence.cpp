#include <iostream>
#include <map>
#include <vector>

// https://www.hackerrank.com/contests/projecteuler/challenges/euler014

using namespace std;

long nextCollatz(long n) {
	//returns next number in collatz sequence
	if (n % 2 == 0)
		n >>= 1;
	else
		n = 3 * n + 1;
	return n;
}

map<long, long> cache;
const long cachesize = 100000;

long collatzSequenceLength(long n) {
	if (n == 1)
		return 1;
	else {
		if (n < cachesize and cache.find(n) != cache.end())
			return cache[n];
		long m = nextCollatz(n);
		long res = 1 + collatzSequenceLength(m);
		if (n < cachesize)
			cache[n] = res;
		return res;
	}
}

vector<long> longestCollatzSoFar(long N) {
	//returns a vector where index i is the number less than or equal to i that produces the longest collatz sequence
	cache[1] = 1;
	vector<long> longestSoFar;
	for (long i = 0; i < N + 1; i++)
		longestSoFar.push_back(1);
	long i = 2;
	long m = 1;
	long m_index = 1;
	while (i <= N) {
		long size = collatzSequenceLength(i);
		if (size >= m) {
			m = size;
			m_index = i;
		}
		longestSoFar[i] = m_index;
		i++;
	}
	return longestSoFar;
}


int main() {
	vector<long> res = longestCollatzSoFar(5000000);
	long t;
	cin >> t;
	for (long i = 0; i < t; i++) {
		long n;
		cin >> n;
		cout << res[n] << endl;
	}

}