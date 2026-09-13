def search():
    numbers=[43,23,56,78,65]

    try:
        target=int(input("Enter target :"))
    except ValueError:
        print("Invalid input for int() .")
        return
    
    found=False
    for i in range(len(numbers)):
        if numbers[i] == target:
            print("Target found on index :",i)
            found=True
            return

    if not found:
        print("Target not found .")


search()
