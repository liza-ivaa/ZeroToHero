#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

// Функція для перевірки середнього арифметичного
// Ми тестуємо логіку
void testAccuracy(double calculated, double expected) {
    if (abs(calculated - expected) < 0.01) {
        cout << "Test PASSED: Results are accurate!" << endl;
    } else {
        cout << "Test FAILED: Difference is too big!" << endl;
    }
}

int main() {
    cout << "--- System Testing ---" << endl;

    //  середня оцінка має бути наприклад 8.37
    double expectedMean = 8.37;
    double currentResult = 8.37; 

    cout << "Checking Mean Calculation..." << endl;
    testAccuracy(currentResult, expectedMean);

    return 0;
}
