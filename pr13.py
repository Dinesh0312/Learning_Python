str = 'hello 12 hi 89. Howdy 34'

for i in str:
    if i == " ":
        str = str.replace(i,"")
print(str)

str = 'hello 12 hi 89. Howdy 34'
str = str.replace(' ','')
print(str)