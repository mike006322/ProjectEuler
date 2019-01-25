#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>

//https://www.hackerrank.com/contests/projecteuler/challenges/euler013

using namespace std;

const int base = 1000000000;

struct bigInt {
	vector<int> a;

	bigInt(vector<int> b) {
		a = b;
	}

	bigInt operator + (const bigInt &v) const {
		// make copies of the two vectors, s and t, then manipulate those copies
		vector<int> s = a;
		vector<int> t = v.a;
		int num_of_digits = max(s.size(), t.size());
		while (s.size() < num_of_digits)
			s.insert(s.begin(), 0);
		while (t.size() < num_of_digits)
			t.insert(t.begin(), 0);
		bool carry_one = false;
		for (int i = 0; i < num_of_digits; i++) {
			int q = t[num_of_digits - 1 - i] + s[num_of_digits - 1 - i];
			if (carry_one)
				q++;
			t[num_of_digits - 1 - i] = q % 10;
			if (q > 9) {
				carry_one = true;
			}
			else carry_one = false;
		}
		if (carry_one)
			t.insert(t.begin(), 1);
		return bigInt(t);
	}
};

ostream& operator << (ostream& stream, const bigInt& other) {
	for (auto i : other.a)
		stream << i;
	return stream;
}

int main() {
	
	int t;
	cin >> t;
	bigInt res(vector<int>(1, 0));
	
	for (int i = 0; i < t; i++) {
		vector<int> a;
		string s;
		cin >> s;
		//getline(cin, s);
		for (int j = 0; j < 50; j++) {
			a.push_back((int)s[j] - '0');
		}
		bigInt b(a);
		res = res + b;
	}
	for (int i = 0; i < 10; i++)
		cout << res.a[i];
	

}
