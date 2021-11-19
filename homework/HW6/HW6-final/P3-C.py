from P3 import NaivePriorityQueue, HeapPriorityQueue, PythonHeapPriorityQueue, timeit
import matplotlib.pyplot as plt

timeNaive = timeit(pqclass = NaivePriorityQueue)
timeHeap = timeit(pqclass=HeapPriorityQueue)
timePython = timeit(pqclass=PythonHeapPriorityQueue)
ns=(10, 20, 50, 100, 200, 500)

plt.plot(ns, timeNaive, label = "Naive")
plt.plot(ns, timeHeap, label = "Heap")
plt.plot(ns, timePython, label = "PythonHeap")
plt.legend(frameon = False)
plt.xlabel("Number of Lists Merged")
plt.ylabel("Elapsed time in seconds")
plt.title("Comparison of different priority queues")

plt.savefig("P3-C.png")
plt.show()


