import string
import sys

#file = open("./sample.s", 'r')
file = open(sys.argv[1], 'r')
d = dict()
funct_list = []
num_of_functions = 0

print("Working on the below file:")
print(sys.argv[1])
print("")

for line in file:
	if line.find('.') == 1:
		continue
	
	# Remove the leading spaces and newline character
	line = line.strip()

	# Convert the characters in line to
	# lowercase to avoid case mismatch
	#line = line.lower()

	if line.find(":") >= 1:
		funct_list.insert(num_of_functions, line)
		num_of_functions += 1
		continue

	# Split the line into words
	words = line.split("\t")

	# Check if the word is already in dictionary
        if words[0] in d:
            # Increment count of word by 1
            d[words[0]] = d[words[0]] + 1
        else:
            # Add the word to dictionary with count 1
            d[words[0]] = 1

print("List of instruction and their usage count")
# Print the contents of dictionary
for key in list(d.keys()):
    print(key,":",d[key])

print("")
# print the number of function find during parsing
print("Number of Functions : ", num_of_functions)
print("list of functions")
print(funct_list)
