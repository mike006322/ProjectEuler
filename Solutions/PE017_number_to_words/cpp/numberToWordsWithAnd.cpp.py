#include <iostream>
#include <vector>
#include <string>
#include <iostream>

//https://projecteuler.net/problem=17

using namespace std;

string spellNumWithSpaces(string num) {
    //Input is a number as a string
    //This function returns a string of the number spelled out
    vector<string> tn{ "", "Thousand ", "Million ", "Billion ", "Trillion " };
    vector<string> tens{ "Zero", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    vector<string> o{ "", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ",
     "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "};
    string res = "";
    if (num.length() % 3 == 1) {
        num = "00" + num;
    }
    else if (num.length() % 3 == 2) {
        num = "0" + num;
        }
    if (num == "0") {
        return "Zero";
    }
    while (num.length() > 0) {
        string a = num.substr(0, 3);
        num = num.substr(3);
        if (a.substr(0, 1) != "0") {
            int b = stoi(a);
            res += o[b / 100] + "Hundred ";
            b %= 100;
            if (to_string(b).substr(0, 1) != "0") {
                res += "and ";
                if (b < 20) {
                    res += o[b];
                }
                else {
                    res += tens[b / 10] + " " + o[b % 10];
                }
                res += tn[num.length() / 3];
            }
        }
        else {
            int b = stoi(a);
            if (b < 20) {
                res += o[b];
            }
            else {
                res += tens[b / 10] + " " + o[b % 10];
            }
            if (b != 0) {
                res += tn[num.length() / 3];
            }
        }
    }
    return res;
}


string spellNum(string num) {
    //Input is a number as a string
    //This function returns a string of the number spelled out
    vector<string> tn{ "", "Thousand", "Million", "Billion", "Trillion" };
    vector<string> tens{ "Zero", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety" };
    vector<string> o{ "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
     "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen" };
    string res = "";
    if (num.length() % 3 == 1) {
        num = "00" + num;
    }
    else if (num.length() % 3 == 2) {
        num = "0" + num;
    }
    if (num == "0") {
        return "Zero";
    }
    while (num.length() > 0) {
        string a = num.substr(0, 3);
        num = num.substr(3);
        if (a.substr(0, 1) != "0") {
            int b = stoi(a);
            res += o[b / 100] + "Hundred";
            b %= 100;
            if (to_string(b).substr(0, 1) != "0") {
                res += "and";
                if (b < 20) {
                    res += o[b];
                }
                else {
                    res += tens[b / 10] + o[b % 10];
                }
                res += tn[num.length() / 3];
            }
        }
        else {
            int b = stoi(a);
            if (b < 20) {
                res += o[b];
            }
            else {
                res += tens[b / 10] + o[b % 10];
            }
            if (b != 0) {
                res += tn[num.length() / 3];
            }
        }
    }
    return res;
}


int main() {
    int s = 0;
    int i = 1;
    while (i <= 1000) {
        s += spellNum(to_string(i)).length();
        i++;
    }
    cout << s << endl;
    return 0;
}