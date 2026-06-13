def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(*(int(x) for x in input("Enter numbers to sum, separated by spaces: ").split())))