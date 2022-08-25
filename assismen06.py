import re

#Extract the IP address

str = " ip address = 192.168.10.1"

pattern = re.compile(r"\d+\.\d+\.\d+\.\d+")
find = pattern.findall(str)
print(find)

#Extract the Mac address

str = " mac address = ab01.ef18.ij0A"
pattern = re.compile(r"\w+\.\w+\.\w+")
find = pattern.findall(str)
print(find)

#Extract the MTU

txt = '''show interfaces bundle.* Wed Jul 27 12:03:39.513 UTC Bundle-Ether100 is up, line protocol is up Interface state transitions: 1 Hardware is Aggregated Ethernet interface(s), address is 7cf8.8046.0e46 Description: EDC PE Crossconnect to ATLGA0001E-CS0101-PE001 bundle 100 Internet address is Unknown MTU 9216 bytes, BW 400000000 Kbit (Max: 400000000 Kbit) reliability 255/255, txload 0/255, rxload 0/255 Encapsulation ARPA, Full-duplex, 400000Mb/s loopback not set, Last link flapped 19w1d No. of members in this bundle: 4 HundredGigE0/1/0/32 Full-duplex 100000Mb/s Active HundredGigE0/1/0/33 Full-duplex 100000Mb/s Active HundredGigE0/1/0/34 Full-duplex 100000Mb/s Active HundredGigE0/1/0/35 Full-duplex 100000Mb/s Active'''

pattern = re.compile("\d+(?=\sbytes)")
find = pattern.findall(txt)
print(find)

pattern = re.compile("(?<=MTU\s)\d+")
find = pattern.findall(txt)
print(find)