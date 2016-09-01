import time

loop = 1000 * 1000 * 100
i = 0

start = time.time()

while i < loop:
    i = i + 1

end = time.time()

print("Elapsed time: %f" % (end - start))
print("Throughput: %f loops/sec" % (loop / (end - start)))
