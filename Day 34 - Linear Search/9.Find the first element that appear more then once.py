arr=[4,7,2,9,7,5,2]

seen=set()
for number in arr:
    if number in seen:
        print(number)
        break
    else:
        seen.add(number)
    
    
