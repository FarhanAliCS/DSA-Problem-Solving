import heapq

numbers=[10,20,30,40,50]
heapq.heapify(numbers)
heapq.heappush(numbers,2)
print(numbers)
print("Smallest :",numbers[0])