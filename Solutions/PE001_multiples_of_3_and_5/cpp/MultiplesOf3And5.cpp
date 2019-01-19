#include <iostream>

//https://www.hackerrank.com/contests/projecteuler/challenges/euler001

using namespace std;

long int SumOneTo(long int n){
    return n*(n+1)/2;
}

long int MultiplesOf3And5(long int n){
    long int NumberOfMultiplesOf3, NumberOfMultiplesOf5, NumberOfMultiplesOf15;
    long int SumOfMultiplesOf3, SumOfMultiplesOf5, SumOfMultiplesOf15;
    NumberOfMultiplesOf3 = (n-1)/3;
    NumberOfMultiplesOf5 = (n-1)/5;
    NumberOfMultiplesOf15 = (n-1)/15;
    SumOfMultiplesOf3 = 3*SumOneTo(NumberOfMultiplesOf3);
    SumOfMultiplesOf5 = 5*SumOneTo(NumberOfMultiplesOf5);
    SumOfMultiplesOf15 = 15*SumOneTo(NumberOfMultiplesOf15);
    return SumOfMultiplesOf3 + SumOfMultiplesOf5 - SumOfMultiplesOf15;
}

int main()
{
    int t;

    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int n;
        cin >> n;
        cout << MultiplesOf3And5(n) << endl;
    }
    return 0;
}
