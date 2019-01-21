#include <iostream>
#include <vector>
#include <set>
#include <math.h>
#include <string>

//https://www.hackerrank.com/contests/projecteuler/challenges/euler008

using namespace std;

long productOfKDigits(string n, int k, int i) {
	//multiplies k digits of num starting at i
	long b = 1;
	int j = 0;
	while (j < k) {
		b *= stoi(n.substr(i+j, 1));
		j++;
	}
	return b;
}

long largestProductInASeries(string n, int k) {
	/*
	n and k are int
	returns the largest product of k digits from n
	start with the product of the first k digits
	then go through and first divide by the last digit and multiply by the next digit in front
	if the last digit is 0, rebuild the product
	compare the product to the maximum product found so far
	*/
	long b = productOfKDigits(n, k, 0);
	int i = k;
	long m = b;
	if (k < n.size()) {
		while (i < n.size()) {
			if (n[i - k] == '0')
				b = productOfKDigits(n, k, i - k + 1);
			else {
				b /= stoi(n.substr(i - k, 1));
				b *= stoi(n.substr(i, 1));
			}
			if (b > m)
				m = b;
			i++;
		}
	}
	return m;
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int n, k;
		cin >> n >> k;
		string num;
		cin >> num;
		cout << largestProductInASeries(num, k) << endl;
	}
}
