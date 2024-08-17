def roman_to_integer(roman):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in roman:
        current_value = roman_values[char]
        
        if current_value > prev_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value
        
        prev_value = current_value
    
    return total

roman_numeral = input("Enter a Roman numeral: ")
integer_value = roman_to_integer(roman_numeral)
print(f"The integer value of {roman_numeral} is {integer_value}.")
#include <iostream>
using namespace std;
int main() {
    int score;
    cout<<"Enter score :";
    cin>>score;
    if (score >= 33) {
        if (score >= 90) {
            cout<<"Grade : A+";
        } else if (score >= 80) {
            cout<<"Grade : A";
        } else if (score >= 70) {
            cout<<"Grade : B+";
        } else if (score >= 60) {
            cout<<"Grade : C";
        } else if (33 <= score <=60) {
            cout<<"Grade : P";
        } 
    } else {
            cout
