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
	whole = int(abs(number))
	decimal = abs(number) % 1

	decimalstr = str(int(round(decimal * 10**num_decimal_digits)))
	decimalstr = "." + decimalstr + "0" * (num_decimal_digits - len(decimalstr))

	if abs(number) > 999:
		wholestr = str(whole)
		result = ""
		while whole > 999:
			if result!= "": 
				result = " " + result
			result = wholestr[-3:] + result
			print(result)
			whole = whole // 1000
			wholestr = str(whole)
			print(whole)
		if whole != 0:
			result = wholestr + " " + result
		print((("-") if number < 0 else "") + f"{result}" + decimalstr)
	else:
		result = abs(number)
	return (("-") if number < 0 else "") + f"{result}" + decimalstr

def get_triangle(num_rows):
	
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
