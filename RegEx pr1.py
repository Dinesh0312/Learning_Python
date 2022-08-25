import re

str = "Hello How are you"


pattern = re.compile('are')
search = pattern.search(str)

print(search)


print(re.search('are',str))


text = "its price is $15"

print(re.search('\$15',text))

matches = pattern.finditer("say hello hello")

for match in matches:
    print(match.span())