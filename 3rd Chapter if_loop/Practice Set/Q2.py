age = int(input("Enter your age: "))

if age < 18:
    print("You are NOT eligible to vote.")
elif age >= 18 and age <= 100:
    print("You are eligible to vote.")
else:
    print("Invalid age entered.")