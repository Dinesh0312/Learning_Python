n = input("Enter the string: ")

length = len(n)
m = length//2

if length>=3:
    print(n[m-1]+n[m]+n[m+1])
else:
    print("Worng output")

