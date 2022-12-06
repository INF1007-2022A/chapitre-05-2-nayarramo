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

	decimalstr = format_decimal(number, num_decimal_digits)
	wholestr = format_whole(number)
	
	return (("-") if number < 0 else "") + f"{wholestr}" + decimalstr

def format_whole(number):
	whole = int(abs(number))

	wholestr = ""
	while whole > 999:
		if wholestr != "":
			wholestr = " " + wholestr
		groupOf3 = whole % 1000
		whole = whole // 1000
		wholestr = str(groupOf3) + wholestr
	if whole < 1000 and whole != 0:
		if wholestr == "":
			wholestr = str(whole) + wholestr
		else:
			wholestr = str(whole) + " " + wholestr
	
	return wholestr

def format_decimal(number, num_decimal_digits):
	numberstr = str(number)
	idxdec = numberstr.rfind(".")
	decstr = numberstr[idxdec:]
	
	if len(decstr) > (num_decimal_digits+1):
		decstr = decstr[:num_decimal_digits+1]
	
	while len(decstr) < (num_decimal_digits + 1):
		decstr += "0"
	
	return decstr

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
