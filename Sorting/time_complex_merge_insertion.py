import random
import time

def time_complexity():
    results = []
    # Running on random interval of 10 starting array 12 designed to run for 10 times. 
    for n in range(12, 121, 10):
        arr = [random.randint(0, 1000) for _ in range(n)]
        
        start_time = time.time()
        insertion_sort(arr.copy())
        insertion_time = time.time() - start_time

        start_time = time.time()
        merge_sort(arr.copy())
        merge_time = time.time() - start_time

        results.append((n, insertion_time, merge_time))
    return results

results = time_complexity()
print(results)
