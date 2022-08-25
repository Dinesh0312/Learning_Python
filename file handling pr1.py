#file handling

f = open('file.txt','r')

print(f.read())

f.close()


f = open('file.txt','w')

f.write("A twink twink poem\n ")

f.close()

f = open('file.txt','a')
f.write('''
Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.
''')

f.close()





file = open('file.txt','r+')


f = open("doc.txt",'w')

for data in file:
    f.write(data)




