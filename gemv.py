import numpy as np
import random
import multiprocessing as mp
import time

# size should be a multiply of num_procs
size = 8 * 1024
num_procs = 4

def do_memory_intensive_work(A, B, x, n_mul):
    for _ in range(0, n_mul):
        B = A * x

def main():
    n_mul = 40
    
    print("init done.")

    procs = []

    start = time.time()
    
    for i in range(0, num_procs):
        A = np.random.rand(size, size / num_procs)
        B = np.zeros([size, size / num_procs])
        x = np.random.rand(size, 1)
        
        p = mp.Process(target=do_memory_intensive_work, args = (A, B, x, n_mul))
        procs.append(p)

    print("created all threads.")
        
    for p in procs:
        p.start()
        
    for p in procs:
        p.join()

    end = time.time()

    print("Elapsed_time: %f (s)" % (end - start))
    print("Throughput: %f (mul/s)" % (n_mul / (end - start)))
    
if __name__ == "__main__":
    main()
