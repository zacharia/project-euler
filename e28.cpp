#include <iostream>

//this is the dimension of the grid.
#define SPIRAL_SIZE 1001


/*
  This calculates the answer by working out the sequence of the
  numbers that appear on the diagonals. It starts at the central one,
  and goes through every corner spiraling outwards.

  The basic formula is that you start with 1, then add 2 four times,
  then 4 four times, then 6 four times, etc.
 */
int smart_calculation(unsigned int size)
{
	//this stores the current number (i.e. the value of the current
	//diagonal number.
	unsigned int curr_num = 1;
	// this is the amount to increase the curr_num by to get the next
	// diagonal number.
	unsigned int inc_amount = 2;
	// this stores the running total of the diagonal numbers.
	unsigned int total = 1;

	//until the current diagonal number is equal to the dimension of
	//the grid squared (i.e. the top right corner)
	while (curr_num < size * size)
	{
		// for each corner in the current layer.
		for (int i = 0; i < 4; ++i)
		{
			// add the increase amount to get the next corner value.
			curr_num += inc_amount;
			//increase the total by the current corner value.
			total += curr_num;
		}

		//after each four corners, increase the increase_amount by 2.
		inc_amount += 2;
	}

	//return the total.
	return total;
}


int main(int argc, char** argv)
{
	unsigned int result = smart_calculation(SPIRAL_SIZE);
	std::cout << "ANSWER: " << result << "\n";
	return 0;
}
