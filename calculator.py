

while True:
    print("\n------ Calculator ------")
    print("1 - ADD")
    print("2 - SUB")
    print("3 - MUL")
    print("4 - DIV")
    print("5 - EXIT")

    try:
        option = int(input("Enter the option (1 to 5): "))

        if option == 5:
            print("Exiting the calculator. Goodbye!")
            break

        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))

        if option == 1:
            answer = num1 + num2
            print(f"Addition = {answer}")
        elif option == 2:
            answer = num1 - num2
            print(f"Subtraction = {answer}")
        elif option == 3:
            answer = num1 * num2
            print(f"Multiplication = {answer}")
        elif option == 4:
            if num2 != 0:
                answer = num1 / num2
                print(f"Division = {answer}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid option. Please choose between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
