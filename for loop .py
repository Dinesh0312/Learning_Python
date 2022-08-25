num = int(input("Enter 1st number : "))
num1 = int(input("Enter 2nd number: "))

while num <= num1:
    for i in range(1, num):
        if i * i == num:
            print(num, end=" ")
    num = num + 1
print("Perfect sqr between two number ", end=" ")
