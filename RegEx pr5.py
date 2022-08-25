#find the pincode from the string

import re


add = "Room 23, Kaddubishnahalli , Palm resort, HD/No 83400. Pin Code: 530068 station"

pattern = re.compile('[1-9]\d{5}')

z = pattern.findall(add)

print(z)