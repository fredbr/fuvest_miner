#!/usr/bin/env python3

from pdfminer.layout import LAParams
from pdfminer.high_level import extract_text
from sys import argv
import re

layout = LAParams(line_overlap = 0.5,
                  boxes_flow = 0)

def main():
	if len(argv) != 3:
		exit(1)

	file_name = argv[1]
	course = argv[2]
	
	text = extract_text(file_name, laparams=layout)

	text = text.strip()
	text = text.split('\n')

	text = filter(lambda t: len(t) > 1, text)

	text = filter(lambda t: not t.isupper(), text)

	text = filter(lambda t: re.match(r'\d+/\d+', t) == None, text)

	text = filter(lambda t: re.search(r'FUVEST', t) == None, text)
	text = filter(lambda t: re.search(r'Matrícula', t) == None, text)

	text = filter(lambda t: re.match(r'^(?:De )|(?:Até )', t) == None, text)

	text = list(text)

	is_name = lambda t: re.match(r'\d+', t) == None
	is_digits = lambda t: re.match(r'\d+', t) != None

	names = list(filter(is_name, text))

	courses = map(lambda t: t.split()[1], filter(is_digits, text))

	v = dict(zip(names, courses))

	final = [key for key, value in v.items() if value == course]

	for nome in final:
		print(nome)

if __name__ == '__main__':
	main()