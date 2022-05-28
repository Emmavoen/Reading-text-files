def read_file_content(filename):
	with open(filename, 'r') as f:
		file = f.read()
		
	return file
	
output = read_file_content("./story.txt")
print(output)

def count_words(str):
	counts = dict()
	text = str.split()
	
	for x in text:
		if x in counts:
			counts[x] += 1
		else:
			counts[x] = 1
			
	return counts
print(count_words(output))