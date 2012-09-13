#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <vector>

int main(int argc, char** argv)
{
	//this stores N for the Nth powers we're trying to find.
	unsigned int num_power = 0;

	// if the program arguments aren't right.
	if (argc != 2)
	{
		// complain and exit.
		std::cout << "ERROR: incorrect number of arguments." << "\n";
		std::cout << "\tprogram <num>" << "\n";
		exit(1);
	}

	//extract the values from the arguments.
	num_power = atoi(argv[1]);

	//display the max values.
	std::cout << "num_power = " << num_power << "\n";

	// this stores the highest number we'll try when looking for
	// numbers the sum of whose digits^N = the number.  I'm sure
	// there's an actual formula to work out exactly what this should
	// be, based on num_power, but I don't know what it is.
	unsigned int upper_limit = 1000000;
	//This is the max number of digits we'll have in a number when
	//searching.
	unsigned int max_digits = log10(upper_limit) + 1;

	std::cout << "max number of digits " << max_digits << "\n";

	//this array stores the individual digits of the current number.
	unsigned int curr_nums[num_power];

	//this vector stores the valid numbers we find (numbers for which
	//the sum of digits^num_power = number).
	std::vector<unsigned int> valid_numbers;

	//go through every number from 2 to upper limit.
	for (int i = 2; i < upper_limit; ++i)
	{
		//loop max_digits times
		for (int j = 0; j < max_digits; ++j)
		{
			//and extract the current digit using mod and integer
			//division (to avoid needing to convert to a string).
			//this does create leading 0's, but they don't matter,
			//since 0^x = 0, which does not affect the sum.
			curr_nums[j] = abs(i) % (unsigned int)pow(10, j+1);
			curr_nums[j] = curr_nums[j] / (unsigned int)pow(10, j);
		}

		//this stores the sum of the digits^num_power
		unsigned int total = 0;

		//loop through each digit
		for (int j = 0; j < max_digits; ++j)u
		{
			//add the digit^num_power to total.
			total += pow(curr_nums[j], num_power);
		}

		// if the digit sum is the current number.
		if (total == i)
		{
			//add it to the valid_numbers vector.
			valid_numbers.push_back(i);
			std::cout << "the digits of " << i << " to the power of " << num_power << " sum to " << i << "\n";
		}
	}

	//this holds the sum of all the valid numbers.
	unsigned int final_answer = 0;

	//get the total sum by summing all the valid numbers.
	for (std::vector<unsigned int>::iterator i = valid_numbers.begin(); i != valid_numbers.end(); i++)
	{
		final_answer += *i;
	}

	//display the sum of valid numbers.
	std::cout << "the sum of all the valid numbers is " << final_answer << "\n";

	return 0;
}
