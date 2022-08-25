import re

pattern = re.compile("Hello",re.UNICODE)
print(pattern)

pattern = re.compile('Hello',flags=re.IGNORECASE)

print(pattern)

str = "hello world"
z = re.compile("hello")
match = z.match(str)
print(match)

str = "hello world"
z = re.compile("world")
x = re.search(str,'world')
print(x)

string = "I love my india"
pattern = re.search(r'love',string)

print(pattern)



txt = '''
file1.xml
file1.txt
file2.txt
file15.xml
file5.docx
file60.txt
file5.txt
'''

pattern = re.compile('file\d+\.txt')
find = pattern.findall(txt)

print(find)
