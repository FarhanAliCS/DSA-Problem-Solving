import heapq
numbers=[10,4,25,8,30,15,40,2]
k=3
k_Largest_elements=[]
numbers=[-num for num in numbers]
heapq.heapify(numbers)
for _ in range(k):
    remove=-heapq.heappop(numbers)
    k_Largest_elements.append(remove)

print(k_Largest_elements)

