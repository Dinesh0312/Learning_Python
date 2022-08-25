
def sum(x,y):
    try:
        print("The sum of both the number is : ", int(x)+int(y))
    except Exception as e:
        print("Sorry! You can not add int and str ", e)
    finally:
        print("This is important to print")

num1 = input("Enter the num1 : \n")
num2 = input("Enter the num2 : \n")

sum(num1,num2)

