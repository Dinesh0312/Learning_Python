#Consider a scenario where we want to extract the first name and last name of a person.

import re

txt = "Nikhil Kumar"

pattern = re.compile("(?P<first>\w+) (?P<last>\w+)")
match = pattern.match(txt)
print(match)

print(match.group('first'))
print(match.group('last'))

#Now consider the scenario where we want to swap first name and last name in above example.

print(pattern.sub("\g<last> \g<first>", txt))

#Consider a scenario where we want to check if a person has same first and last name.


txt = "Jhonson Jhonson"
pattern = re.compile("(?P<first>\w+) (?P=first)")

find = pattern.findall(txt)
print(find)

