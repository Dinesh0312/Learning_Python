"""Symbol 	Name 	Quantification of previous character
 ? 	  Question Mark 	Optional (0 or 1 repetitions)
 * 	  Asterisk 	Zero or more times
 + 	  Plus Sign 	One or more times
{n,m} Curly Braces 	Between n and m times"""


import re
#Find all the matches for dog and dogs in the given text
txt = """
I have 2 dogs. One dog is 1 year old and other one is 2 years old. Both dogs are very cute! 
"""

pattern = re.compile("dogs?")
z = pattern.findall(txt)
print(z)
#Find all filenames starting with file and ending with .txt in the given text.
txt = """
file1.txt
file_one.txt
file.txt
fil.txt
file.xml
file-1.txt
"""

pattern = re.compile("file[\w-]*\.txt")
z = pattern.findall(txt)
print(z)

#Find all filenames starting with file followed by 1 or more digits and ending with .txt in the given text.



txt = """
file1.txt
file_one.txt
file09.txt
fil.txt
file23.xml
file.txt
"""

pattern = re.compile("file\d+\.txt")
z = pattern.findall(txt)
print(z)

#Find years in the given text.



txt = """
The first season of Indian Premiere League (IPL) was played in 2008. 
The second season was played in 2009 in South Africa. 
Last season was played in 2018 and won by Chennai Super Kings (CSK).
CSK won the title in 2010 and 2011 as well.
Mumbai Indians (MI) has also won the title 3 times in 2013, 2015 and 2017.
"""



pattern = re.compile("\d{4}")
z = pattern.findall(txt)
print(z)

#In the given text, filter out all 4 or more digit numbers.


txt = """
123143
432
5657
4435
54
65111
"""

pattern = re.compile("\d{4,}")
print(re.findall(pattern, txt))

#Write a pattern to validate telephone numbers.
#Telephone numbers can be of the form: 555-555-5555, 555 555 5555, 5555555555



txt = """
555-555-5555
555 555 5555
5555555555
"""

pattern = re.compile("\d{3}[-\s]?\d{3}[-\s]?\d{4}")
print(re.findall(pattern, txt))
