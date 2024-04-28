#include <iostream>
using namespace std;

void getInputAndUpdatePrevious() {
	static int previousInput = 0; // Initialize previousInput to 0
	cout << "Previous input: " << previousInput << endl;

	// Get new input
	int newInput;
	cout << "Enter a new integer: ";
	cin >> newInput;

	previousInput = newInput; // Update previousInput with new input
}

int main() {
	getInputAndUpdatePrevious();
	return 0;
}