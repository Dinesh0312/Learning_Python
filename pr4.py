#Find index for (/)  and print index no . eg o/p https://cisco.webex.com/meet/cisco123

s = "https://cisco.webex.com/meet/cisco123"

s1 = len(s)

for i in range(0,s1):
    if s[i] == "/":
        print(i)

