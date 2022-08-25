str1 = 'jump zoo zoo jump Taxi Aeroplane Taxi zoo'
str2 = 'fly up till next universe'

# Create string with only unique words
# add 'saturn' at end of str1
# add 'jupiter' after 'jump' of str1
# delete 'aeroplane' of str1
# merge Str1 & str2 string with '_'
# split after merging the string

str1 = str1.split()

l1 = []

for i in str1:
    if i not in l1:
        l1.append(i)
print(l1)

str1.append("saturn")

print(str1)

for i in range(0,len(str1)):
      if str1[i]=="jump":
        str1.insert(i+1,"jupiter")

print(str1)

str1.remove("Aeroplane")

print(str1)

str1 = " ".join(str1)
print(str1)

str3 = str1+"_"+str2

print(str3)

str3 = str3.split()

print(str3)