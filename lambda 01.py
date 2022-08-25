#Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result


i = int(input("Enter the number : "))
def double(i):
    l = lambda x:x*2
    print(l(i))

double(i)

l = lambda x:x+15
print(l(i))


l1 = lambda x,y : x*y
print(l1(6,8))

