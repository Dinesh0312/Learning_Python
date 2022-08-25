#Write a Python function that takes a number as a parameter and check the number is prime or not


def prime(n):
    for i in range(2,n):
        if n%i == 0:
            print("Not prime")
            break
    else:
        print("prime")

n = int(input("Enter the number : "))
prime(n)