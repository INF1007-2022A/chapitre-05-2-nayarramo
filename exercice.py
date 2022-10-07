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
	
	return ""

def get_triangle(num_rows):
	return ""


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
