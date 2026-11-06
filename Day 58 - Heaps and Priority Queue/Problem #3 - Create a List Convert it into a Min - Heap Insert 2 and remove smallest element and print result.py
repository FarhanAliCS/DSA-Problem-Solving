import heapq

numbers = [40,10,30,5,20]

heapq.heapify(numbers)
heapq.heappush(numbers , 2)
removed_smallest=heapq.heappop(numbers)
print("Removed Element :",removed_smallest)
print("Update Heap :",numbers)