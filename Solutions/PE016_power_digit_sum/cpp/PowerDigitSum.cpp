#include <iostream>

//https://www.hackerrank.com/contests/projecteuler/challenges/euler016
// n <= 10^4

using namespace std;

int * getSums() {
	//returns a pointer to an array representing sums of digits of 2^n for n up to 10000
	static int sum[10001];
	int product[10001], carry;
	for (int i = 0; i < 10001; i++) {
		product[i] = -1;
		sum[i] = 0;
	}
	//'product' is an array of integers < 10 representing the digits of 2^n
	//'product' starts at 2 and get multiplied by 2 with a for loop
	//for each incriment of the for loop sum is recorded
	product[10000] = 2;
	sum[0] = 2;
	for (int k = 1; k <= 10000; k++) {
		int j = 10000;
		carry = 0;
		while (j >= 0) {
			if (product[j] == -1) {
				break;
			}
			product[j] *= 2;
			product[j] += carry;
			carry = product[j] / 10;
			product[j] = product[j] % 10;
			sum[k] += product[j];
			j--;
		}
		if (carry > 0) {
			sum[k] += carry;
			product[j] = carry;
		}
	}
	return sum;
}


int main() {
	int *sums;
	sums = getSums();
	int t, n;
	cin >> t;
	int i = 0;
	while (i < t) {
		cin >> n;
		cout << sums[n - 1] << endl;
		i++;
	}
	return 0;
}
