#Let us try to split a string to get individual lines in it.

import re

txt = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""

pattern = re.compile("\n")
split = pattern.split(txt)
print(split)

#Let us try one more example in which we want to get all the words in the given text.

pattern = re.compile("\W")
z = pattern.split(txt)
k = list(filter(lambda x: x!="",z))
print(k)

#What is we want only first 3 words? We need to split only 3 times in this case, which can be done by setting the value of maxsplit as 3.

c = pattern.split(txt, maxsplit=3)

print(c)

