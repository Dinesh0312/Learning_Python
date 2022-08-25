#Write a Python program to sort a list of dictionaries using Lambda

list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]


l=sorted(list,key = lambda x: x['color'])

print(l)