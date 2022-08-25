#From this o/p. for given host/port print input bps

str1 = '''host,port,input bps,output bps
switch01,te0/1,2378748485,8474857587
switch02,te0/2,2378748486,5474857187
switch03,te0/3,3378748485,9474857587
switch04,te0/4,4378748486,15474857187'''

str1 = str1.split('\n')
print(str1)
dic = {}
l1 = []

for i in str1[1:-1]:
    x = i.split(',')
    print(x[0],x[1],x[2])
    dic[x[1]] = x[2]
    l1.append(x[0])

final_dic = {}

for k,v in zip(l1,dic.items()):
    final_dic[k] = v
print(final_dic)












