import multiprocessing
from multiprocessing.pool import Pool
import os
import numpy as np

cpus = os.cpu_count()
   
if __name__ == '__main__':
   
   arr = np.array([i for i in range(0, 10000000)]).tolist()

   chunks = [arr[i:i + cpus] for i in range(0, len(arr), cpus)]
   
   result = 0
   
   with Pool(cpus) as pool:
     result = pool.map(sum, chunks)
   
   print(sum(result))





   
