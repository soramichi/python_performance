import time

loop = 1000 * 1000 * 100
i = 0

start = time.time()

for i in range(0, loop):
    continue

end = time.time()

print("Elapsed time: %f" % (end - start))
print("Throughput: %f loops/sec" % (loop / (end - start)))
