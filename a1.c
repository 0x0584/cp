/*
		   File:	a1.c
		 Author:	anas rchid
	Description:	This is a naive approach.. and number theory approach

	  Created: <2019-07-08 Mon 02:12:28>
	  Updated: <2019-07-08 Mon 10:31:37>

	  Link: https://codeforces.com/contest/1184/problem/A1
*/

#define HASH_LIMIT_OUTPUT								1e12

#include <math.h>
#include <limits.h>
#include <stdio.h>

typedef unsigned	long long uint128_t;

const uint128_t r = HASH_LIMIT_OUTPUT;

uint128_t	hash_function(uint128_t u, uint128_t v)
{
	return (u * u + 2 * u * v + u + 1);
}

void		bad_reverse_hash(uint128_t *u, uint128_t *v, uint128_t hash)
{
	uint128_t tmp[2] = {0, 0};

	if (!u || !v) return ;
	while (tmp[0] < HASH_LIMIT_OUTPUT)
	{
		while (tmp[1] < HASH_LIMIT_OUTPUT)
		{
			if (hash_function(tmp[0], tmp[1]) == hash)
			{
				*u = tmp[0];
				*v = tmp[1];
				break;
			}
			tmp[1]++;
		}
		tmp[0]++;
	}
}

/*
 *
 * Solution: (x, y) is the positive integer pair, r is a positive integer.
 *
 *		r = hash(x, y) =>  x = (-(2y + 1) + sqrt((2y + 1)^2 + 4 * (r - 1))) / 2
 *
 * Proof of correctness:
 *
 * in number theory, we can turn that equation into the following:
 *
 *		x^2 + x(2y + 1) + 1 = r => x^2 + x(2y + 1) - (r - 1) = 0
 *
 * if we try to solve that equation, delta would be (2y + 1)^2 - 4 * (r - 1).
 * and it's clear that delta > 0. and x > 0, thus we're only ineterested in
 * positive. and also we know that 2y + 1 is odd, as well as (2y +1)^2.
 * while 4 * (r - 1) is even. the whole summation is even, thus we can
 * devide by 2.
 */

uint128_t	has_good_sqrt(uint128_t nbr)
{
	uint128_t i = 0;

	if (nbr == 0) return 0;
	while (i < INT_MAX && i * i < nbr)
		i++;
	return i * i == nbr ? i : 0;
}

void		optimal_reverse_hash(uint128_t *u, uint128_t *v, uint128_t hash)
{
	uint128_t y = 0;

	while (y < HASH_LIMIT_OUTPUT)
		if (!has_good_sqrt(y))
		{
			y++;
		}
		else
		{
			*u = (-(2 * y + 1) + sqrt(pow((2 * y + 1), 2) + 4 * (r - 1))) / 2;
			*v = y;
			break;
		}
}

int		main(int argc, char *argv[])
{
	uint128_t x, y;

	optimal_reverse_hash(&x, &y, hash_function(2, 1));
	printf("%llu %llu\n", x, y);

	return 0;
}

/*								-*- 0x0584 -*-								*/
