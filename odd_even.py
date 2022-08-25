# Python program to count Even
# and Odd numbers in a List

# Print the count of even and odd numbers of list

list1 = [10, 21, 4, 45, 66, 93, 1]

even_count, odd_count = 0,0

for num in list1:
    if num%2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even count: ", even_count)
print("Odd count: ", odd_count)

# print the even and odd number of the list

even = []
odd = []

for i in list1:
    if (i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)

print("Even List: ", even)
print("Odd List: ", odd)