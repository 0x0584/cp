//		   File:	nizar-and-grades.c
//		 Author:	Anas - 0x0584
//	Description:	find the middle grade or grades?
//					the trick is to test if # grades is odd to take middle,
//					or even take last of half-one and first of half-two
//
//	  Created: <2019-07-08 Mon 17:01:21>
//	  Updated: <2019-07-08 Mon 21:27:39>

#include <iostream>
#include <string>

int		sum(int *arr, short size)
{
	int sum = 0;

	for (short i = 0; i < size; ++i)
		sum += arr[i];
	std::cout << sum;
	return sum;
}

void	print_middle(int *arr, short size)
{
	int mids[2] = {
		INT_MIN, INT_MAX
	}, value = sum(arr, size) / 2;

	std::cout << value;

	for (short i = 0; i < size; ++i) {
		mids[0] = (arr[i] <= value && arr[i] > mids[0]) ? arr[i] : mids[0];
		mids[1] = (arr[i] >= value && arr[i] < mids[1]) ? arr[i] : mids[1];
	}

	if (mids[0] != mids[1])
		std::cout << mids[0] << " " << mids[1] << std::endl;
	else
		std::cout << mids[0] << std::endl;
}

int		main(int argc, char *argv[])
{
	short tst = 0, n_tests, single_test_size;

	std::cin >> n_tests;
	std::cin >> single_test_size;

	int arr[single_test_size];
	while (tst++ < n_tests)
	{
		for(int i = 0; i < single_test_size; i++)
			std::cin >> arr[i];
		print_middle(arr, single_test_size);
	}

	return 0;
}

// D. #247588
