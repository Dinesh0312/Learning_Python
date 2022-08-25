add = "Room 23, Kaddubishnahalli , Palm resort, HD/No 83400. Pin Code: 530068 station"
add = add.split()

for i in add:
    length = len(i)
    if length == 6 and i.isdigit():
        print("Pincode", i)



