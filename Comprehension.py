
#list Comprehension

#printa list divisible by 3

#ls = []
#for i in range(100):
#    if i%3 == 0:
#        ls.append(i)
#print(ls)


ls = [i for i in range(100) if i%3==0]
print(ls)


#dict comprehension

dict1 = {i:f"item{i}" for i in range(5)}
print(dict1)
dict2 = {value:key for key,value in dict1.items()}
print(dict2)

#set comprehension

dresses = {dress for dress in ['dress1','dress2','dress1','dress2','dress3']}
print(dresses)

#genrator/itrator comprehension

evens = (i for i in range(100) if i%2 == 0)
print(evens)

print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(next(evens))
print(next(evens))