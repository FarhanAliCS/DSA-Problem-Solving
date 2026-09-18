arr = [10, 5, 8, 21, 14, 7, 18, 3]

for i in range(len(arr)):
    if arr[i]%2 == 0  and arr[i] > 10 :
        print(i)
        break
