#Change string to dictionary with key as Name and value as age. Create new dic in ascending order on basis of age

str="anupam is 34 , Pavani is 30 , Mohan is 18 , Ramesh is 33 and Guru is 31"

str = str.split()

for i in str:
    if i == 'is' or i == ',' or i == 'and':
        str.remove(i)
print(str)

dict = {}

for i in range(0,len(str),2):
    dict[str[i]] = int(str[i+1])
print(dict)

short_dict ={}

for i in sorted(dict,key=dict.get):
    short_dict[i] = dict[i]
print(short_dict)

