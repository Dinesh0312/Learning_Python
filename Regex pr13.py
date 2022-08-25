#Grouping

#For example, (ab)+ will match one or more repetitions of ab.
import re
txt = "abbbbbabbbb"

print(re.findall("ab+",txt))
print(re.findall("(ab)+",txt))

#restrict alternation to part of the regex.

txt = """
my name is ram
my name is sam
"""

print(re.findall("my name is ram|sam",txt))
print(re.findall("my name is (ram|sam)",txt,))

#Consider an example where we want to parse a date and determine day, month and year.

txt = "12/02/2019"
pattern = re.compile("(\d{2})\/(\d{2})\/(\d{4})")
match = pattern.match(txt)
print(match)

print(match.group(1))
print(match.group(2))
print(match.group(3))

day, month, year = match.groups()

print(day, month, year)

#In the given text, find all the patterns with Name: <some-name> and extract <some-name>.



txt = """
Name: Nikhil
Age: 0
Roll No.: 15
Grade: S

Name: Ravi
Age: -1
Roll No.: 123
Grade: K

Name: Ram
Age: N/A
Roll No.: 1
Grade: G
"""

pattern = re.compile("Name: (.+)\n")
find = pattern.findall(txt)
print(find)

