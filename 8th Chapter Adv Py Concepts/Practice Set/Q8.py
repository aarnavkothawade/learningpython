while (a := input("Enter a string: ")) != "quit":
    print(a)

list = ["python", "rocks", "ai", "aa"]
long_names = [name for name in list if (length := len(name)) >= 4]
print(long_names)
