import heapq

def priority_queue(numbers , k):
    numbers=[-num for num in numbers]
    heapq.heapify(numbers)
    for _ in range(k):
        removed=-heapq.heappop(numbers)
    return removed


numbers=[10,4,25,8,30,15,40,2]
k=3
print(priority_queue(numbers ,k))
    