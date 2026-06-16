with open('text.txt', 'r') as file:
    content = file.read()
    print(content)


print("Write mode: ")
with open('text.txt', 'w') as file:
    file.write('This is a new line of text.\n')
    file.write('This will overwrite the previous content.\n')

with open('text.txt', 'r') as file:
    content = file.read()
    print(content)
