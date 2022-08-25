#Write a program to find key value pair when user given key in nested dictionary

dic1 = {'dictA':{'key_1':'value_1'},'dictB':{'Key_2':'value_2'},'dictC':{'Key_3':'value_3'}}

n = input("Enter the key : ")

for k,v in dic1.items():
    if n in v:
        print(v)