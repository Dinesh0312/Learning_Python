#Replace 'a' in a string with 't'

str1 ="axbctghn"

str1 = list(str1)
print(str1)

for i in str1:
    if i == 'a':
        ind = str1.index(i)
        str1[ind] = 't'
str1 = "".join(str1)

print(str1)



