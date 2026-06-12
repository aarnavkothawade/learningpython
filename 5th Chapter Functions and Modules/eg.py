def add(a, b, c = 12) :
    x = a + b + c
    return x

c = add(b = 10, a = 20, c = 4) # Here it is not allowed to change the value of c without its variable name in front of it

print(c)

print(add(10, 20))
