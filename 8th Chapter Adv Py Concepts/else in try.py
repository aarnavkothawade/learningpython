try: 
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    c = a/b

except:
    print("An error occurred, You cannot divide by zero!")

else:
    print("The division is ", c)