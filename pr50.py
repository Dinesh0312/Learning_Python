#print value if it is odd number and break if it is divisble by 25

l = [1,4,7,19,36,105,8,223,445,75,499]

odd_num = []
for i in l:
    if i%25 == 0:
        break
    if i%2 != 0:
        odd_num.append(i)
print(odd_num)
