#Let's check out an example to find all occurances of the and The in the given text.

import re

txt = """
The best thing about regex is that it makes the task of string manipulation so easy.
"""

print(re.findall("the",txt,flags=re.I))

#Let's check out an example to find all lines starting with A.

txt = """
A man was crossing the road.
Suddenly, a car passed before him in a very high speed.
He was terrified
And shocked.
"""
print(re.findall('^A.+',txt,flags=re.M))

#Let's consider an examle to match all the text after (and including) car.

txt = """
A man was crossing the road.
Suddenly, a car passed before him in a very high speed.
He was terrified
And shocked.
"""

print(re.findall("car.+",txt,flags=re.S))

#Let's consider an example where we try to work on hindi language.

txt = "मुझे किताबें पढ़ना बहुत पसंद है।"

print(re.findall("\w+",txt))

import regex

print(regex.findall("\w+",txt))

#Let us see an example below:
chars =  ''.join(chr(i) for i in range(256))
print(chars)


print(re.findall("\w+",chars,re.A))