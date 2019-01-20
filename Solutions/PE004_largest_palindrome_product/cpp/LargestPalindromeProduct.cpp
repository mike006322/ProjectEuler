# include <iostream>
# include <string>

//https://www.hackerrank.com/contests/projecteuler/challenges/euler004

using namespace std;

int NextPalindrome(int n) {
	//takes n and returns the next palindrome number counting down
	string str_n = to_string(n);
	int FirstHalf = stoi(str_n.substr(0, str_n.length() - 3));
	FirstHalf--;
	string FirstHalfStr = to_string(FirstHalf);
	string res = FirstHalfStr + FirstHalfStr.substr(2) + FirstHalfStr[1] + FirstHalfStr[0];
	return stoi(res);

}

bool HasThreeDigitFactors(int n) {
	//incrimints from 101 to 999 looking for 3 digit factors
	//if a 3 digit factor is found then checks if the other factor is 3 digit or moves on
	int i = 100;
	while (i < 1000) {
		if (n % i == 0) {
			int d = n / i;
			if (d > 99 && d < 1000)
				return true;
		}
		i++;
	}
	return false;
}

int LargestPalindromeProduct(int n) {
	//first check if n in palindrome
	//if n is a palindrome, run try_three_digits on it
	//then change n with next_palindrome and keep running try_three_digits
	//if n is not a palindrome then go right to find_next_palindrome
	n--;
	while (to_string(n).substr(0, to_string(n).length() - 3) != to_string(n).substr(5, 1) + to_string(n).substr(4, 1) + to_string(n).substr(3, 1))
		n--;
	while (!HasThreeDigitFactors(n))
		n = NextPalindrome(n);
	return n;
}

int main() {
	int t;
	cin >> t;
	for (int a0 = 0; a0 < t; a0++) {
		int n;
		cin >> n;
		cout << LargestPalindromeProduct(n) << endl;
	}

}
