#Write a Python function to find the Max of three numbers.

def max():
    if num1>num2 and num1>num3:
        return num1
    elif num2>num3 and num2>num1:
        return num2
    else:
        return num3


num1 = int(input("Enter the number_1 : "))
num2 = int(input("Enter the number_2 : "))
num3 = int(input("Enter the number_3 : "))

result = max()

print("Max of three number is " + str(result))
