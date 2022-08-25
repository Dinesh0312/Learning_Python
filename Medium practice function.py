#Find the longest word in the given list

def longest(lst):
    word = max(lst,key=len)
    return word

lst = ['Apple','Banana','Lichi','Pineapple','Watermellon']

result = longest(lst)
print(f"Longest word is {result} \nLength of the word is {len(result)}")

#find the prime number in the given list

def prime(list1):
    for i in list1:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(f"prime number {i}" )

list1 = [2,4,7,9,11,6]
prime(list1)


#Reverse the given string

def reverse(lst1):
    return lst1[::-1]

lst1 = "Apple is red"
result = reverse(lst1)
print(result)

#find the factorial

def fac(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f
x = int(input("Enter the number : "))

result = fac(x)
print(result)

#factorinal with recursion
def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)
n= int(input("Enter the number : \n"))
result = fact(n)
print(result)

#recursive function to calculate the sum of 'n' numbers
def sum(n):
    while n:
        s = n + sum(n-1) # 10 + 9 + 8 + 7 + 6.....1
        return s
    else:
        return 0
num = int(input("Enter your number: \n"))
result = sum(num)
print(result)