print("Starting Program...")

import time
import pymp
import re

def word_counter(thread_num):

    start_time = time.time()
    
    loading_file_start_time = time.time()
    
    files = []
    
    for i in range(1,9):
        file_name = "shakespeare" + str(i) + ".txt"
        file = open(file_name, "r", encoding="utf8")
        files.append(file.read())
        #file.close()
    
    words_of_interest = ["hate", "love", "death", "night", "sleep", "time", "henry", "hamlet", "you", "my", "blood", "poison", "macbeth", "king", "heart", "honest"]
    
    results_dict = pymp.shared.dict()
    
    
        
    loading_file_time = time.time() - loading_file_start_time
    print("Finished loading files with time:", loading_file_time)
    
    with pymp.Parallel(thread_num) as p:
        thread_lock = p.lock
        for word in words_of_interest:
            results_dict[word] = 0
        for f in p.iterate(files):
            word_count_time = time.time()
            for word in words_of_interest:
                f = f.replace('\n', ' ').replace('\r', '').lower()
                f = re.sub(r'[^a-z ]+', '', f)
        
                num = f.split(" ").count(word)
        
                thread_lock.acquire()
                results_dict[word] += num
                thread_lock.release()
            time_taken = time.time() - word_count_time
            print("Finished reading file with time: ", time_taken)
            
    time_taken = time.time() - start_time
    print(results_dict)      
    print("Time taken:", time_taken)
    
print("-------Using 2 threads")
word_counter(2)

file1 = open("shakespeare1.txt", "r", encoding="utf8")
file2 = open("shakespeare2.txt", "r", encoding="utf8")
file3 = open("shakespeare3.txt", "r", encoding="utf8")
file4 = open("shakespeare4.txt", "r", encoding="utf8")
file5 = open("shakespeare5.txt", "r", encoding="utf8")
file6 = open("shakespeare6.txt", "r", encoding="utf8")
file7 = open("shakespeare7.txt", "r", encoding="utf8")
file8 = open("shakespeare8.txt", "r", encoding="utf8")

files = [file1, file2, file3, file4, file5, file6, file7, file8]  # putting all files in a list for easy access


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

#word_dictionary = pymp.shared.dict(word_dictionary)
#file_names = pymp.shared.list(file_names)

thread_num = 2

print("\n")
print("threads used:", thread_num , "\n\n")
#lock = lock()

totalTimeStart = time.time()
print("----------------starting program-----------------")

with pymp.Parallel(thread_num) as p1:
    #lock = p1.lock()
    for i in p1.range(len(files)):
        
        fTimeStart = time.time()
        f = files[i]
        print("--------",f)

        for line in f:

            line = line.strip()
            line = line.lower()
            line = line.strip(".,';()")  # removes special characters that might be attached to the word
            wLine = line.split(" ")  # getting all words in every line separated by a space

            for w in wLine:
                wTimeStart = time.time()
                
                #lock.acquire()
                with p1.lock:
                    if w in word_dictionary:
                        word_dictionary[w] += 1
                #lock.release()
                wTimeStop = time.time()

        fTimeStop = time.time()
        print("time for file no.", i+1, ": ",(fTimeStop-fTimeStart) , "\n")

totalTimeStop = time.time()
print("\n")
print("total time of parallel program", (totalTimeStop-totalTimeStart), "\n\n")


print("--------------word dictionary--------------")
for i in list(word_dictionary.keys()):
    print(i, ": ", word_dictionary[i])

print("-------------------------------------------")
