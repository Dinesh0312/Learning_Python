#Search the string to see if it starts with "The" and ends with "Spain":
import re

txt = "The rain in Spain"

pattern = re.compile(r"^The.*Spain$")
find = pattern.findall(txt)

if find:
  print("YES! We have a match!")
else:
  print("No match")
