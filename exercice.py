#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	sous_total = data[0][1]*data[0][2] + data[1][1]*data[1][2]
	taxes = sous_total *0.15
	total = sous_total + taxes

	result = name
	bill_lines = [("SOUS TOTAL", sous_total), ("TAXES     ", taxes), ("TOTAL     ", total)]
	for line in bill_lines:
		result += "\n" + f"{line[0]} {line[1]: 10.2f} $"

	return result


def format_number(number, num_decimal_digits):
	flip, space, result = False, 0, ""
	if number < 0:
		number, flip = number * (-1), True
	full = int(number)
	decimal = number % 1
	full = str(full)
	
	for i in range(len(full)):
		space += 1
		print(i)
		if space < 3:
			result = full[len(full)-i-1] + result
		if space == 3:
			result = " " + full[len(full)-i-1] + result
			space = 0

	decimal = int(round(decimal* (10**num_decimal_digits)))

	if flip:
		result = "-" + result
	
	return result + "." + str(decimal)

def get_triangle(num_rows):
	# print("+" * (num_rows + num_rows + 1))
	# for i in range(num_rows+1):
	# 	if i != 0:
	# 		print("+" + " " * (num_rows-i) + "A" * (i+i-1) + " " * (num_rows-i) + "+")
	# print("+" * (num_rows + num_rows + 1))
	
	triangle = "+" * (num_rows + num_rows + 1)
	for i in range(1,num_rows+1):
		triangle += "\n" + "+" + " " * (num_rows-i) + "A" * (i+i-1) + " " * (num_rows-i) + "+"
	triangle += "\n" + "+" * (num_rows + num_rows + 1)
	return triangle

def seperate(times):
	i = 0
	while i < times:
		print("- - - - - - - -")
		i += 1


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))
	seperate(1)
	print(format_number(-12345.678, 2))
	seperate(1)
	print(get_triangle(2))
	seperate(1)
	print(get_triangle(5))
