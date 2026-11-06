import heapq
numbers=[10,15,10,20,5]

heapq.heapify(numbers)

smallest=heapq.heappop(numbers)

print("Remove :",smallest)
print("Update Heap :",numbers)
print("New Smallest :",numbers[0])