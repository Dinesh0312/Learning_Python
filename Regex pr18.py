#Look ahead
#Let's check out an example to understand the concept. Let's assume that we want to find a match for love in the given text only if it is followed by regex.

import re

txt = "i love python, i love regex"

pattern = re.compile('love regex')
match = pattern.search(txt)
print(match.span())
print(match)

find = pattern.findall(txt)
print(find)

pattern = re.compile("love(?=\sregex)")
match = pattern.search(txt)
print(match.span())
print(match)

find = pattern.findall(txt)
print(find)

#Let us check out another example to find all words in given text which are followed by . or ,.

txt = "My favorite colors are red, green, and blue."
pattern = re.compile("\w+(?=,|\.)")
print(pattern.findall(txt))

#Let's assume that we want to find a match for love in the given text only if it is NOT followed by regex

txt = "i love python, i love regex"
pattern = re.compile("love(?!\sregex)")

find = pattern.findall(txt)
print(find)



