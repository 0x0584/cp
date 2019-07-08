/*		   File:	c.c
 *	Description:	the idea is to keep only the last n digits while
 *					computing the n-th power!
 *
 *		 Author:	Anas Rchid
 *
 *	  Created: <2019-07-08 Mon 13:06:12>
 *	  Updated: <2019-07-08 Mon 19:08:28>
 */

#include <stdio.h>
#include <stdlib.h>

# define IS_DIGIT(c)		(c >= '0' && c <= '9')

typedef unsigned int	uint32_t;

uint32_t	foo(uint32_t number, uint32_t n)
{
	uint32_t result = number;

	while (n--)
		result *= number;
	return number;
}

uint32_t	last_digits(uint32_t k, uint32_t a, uint32_t n)
{
	uint32_t result = 1;
	uint32_t power, ten_pow;

	for (power = 1; power <= n; power++) {
		ten_pow = foo(10, k);
		result = (result * a) % ten_pow;
	}
	return result;
}

void		clear_buff(char *buff, short len)
{
	while (len--)
		buff[len] = '\0';
}

int			main(void)
{
	uint32_t i, n_tests, sum;
	char *buff, *walk;
	struct {
		uint32_t a, n, k;
	} *array;

	scanf("%u", &n_tests);

	if (n_tests > 20) return -1;
	if (!(buff = malloc(0xff)) || !(array = malloc(n_tests * sizeof *array)))
		return 2;

	i = 0;
	while (i < n_tests) {
		scanf("%u %u %u", &array[i].a, &array[i].n, &array[i].k);
		i++;
	}

	i = 0;
	while (i < n_tests) {
		bzero(buff, 0xff);
		sprintf(buff, "%d", last_digits(array[i].k, array[i].a, array[i].n));
		walk = buff, sum = 0;
		while(*walk && isdigit(*walk)){
			printf("*walk = %c\n", *walk);
			sum += *walk++ - '0';}
		printf("%u\n", sum);
		i++;
	}

	free(array);
	free(buff);

	return 0;
}
