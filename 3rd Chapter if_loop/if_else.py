age = int(input("Enter your Age : "))

if(age < 18) : 
    v = False
    print("You are NOT Eligible to Vote")
else : 
    v = True
    print("You are Eligible to Vote")

if v :
    print("Make a Voter ID for you to be able to Vote in the next ELECTIONS")