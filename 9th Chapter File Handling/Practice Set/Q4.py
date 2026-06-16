f = open("tasks.txt", "a")

f.write("Task Completed!\n")

f.close()

f = open("tasks.txt", "r")
print(f.readlines())
f.close()