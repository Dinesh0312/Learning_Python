#write a code to print out the value form 1 to 100 .skip the number which are divisible by 3 and 5


i = 1

while i<=100:
    if i%3 == 0 or i%5 == 0:
        i = i+1
    else:
        print(i)
        i = i+1

