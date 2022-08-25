
# f = open('MyData','r')
# # print(f.read())
# # print(f.readline(4),end="")
# f1 = open('abc','a')
# # f1.write("Something")
# # f1.write("People")
# # f1.write('Mobile')


file = open("mydata",'r')

f1 = open('abc','w')

for data in file:
    f1.write(data)
