def  calculator():
    print("Welcome!")
    print("To start press:")
    print("1. Multiplication")
    print("2. Division")
    print("3. Addition")
    print("4. Subtraction")

    choice = input("Enter the corresponding number for your desired choice (1,2,3,4): ")

    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    if choice == "1":
        print(f"The result of {num1}*{num2} is {num1 * num2}")
    elif choice == "2":
        if num2 != 0:
            print(f"The result of {num1}/{num2} is {num1 / num2}")
        else:
            print("You can't divide by zero.")
    elif choice == "3":
            print(f"The result of {num1} + {num2} is {num1 + num2}")
    elif choice == "4":
        print(f"The result of {num1} - {num2} is {num1 - num2}")
    else:
        print("Invalid choice.")


calculator()