#!usr/bin/env python3
from multiprocessing.pool import ThreadPool
import os
import time
import numpy as np
import math

cpus = os.cpu_count()

def getPrime(chunk):

    count = 0
    for value in chunk:
        
        if value == 1:
            continue

        if value == 2:
            count +=1
            continue

        square = int(math.sqrt(value))
        
        isPrime = True

        for i in range(2, square + 1):
            if value % i == 0:
                isPrime = False
                break
            
        if isPrime: count+=1
    
    return count
        
    

if __name__ == '__main__':

    arr = np.array([i for i in range(1, 100000)]).tolist()
    
    result = []

    chunks = [arr[i:i + cpus] for i in range(0, len(arr), cpus)]
    
    startTime = time.time()

    with ThreadPool(cpus) as pool:
        result = pool.map(getPrime, chunks)
    
    print(f"Parallel time : {time.time() - startTime} and result : {sum(result)}")

    startTime = time.time()
    result = getPrime(arr)

    print(f"Sequential time : {time.time() - startTime} and result : {result}")
    
