#include <iostream>
#include <vector>
#include <set>
#include <math.h>
#include <string>
#include <set>
#include <tuple>

//https://www.hackerrank.com/contests/projecteuler/challenges/euler009

using namespace std;

vector<vector<int>> generatePrimiticePythagoreanTriples(int N) {
	//generates all primitive pythagorean triples such that a + b + c <= n
	vector<vector<int>> res;
	int n = 1;
	while (n < N / 3 + 1) {
		int m = n + 1;
		while (2 * m*n + 2 * pow(m, 2) <= N) {
			vector<int> t;
			t.push_back(2 * m*n);
			t.push_back(m*m - n * n);
			t.push_back(m*m + n * n);
			res.push_back(t);
			m++;
		}
		n++;
	}
	return res;
}

vector<tuple<int, int, int>> checkMultiplesOfPrimitives(vector<vector<int>> primitives, int N) {
	//for each triple in the list of primitives it finds all multiples such that k(a + b + c) = n
	//returns a set of the triples
	vector<tuple<int, int, int>>  res;
	for (auto triple : primitives) {
		int i = 1;
		int sum = 0;
		for (auto t : triple) 
			sum += t;
		while (i*sum <= N) {
			if (i*sum == N) {
				int d = 0;
				int array_triple[3];
				for (auto b : triple) {
					array_triple[d] = b;
					d++;
				}
				tuple<int, int, int> tuple_triple = make_tuple(i*array_triple[0], i*array_triple[1], i*array_triple[2]);
				res.push_back(tuple_triple);
			}
			i++;
		}
	}
	return res;
}


int chooseLargest(vector<tuple<int, int, int>> triples) {
	//returns the largest product of a triple
	if (triples.size() == 0)
		return -1;
	int m = 0;
	for (auto triple : triples) {
		int product = get<0>(triple) * get<1>(triple) * get<2>(triple);
		if (product > m)
			m = product;
	}
	return m;
}

int specialPythagorean(int N) {
	if (N % 2 != 0)
		return -1;
	vector<vector<int>> primitives = generatePrimiticePythagoreanTriples(N);
	vector<tuple<int, int, int>> triples = checkMultiplesOfPrimitives(primitives, N);
	int m = chooseLargest(triples);
	return m;
}

int main () {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int n;
		cin >> n;
		cout << specialPythagorean(n) << endl;
	}

}