# find the second-largest number in the list below
list1 = [2, 4, 7, 3, 5]

# solve with sort method
list1.sort(reverse=True)
second_largest_number = list1[1]
print("Second largest number:", second_largest_number)

list2 = sorted(list1)[-2]
print("Second largest number:", list2)

# solve with loop
first_largest = second_largest = float('-inf')

for num in list1:
    if num > first_largest:
        second_largest = first_largest
        first_largest = num
    elif num > second_largest and num != first_largest:
        second_largest = num

print("Second largest number:", second_largest)
