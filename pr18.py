#1.Find the length of each element of the list.
#2.Find the longest from the given list

#l= ['apple','banana','orange','pineapple']

#for in l:
   #print(i,":",len(i))


list=['apple','banana','orange','pineapple']

maxlen = len(list[0])
max = list[0]
for i in list:
    if(len(i) > maxlen):
        maxlen = len(i)
        max = i
print(max,maxlen)