#include <iostream>
#include <math.h>

using namespace std;

long SumSquareDifference(long n) {
	return pow(n, 2)*(pow(n + 1, 2)) / 4 - n*(n + 1)*(2*n + 1) / 6;
}

int main() {
	int t;
	cin >> t;
	for (int a = 0; a < t; a++) {
		long n;
		cin >> n;
		cout << SumSquareDifference(n) << endl;
	}
}