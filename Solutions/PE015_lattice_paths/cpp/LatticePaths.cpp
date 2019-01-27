#include <iostream>

// https://www.hackerrank.com/contests/projecteuler/challenges/euler015

using namespace std;

long long gcdExtended(long long a, long long b, long long *x, long long *y)
{
	if (a == 0)
	{
		*x = 0, *y = 1;
		return b;
	}

	long long x1, y1;
	long long gcd = gcdExtended(b%a, a, &x1, &y1);
	*x = y1 - (b / a) * x1;
	*y = x1;
	return gcd;
}

long long modInverse(long long a, long long m)
{
	long long x, y;
	long long g = gcdExtended(a, m, &x, &y);
	int res = (x%m + m) % m;
	return res;
}

long long latticePaths(int n, int m) {
	long long res = 1;
	long long m_fac = 1;
	long long mod = 1000000007;
	for (int i = n + 1; i < n + m + 1; i++) {
		res *= i;
		res %= mod;
	}
	for (int i = 1; i < m + 1; i++) {
		res *= modInverse(i, mod);
		res %= mod;
	}
	return res;
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		long long n, m;
		cin >> n >> m;
		cout << latticePaths(n, m) << endl;
	}
}