s = "https://cisco.webex.com/meet/cisco123"

for i in range(0,len(s)):
    if s[i] == "/":
        print(i)
