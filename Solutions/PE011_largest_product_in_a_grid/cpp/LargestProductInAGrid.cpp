#include <iostream>

//https://www.hackerrank.com/contests/projecteuler/challenges/euler011/submissions/code/1312537382

using namespace std;

void checkHorz(int numbers[20][20], long &m) {
	for (int i = 0; i < 20; i++) {
		for (int j = 0; j < 17; j++) {
			long s = numbers[i][j] * numbers[i][j+1] * numbers[i][j+2] * numbers[i][j+3];
			m = s > m ? s : m;
		}
	}
}

void checkVert(int numbers[20][20], long &m) {
	for (int i = 0; i < 17; i++) {
		for (int j = 0; j < 20; j++) {
			long s = numbers[i][j] * numbers[i+1][j] * numbers[i+2][j] * numbers[i+3][j];
			m = s > m ? s : m;
		}
	}
}

void checkUpDiag(int numbers[20][20], long &m) {
	for (int i = 3; i < 20; i++) {
		for (int j = 0; j < 17; j++) {
			long s = numbers[i][j] * numbers[i - 1][j + 1] * numbers[i - 2][j + 2] * numbers[i - 3][j + 3];
			m = s > m ? s : m;
		}
	}
}

void checkDownDiag(int numbers[20][20], long &m) {
	for (int i = 0; i < 17; i++) {
		for (int j = 0; j < 17; j++) {
			long s = numbers[i][j] * numbers[i + 1][j + 1] * numbers[i + 2][j + 2] * numbers[i + 3][j + 3];
			m = s > m ? s : m;
		}
	}
}

int main() {
	long m = 0;
	int numbers[20][20];
	for (int i = 0; i < 20; i++) {
		for (int j = 0; j < 20; j++)
			cin >> numbers[i][j];
	}
	checkHorz(numbers, m);
	checkVert(numbers, m);
	checkUpDiag(numbers, m);
	checkDownDiag(numbers, m);
	cout << m;
	/*
	for (int i = 0; i < 20; i++) {
		for (int j = 0; j < 20; j++)
			cout << numbers[i][j] << " ";
		cout << endl;
	}
	*/

}