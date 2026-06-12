# String Formatting

from tempfile import template


s = "Hello, {} how are you? We are happy to provide you a scholarship of {}$"

a = "Aarnav"
a1 = 1000
b = "Sumay"
b1 = 900
c = "Sachin"
c1 = 800

print(s.format(a, a1))
print(s.format(b, b1))
print(s.format(c, c1))

# NEED TO CHECK THIS LATER ONLINE
# s1 = template.format(a, a1)
# print(s1)

#f-string
print(f"Hello, {a} how are you? We are happy to provide you a scholarship of {a1}$")
print(f"Hello, {b} how are you? We are happy to provide you a scholarship of {b1}$")
print(f"Hello, {c} how are you? We are happy to provide you a scholarship of {c1}$")   
