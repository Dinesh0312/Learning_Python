
#f = open("txt",'r')

#print(f.read())

import re

txt = ''' Vlan1 as id and status as down,  
-------------------------------------------------------------------------------
Interface Secondary VLAN(Type) Status Reason
-------------------------------------------------------------------------------
Vlan1 -- down Administratively down
Vlan10 -- down VLAN/BD is down
Vlan139 -- up --
Vlan1001 -- up --
Vlan1101 -- down VLAN/BD is down
Vlan1102 -- down VLAN/BD is down
Vlan1103 -- down VLAN/BD is down
Vlan1104 -- down VLAN/BD is down
Vlan1105 -- down VLAN/BD is down
Vlan1111 -- down VLAN/BD is down
Vlan1112 -- down VLAN/BD is down
Vlan1122 -- down VLAN/BD is down
Vlan1132 -- down VLAN/BD is down
Vlan1201 -- down VLAN/BD is down
Vlan1202 -- down VLAN/BD is down
Vlan1203 -- down VLAN/BD is down
Vlan1204 -- down VLAN/BD is down
Vlan1205 -- down VLAN/BD is down
Vlan1211 -- down VLAN/BD is down
Vlan1212 -- down VLAN/BD is down
Vlan1222 -- down VLAN/BD is down
Vlan1232 -- down VLAN/BD is down
Vlan2352 -- down VLAN/BD does not exist
Vlan2353 -- down VLAN/BD does not exist
Vlan3522 -- up --
Vlan3960 -- up --
Vlan3961 -- up --
Vlan3962 -- up --
Vlan3963 -- up --
Vlan3964 -- up --'''



vlan = re.findall(r'Vlan[0-9]{1,4}',txt)
print("Interface", vlan)

status = re.findall("(?<=--\s)(up|down)",txt)
print("Status", status)

dic = {}
for i in vlan:
    for j in status:
        dic[i] = j
z=0
for k,v in dic.items():
    dic[k] = {}
    dic[k] = status[z]
    z = z + 1


print("Dictionary is:",dic)