#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <vector>


/*
  This is a very simplistic way to find the answer, and I'm sure there
  are quicker ways to do it. This is just a slow, simple approach.

  This approach just iterates through all coin combination
  possibilities and sees which match the desired total.
 */
unsigned int num_ways_to_make_num(unsigned int num)
{
	//stores the total number of ways
	unsigned int total = 0;
	
	unsigned int p200_upper_amount = num / 200;

	for (int p200 = 0; p200 <= p200_upper_amount; p200++)
	{
		unsigned int p100_upper_amount = num / 100;

		std::cout << "p200: " << p200 << "\n";

		for (int p100 = 0; p100 <= p100_upper_amount; p100++)
		{
			unsigned int p50_upper_amount = num / 50;

			std::cout << "p100: " << p100 << "\n";

			for (int p50 = 0; p50 <= p50_upper_amount; p50++)
			{
				unsigned int p20_upper_amount = num / 20;

				std::cout << "p50: " << p50 << "\n";

				for (int p20 = 0; p20 <= p20_upper_amount; p20++)
				{
					unsigned int p10_upper_amount = num / 10;

					for (int p10 = 0; p10 <= p10_upper_amount; p10++)
					{
						unsigned int p5_upper_amount = num / 5;

						for (int p5 = 0; p5 <= p5_upper_amount; p5++)
						{
							unsigned int p2_upper_amount = num / 2;

							for (int p2 = 0; p2 <= p2_upper_amount; p2++)
							{
								unsigned int p1_upper_amount = num / 1;

								for (int p1 = 0; p1 <= p1_upper_amount; p1++)
								{
									//work out the coin total.
									unsigned int curr_total =
										p1 * 1 +
										p2 * 2 +
										p5 * 5 +
										p10 * 10 +
										p20 * 20 +
										p50 * 50 +
										p100 * 100 +
										p200 * 200;

									//if it's what we want, increase the counter.
									if (curr_total == num)
									{
										total++;
									}
								}
							}
						}
					}
				}
			}
		}	
	}

	//return the total
	return total;
}


int main(int argc, char** argv)
{
	//this stores N for the Nth powers we're trying to find.
	unsigned int target_num = 0;

	// if the program arguments aren't right.
	if (argc != 2)
	{
		// complain and exit.
		std::cout << "ERROR: incorrect number of arguments." << "\n";
		std::cout << "\tprogram <num>" << "\n";
		exit(1);
	}

	//extract the values from the arguments.
	target_num = atoi(argv[1]);

	//calculate and print the answer.
	unsigned int answer = num_ways_to_make_num(target_num);
	std::cout << "There are " << answer << " ways to make up " << target_num << "p" << "\n";
	
	return 0;
}
