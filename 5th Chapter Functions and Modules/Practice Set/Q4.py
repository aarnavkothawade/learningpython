def calculated_area(length, width = 10):
    area = length * width
    return area

length = int(input("Enter the length of the rectangle: "))
area = calculated_area(length)
print("The area of the rectangle is:", area)

area = calculated_area(length, 5)
print("The area of the rectangle with width 5 is:", area)