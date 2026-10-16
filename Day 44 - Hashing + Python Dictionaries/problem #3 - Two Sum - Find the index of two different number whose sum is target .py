def two_sum(num,target):
    seen={}
    for i in range(len(num)):
        required= target - num[i]
        if required in seen:
            return i , seen[required]
        else:
            seen[num[i]]=i

    
num=[2,3,4,5,6,7]
target=5
print(two_sum(num , target))