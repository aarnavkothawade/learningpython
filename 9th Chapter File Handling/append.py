f = open("text.txt", "a+")

f.write("\nAppending into the file.")

f.close()

f = open("text.txt", "r")

for line in f:
    print(line.strip())

f.close()