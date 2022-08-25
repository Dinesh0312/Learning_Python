#count the even and odd number from the user input list

lst = []
num = int(input("How many number would you like to enter ? "))

for i in range(num):
    lst.append(int(input("Enter the number : ")))

print(lst)

def even_odd(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    return even,odd

even,odd = even_odd(lst)

print("Even_count {} \nOdd_count {}".format(even,odd))
