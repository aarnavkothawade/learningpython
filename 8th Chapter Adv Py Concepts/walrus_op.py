def v_s_f():
    print("Something..")
    print("Something..")
    print("Something..")
    print("Something..")
    return 11

if (a := v_s_f()) > 10:
    print(a)

else :
    print("Not greater than 10")





#Creating a loop which will halt whenever user enters a certain value

while (data := input("Enter: ")):
    print(data)
    if data == 'q':
        break

    ##Can be useful for passwords