def first_repeting_number(num):
    seen={}
    for i in num:
        if i in seen:
            return i
        else:
            seen[i]=1
            

num=[2,3,4,1,1]
print(first_repeting_number(num))