list1 = ['potato','tomato','apple','kiwi','avocado','lichi','pea','pineapple']

maxlen = len(list1[0])
max = list1[0]

for i in list1:
    if len(i) > maxlen:
        maxlen = len(i)
        max = i
print(max)