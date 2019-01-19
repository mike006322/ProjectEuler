#include <iostream>
#include <vector>
#include <map>

//https://www.hackerrank.com/contests/projecteuler/challenges/euler002

using namespace std;

map<long, long> cache;

long int Fib(long int n) {
	if (cache.find(n) != cache.end())
		return cache[n];
	else {
		if (n == 1)
			return 1;
		else if (n == 2)
			return 2;
		else if (n > 2) {
			cache[n] = Fib(n - 1) + Fib(n - 2);
			return cache[n];
		}
		else
			return 1;
	}
}

long int EvenFib(long int n) {
	//returns the sum of the even valued fibonacci numbers less than or equal to n
	vector<long int> EvenFibLessThann;
	long int i = 1;
	long int fib_i = 1;
	while (fib_i <= n) {
		if (fib_i % 2 == 0)
			EvenFibLessThann.push_back(fib_i);
		i++;
		fib_i = Fib(i);
	}
	long int sum_of_elems = 0;
	for (auto i : EvenFibLessThann)
		sum_of_elems += i;
	return sum_of_elems;
}

int main() {
	int t;
	cin >> t;
	for (int a0 = 0; a0 < t; a0++) {
		long int n;
		cin >> n;
		cout << EvenFib(n) << endl;
	}
}
