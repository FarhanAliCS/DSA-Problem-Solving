def find_missing_number(numbers):
    seen=set()
    for num in numbers:
        seen.add(num)

    for i in range(1,len(numbers)+2):
        if i not in seen:
            return i
                    


numbers=[1,2,3,5,6,7]
print(find_missing_number(numbers))