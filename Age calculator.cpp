#include <iostream>
#include <ctime>

using namespace std;

int main() {
    // Get current year
    time_t now = time(0);
    tm *ltm = localtime(&now);
    int currentYear = 1900 + ltm->tm_year;

    // Input birth year
    int birthYear;
    cout << "Enter your birth year: ";
    cin >> birthYear;

    // Calculate age
    int age = currentYear - birthYear;

    // Output age
    cout << "You are " << age << " years old." << endl;

    return 0;
}

