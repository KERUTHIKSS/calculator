while True:
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
    choise = int(input("Enter The Choise : "))
    a = float(input("Enter The First Number : "))
    b = float(input("Enter The Second Number : "))
    if choise == 1:
        print(f"{a} + {b} = {a+b}")
    elif choise == 2:
        print(f"{a} - {b} =  {a-b}")
    elif choise == 3:
        print(f"{a} * {b} =  {a*b}")
    elif choise == 4:
        print(f"{a} / {b} =  {a/b}")
    elif choise == 5:
        print("Thank You For Using...")
        break
    else:
        print("Enter the valid choise...")