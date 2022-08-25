import re
str= '''PE1_ESP200x#sh ip int br
Interface              IP-Address      OK? Method Status                Protocol
Fo0/0/0                unassigned      YES unset  up                    up      
Fo0/0/1                unassigned      YES unset  up                    up      
Te0/1/0                99.1.1.1        YES NVRAM  up                    up      
Te0/1/1                unassigned      YES unset  down                  down    
Te0/1/2                77.1.1.1        YES NVRAM  up                    up      
Te0/1/3                unassigned      YES unset  down                  down 
Te1/1/1.4001           102.1.1.2       YES NVRAM  up                    up      
Te1/1/1.4002           102.1.2.2       YES NVRAM  up                    up      
Te1/1/2                65.0.0.2        YES NVRAM  up                    up 
 '''
pattern = re.compile(r"\w+\d/\d/\d")
interface = pattern.findall(str)
print(interface)

pattern = re.compile(r"(up|down)..........")
Status = pattern.findall(str)
print(Status)

output = {}

for i in interface:
    for j in Status:
        output[i] = j
print(output)