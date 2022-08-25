import re

txt = """
the most common conjunctions are and, or and but.
"""

pattern = re.compile("and|or|the")
find = pattern.findall(txt)
print(find)



str = """
What is your name?
Who is that guy?
"""

p = re.compile("What|Who is")
f = p.findall(str)
print(f)

pattern = re.compile("(What|Who) is")
find = pattern.findall(str)
print(find)