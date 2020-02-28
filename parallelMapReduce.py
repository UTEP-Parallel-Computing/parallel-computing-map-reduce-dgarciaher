import numpy as np
import time
import pymp

file1 = open("shakespeare1.txt", "r", encoding="utf8")
file2 = open("shakespeare2.txt", "r", encoding="utf8")
file3 = open("shakespeare3.txt", "r", encoding="utf8")
file4 = open("shakespeare4.txt", "r", encoding="utf8")
file5 = open("shakespeare5.txt", "r", encoding="utf8")
file6 = open("shakespeare6.txt", "r", encoding="utf8")
file7 = open("shakespeare7.txt", "r", encoding="utf8")
file8 = open("shakespeare8.txt", "r", encoding="utf8")

files = [file1, file2, file3, file4, file5, file6, file7, file8]  # putting all files in a list for easy access
p_list = pymp.shared.array(files)

word_dictionary = {
					"hate": 0,
					"love": 0,
					"death": 0,
					"night": 0,
					"sleep": 0,
					"time": 0,
					"henry": 0,
					"hamlet": 0,
					"you": 0,
					"my": 0,
					"blood": 0,
					"poison": 0,
					"macbeth": 0,
					"king": 0,
					"heart": 0,
					"honest": 0
				}

# p_dictionary = pymp.shared.dict()

thread_num = 2

print("\n")
print("threads used:", thread_num , "\n\n")

totalTimeStart = time.time()

with pymp.Parallel(thread_num) as p1:

	# lock = p1.lock()
	
	for i in p1.range(len(p_list)):

		fTimeStart = time.time()
		f = files[i]

		for line in f:

			line = line.strip()
			line = line.lower()
			line = line.strip(".,';()")  # removes special characters that might be attached to the word
			wLine = line.split(" ")  # getting all words in every line separated by a space

			for w in wLine:
				with p1.lock:

					if w in word_dictionary:
						word_dictionary[w] += 1

		fTimeStop = time.time()
		p1.print("time for file no.", i+1, ": ",(fTimeStop-fTimeStart) , "\n")

totalTimeStop = time.time()
print("\n")
print("total time of parallel program", (totalTimeStop-totalTimeStart), "\n\n")


print("--------------word dictionary--------------")
for i in list(word_dictionary.keys()):
	print(i, ": ", word_dictionary[i])

print("-------------------------------------------")