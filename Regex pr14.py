#Consider a scenario where we want to find all the duplicated words in the given text.

import re

txt = """
hello hello
how are you
bye bye
"""

pattern = re.compile(r"(\w+) \1")
find = pattern.findall(txt)
print(find)


#Consider a scenario where we want to find all dates with the format dd/mm/yyy and change them to yyyy-mm-dd format.



txt = """
today is 23/02/2019.
yesterday was 22/02/2019.
tomorrow is 24/02/2019.
"""

pattern = re.compile("(\d{2})\/(\d{2})\/(\d{4})")
find =pattern.findall(txt)
print(find)

newtxt = pattern.sub(r"\3-\2-\1",txt)

print(newtxt)
