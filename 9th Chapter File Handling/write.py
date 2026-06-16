f = open("text.txt", "w")

f.write("Hello! I am writing into the file.")

f.close()

f = open("text.txt", "r")

print(f.read())

f.close()