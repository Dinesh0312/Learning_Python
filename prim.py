range1 = int(input("Enter number1 :  "))
range2 = int(input("Enter number2 :  "))

for i in range(range1,range2):
    if i%2 == 0:
        print("prime " + str(i))
    else:
        print("odd " + str(i))
