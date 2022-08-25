#Consider a scenario where you want to find all occurances of and, or and the in the given text.

import re

txt = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. 
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""
print(re.findall("\\b(and|or|the)\\b",txt))

#Consider a scenario where we want to find all the lines in the given text which start with the pattern Name:.

txt = """
Name:
Age: 0
Roll No.: 15
Grade: S

Name: Ravi
Age: -1
Roll No.: 123 Name: ABC
Grade: K

Name: Ram
Age: N/A
Roll No.: 1
Grade: G
"""

print(re.findall("^Name: \w+",txt,flags=re.M))

#Find all the sentences which do not end with a full stop (.) in the given text.

txt = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s!
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages
More recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

print(re.findall("^.+[^\.]$",txt,flags=re.M))

