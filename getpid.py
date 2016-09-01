import os
import time

#loop = 1000 * 1000 * 5
loop = 10
i = 0

start = time.time()

while i < loop:
    i = i + 1
    v0 = os.getpid()
    print(v0)
    """
    v1 = os.getpid()
    v2 = os.getpid()
    v3 = os.getpid()
    v4 = os.getpid()
    v5 = os.getpid()
    v6 = os.getpid()
    v7 = os.getpid()
    v8 = os.getpid()
    v9 = os.getpid()
    """

end = time.time()

print("Elapsed time: %f" % (end - start))
print("Throughput: %f loops/sec" % (loop / (end - start)))
