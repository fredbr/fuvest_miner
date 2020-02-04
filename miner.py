#!/usr/bin/env python3

import parser
from pdfminer.layout import LAParams
from pdfminer.high_level import extract_text
from sys import argv
import re

layout = LAParams(line_overlap = 0.5,
                  boxes_flow = 0.7)

default_filters = [
	lambda t: len(t) > 1,
	lambda t: not t.isupper(),
	lambda t: re.match(r'\d+/\d+', t) == None,
	lambda t: re.search(r'FUVEST', t) == None,
	lambda t: re.search(r'Matrícula', t) == None,
	lambda t: re.match(r'^(?:De )|(?:Até )', t) == None,
]

def apply_filters(filters, array):
	for f in filters:
		array = filter(f, array)

	return array

def get_names(text):
	is_name = lambda t: re.match(r'\d+', t) == None

	names = list(filter(is_name, text))

	return names

def get_courses(text):
	is_digits = lambda t: re.match(r'\d+', t) != None

	courses = map(lambda t: t.split()[1], filter(is_digits, text))

	return courses

def get_pairs(text):
	return zip(get_names(text), get_courses(text))

def main():
	file_name, course_filter = parser.parse()
	
	text = extract_text(file_name, laparams=layout).split('\n')

	text = list(apply_filters(default_filters, text))

	students = get_pairs(text)

	names = [name for name, course in students if course == course_filter]

	for name in names:
		print(name)

if __name__ == '__main__':
	main()