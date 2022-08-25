
#Greedy Behaviour
import re

txt = """<html><head><title>Title</title>"""

pattern = re.findall(r"<.*>",txt)
print(pattern)

#Non-Greedy behaviour

txt = """<html><head><title>Title</title>"""

pattern = re.findall(r"<.*?>",txt)
print(pattern)