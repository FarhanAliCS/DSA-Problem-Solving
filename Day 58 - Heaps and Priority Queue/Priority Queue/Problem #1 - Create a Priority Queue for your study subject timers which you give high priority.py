import heapq
subjects=[]

heapq.heappush(subjects,(3,"Study Python"))
heapq.heappush(subjects,(1,"Complete Assignment"))
heapq.heappush(subjects,(2,"Practive DSA"))
heapq.heappush(subjects,(4,"Read AI/ML"))

while subjects:
    priority,subject=heapq.heappop(subjects)
    print(priority,subject)