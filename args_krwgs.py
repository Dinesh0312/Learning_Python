def function_name_print(normal,*args,**kwargs):
    '''Print king of the fruits'''
    print(normal)
    print("Print list of the other fruits\n")
    for items in args:
        print(items)
    print("Print the school data\n")
    for k,v in kwargs.items():
        print(k,v)
king = "Mango"
Fruits = ["apple","orange","pineapple","lichi"]
School = {'Rohan':'Topper','Siya':'Monitor','Bunty':'Cordinator'}

print(function_name_print.__doc__)
function_name_print(king,*Fruits,**School)

