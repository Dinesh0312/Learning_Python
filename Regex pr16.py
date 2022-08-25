#Let's consider an example where we want to find the strings i love cats or i love dogs in the given text.

import re

txt = """
i love cats
i love dogs
"""

pattern = re.compile("i love (cats|dogs)")
print(pattern.findall(txt))

for match in pattern.finditer(txt):
    print("Complete regex match (default):", match.group(0))
    print("Match captured by 1st group:", match.group(1))


pattern = re.compile("i love (?:cats|dogs)")
print(pattern.findall(txt))

for match in pattern.finditer(txt):
    print("Complete regex match (default):",match.group(0))