with open("text.txt", "r") as f1:
    with open("new.txt", "a") as f2:
        f2.write(f1.read().upper())
    
