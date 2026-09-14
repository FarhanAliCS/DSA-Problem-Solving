arr=[1,2,3,5,6,7]
n=len(arr)+1
expected_sum = n*(n+1)/2
print(expected_sum)

actual_sum=0
for i in arr:
    actual_sum+=i

missing_number=expected_sum-actual_sum
print(missing_number)



