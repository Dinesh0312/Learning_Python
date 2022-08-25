s1 = input("Enter your 1st String: \n")
s2 = input("Enter your 2nd String: \n")

length = len(s1)
length1 = len(s2)

mid_s1 = length//2
mid_s2 = length1//2

print(s1[0]+s2[0]+s1[mid_s1]+s2[mid_s2]+s1[length-1]+s2[length1-1])