str= "jhon is 34 , Mojo is 30 , Tom is 18 , Rambo is 33 and Jhonny is 31"

str = str.split()

for i in str:
    if i == 'is' or i == "," or i == 'and':
        str.remove(i)

print(str)

dict1 = {}

for i in range(0,len(str),2):
    dict1[str[i]] = int(str[i+1])
print(dict1)



sorted_dic = {}
for i in sorted(dict1,key=dict1.get):
    sorted_dic[i] = dict1[i]
print(sorted_dic)
