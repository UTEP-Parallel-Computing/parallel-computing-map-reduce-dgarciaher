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