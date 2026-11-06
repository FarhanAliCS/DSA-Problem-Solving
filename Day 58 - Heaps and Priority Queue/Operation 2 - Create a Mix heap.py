import heapq

numbers=[20,10,30,5,15]

mix_heap=[-num for num in numbers]

heapq.heapify(mix_heap)

heapq.heappush(mix_heap,-50)
removed=-heapq.heappop(mix_heap)
mix_heap=[-num for num in mix_heap]
print("Removed Element :",removed)
print("Mix heap :",mix_heap)
