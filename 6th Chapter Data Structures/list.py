l = [1, 2, 3, 4, 5]

print(l.count(3))

l.append(6)
print(l)

l.insert(0, 0)
print(l)

l.remove(3)
print(l)

l.pop()
print(l)

l.pop(0)
print(l)

l[0] = 10
print(l)

l[1:3] = [20, 30]
print(l)

l[1:3] = []
print(l)

l.clear()
print(l)

l.extend([1, 3, 2])
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)