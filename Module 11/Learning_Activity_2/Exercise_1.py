lines = ['Readme', 'How to write text files in Python']
with open('readme.txt', 'w') as f:
	for line in lines:
		f.write(line)
		f.write('\n')