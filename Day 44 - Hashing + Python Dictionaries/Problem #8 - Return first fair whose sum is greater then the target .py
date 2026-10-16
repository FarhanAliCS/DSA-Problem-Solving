def first_sum(numbers , target):
    seen=set()

    for num in numbers:
        required=target - num
        if required in seen:
            return required , num
        seen.add(num)

    return None



numbers=[3,2,1,5,6,7]
target=5
print(first_sum(numbers, target))