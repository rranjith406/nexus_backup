from difflib import Differ

with open('config.txt') as file_1, open('temp') as file_2:
	differ = Differ()

	for line in differ.compare(file_1.readlines(), file_2.readlines()):
		print(line)

