def sum(*args): 
    total = 0
    for num in args:
        total += num
    return total

print(sum(*(int(x) for x in input("Enter numbers to sum, separated by spaces: ").split())))