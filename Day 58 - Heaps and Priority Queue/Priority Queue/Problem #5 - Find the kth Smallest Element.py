import heapq

def priority_queue(numbers , k):

    heapq.heapify(numbers)
    for _ in range(k):
        k_smallest=heapq.heappop(numbers)
    return k_smallest


numbers=[10,4,25,8,30,15,40,2]
k=3
print(priority_queue(numbers ,k))
    
