#use while loop, continue and break for below question .
#[1,4,7,19,36,105,8,223,445,75,499] print value if it is odd number and break if it is divisble by 25

list1 = [1, 4, 7, 19, 36, 105, 8, 223, 445, 75, 499]

i = 0

while i < len(list1):
    if list1[i] % 25 == 0:
        break
    if list1[i] % 2 != 0:
        print(list1[i])
    i = i + 1

list2 = [1, 4, 7, 19, 36, 105, 8, 223, 445, 75, 499]

for i in list2:
    if i%25 == 0:
        break
    if i%2 != 0:
        print(i)