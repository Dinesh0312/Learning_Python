import re

txt = """
Yesterday, I was driving my car without a driving licence. The traffic police stopped me and asked me for my 
license. I told them that I forgot my licence at home. 
"""

pattern = re.compile('licen[cs]e')
find_all = pattern.findall(txt)
print(find_all)

txt = """
The first season of Indian Premiere League (IPL) was played in 2008. 
The second season was played in 2009 in South Africa. 
Last season was played in 2018 and won by Chennai Super Kings (CSK).
CSK won the title in 2010 and 2011 as well.
Mumbai Indians (MI) has also won the title 3 times in 2013, 2015 and 2017.
"""

find = re.compile('[1-9][0-9][0-9][0-9]')
find_in = find.findall(txt)
print(find_in)

pattern = re.compile('[^aeiou]')
z = pattern.findall(txt)
print(z)
join = "".join(z)
print(join)


pattern = re.compile('[^\w\s]')
sp = pattern.findall((txt))
print(sp)