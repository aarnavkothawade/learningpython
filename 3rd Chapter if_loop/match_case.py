
while True :
    a = int(input("Enter 1. for susu\n" 
    "2. for haggu\n" 
    "3. for exit\n"))

    if a == 3 :
        break
    
    match a :
        case 1:
            print("Susu ke liye 5₹")
        case 2:
            print("Haggu ke liye 10₹")
        case _:
            print("Ulti karna not allowed")