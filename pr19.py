
animal = ["cat","dog","tiger","monkey","elephent"]

maxlen = len(animal[0]) #3
max = animal[0] #cat

for i in animal:
    if len(i) > maxlen:
        maxlen = len(i)
        max = i
print(max,maxlen)