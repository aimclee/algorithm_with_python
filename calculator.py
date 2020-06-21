def calculator():
    while True:
        operation = int(input(
            "Please select operation \n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide \n\n Select operation from 1, 2, 3, 4: "))

        if operation == 1:
            print("You chose add cal")

            def add(x, y):
                return x+y
            firstNum = int(input("Please enter the fist number: "))
            secondNum = int(input("Please enter the second number: "))
            result = add(firstNum, secondNum)
            print('The result is %f' % result)

        elif operation == 2:
            print("You chose subtraction cal")

            def subtraction(x, y):
                return x-y
            firstNum = int(input("Please enter the fist number: "))
            secondNum = int(input("Please enter the second number: "))
            result = subtraction(firstNum, secondNum)
            print('The result is %f' % result)

        elif operation == 3:
            print('You chose multiplicaion cal')

            def multiply(x, y):
                return x * y
            firstNum = int(input("Please enter the fist number: "))
            secondNum = int(input("Please enter the second number: "))
            result = multiply(firstNum, secondNum)
            print('The result is %f' % result)

        elif operation == 4:
            print("You chose division cal")

            def division(x, y):
                return x / y
            firstNum = int(input("Please enter the fist number: "))
            secondNum = int(input("Please enter the second number: "))
            result = division(firstNum, secondNum)
            print('The result is %f' % result)

        else:
            print("You typed wrong number! Please choose the number from 1 to 4.")


calculator()