/*
		   File:	big-power.c
		 Author:	Anas - 0x0584
	Description:	the idea is to keep only the last n digits while
					computing the n-th power using modular arithmetic!

	  Created: <2019-07-08 Mon 12:31:14>
	  Updated: <2019-07-08 Mon 21:24:30>
*/

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define ISDIGIT(c)		(c >= '0' && c <= '9')
#define BUFF_SIZE		16

int	last_digits(int k, int a, int n)
{
	int	result = 1;
	int	power;

	for (power = 1; power <= n; power++)
		result = (result * a) % (int)pow(10, k);
	return result;
}

int			main(void)
{
	int i = 0, n_tests, sum;
	char buff[BUFF_SIZE], *walk;
	struct {
		int a, n, k;
	} array[20];

	scanf("%d", &n_tests);
	while (i < n_tests) {
		scanf("%d %d %d", &array[i].a, &array[i].n, &array[i].k);
		i++;
	}

	i = 0;
	while (i < n_tests) {
		snprintf(buff, BUFF_SIZE, "%d",
				 last_digits(array[i].k, array[i].a, array[i].n));
		walk = buff, sum = 0;
		while(*walk && ISDIGIT(*walk))
			sum += *walk++ - '0';
		while (walk-- > buff)
			*walk = '\0';
		printf("%d\n", sum);
		i++;
	}

	return 0;
}

/*
   fix: remove some headers, replace some function due to a compilation error
		it might be because of the list of allowed functions and flags, probably!
   fix: replace sprintf but snprintf, and change %d to %u
   fix: switch to static memory instead of dynamic
*/
