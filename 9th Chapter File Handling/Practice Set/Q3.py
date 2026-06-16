with open("tasks.txt", "w") as f:
    f.write("Hi, my name is Aarnav Kothawade.\n")
    f.write("I am a Second year B. Tech Student.\n")
    f.write("I aspire to be a Data Scientist!\n")

f = open("tasks.txt", "r")
print(f.read())
f.close()