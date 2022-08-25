def reverse(str1):
    str2 = ""
    for i in str1:
        str2 = i + str2
    return str2


str1 = "python is learning"
obj = reverse(str1)

print(obj)

def reverse(str1):
    str1 = str1[::-1]
    print(str1)

print(reverse(str1))

def fun(dict1):
    print(f"Keys are : {dict1.keys()}, values are:{dict1.values()}")

dict1 = {'Ram': 289001,'Robert':287654}
print(fun(dict1))