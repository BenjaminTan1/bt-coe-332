#include <iostream>

//Tests if the input is a prime.
bool test_If_Prime(int input);
//Input indicate the number of primes printed.
void multiple_Primes(int input);

int main() {
	int how_many;
	std::cin>>how_many;
	multiple_Primes(how_many);
	return 0;
}

bool test_If_Prime(int input) {
	//Checks evens, 1, and 3.
	if (input == 1 || input == 2 || input == 3) {
		return true;
	}
	else if (input % 2 == 0) {
		return false;
	}

	//Checks odds until half input
	int i = 3;
	while (i <= input / 2) {
		if (input % i == 0) {
			return false;
		}
		i += 2;
	}
	return true;
}

void multiple_Primes(int input) {
	int number_of_primes_found = 0;
	for (int i = 2; number_of_primes_found < input; i++) {
		if(test_If_Prime(i)) {
			std::cout<<i<<"\n";
			number_of_primes_found++;
		}
	}
}