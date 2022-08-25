

import re

txt = '''
c:\Windows
c:\Python
c:\Windows\System32
'''


pattern = re.compile("c:\\\\Windows\\\\System32")
search = pattern.search(txt)
print(search)

p = re.compile(r"c:\\Windows\\System32")
z = p.search(txt)
print(z)


re.escape("c:\Windows\System32")

print(re.search(re.escape("c:\Windows\System32"),txt))