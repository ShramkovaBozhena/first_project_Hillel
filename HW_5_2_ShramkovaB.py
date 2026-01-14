def calculator():
    first_numb = float(input("Enter the first number: "))
    second_numb = float(input("Enter the second number: "))
    arithmet_operat = input("Enter operation of arithmetic (+, -, *, /): ")
    if arithmet_operat == '+':
        result = first_numb + second_numb
        print(result)
    elif arithmet_operat == '-':
        result = first_numb - second_numb
        print(result)
    elif arithmet_operat == '*':
        result = first_numb * second_numb
        print(result)
    elif arithmet_operat == '/' and second_numb    == 0:
        print("You can't divide by zero :)")
    elif arithmet_operat == '/':
        result = first_numb / second_numb
        print(result)
    else:
        print("Check the entered data")

calculator()
while True:
    print("Do you still want to use the calculator?")
    answer = input("Your answer: ")
    if (answer == "yes") or (answer == "y"):
        calculator()
    else:
        break