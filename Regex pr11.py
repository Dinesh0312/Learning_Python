#Let us consider a case where we want to replace all occurances of numbers with a - in the given text.

import re
txt = "100 cats, 23 dogs, 3 rabbits"

pattern = re.compile("\d+")
z = pattern.sub("-",txt)
print(z)

#Returns the substituted string as well as the no. of substitutions.

c = pattern.subn("-", txt)
print(c)