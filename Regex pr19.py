#Let's check out an example to understand the concept. Let's assume that we want to find a match for regex in the given text only if it is succeeded by love or hate.

import re

txt = "love regex or hate regex, can't ignore regex"
pattern = re.compile("(?<=(love|hate)\s)regex")
match = pattern.search(txt)
print(match.span())

#aume that we want to find a match for regex in the given text if it is not followed by love or hate.

pattern = re.compile("(?<!(love|hate)\s)regex")
match = pattern.search(txt)
print(match.span())