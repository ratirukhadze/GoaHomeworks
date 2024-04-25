import re 

txt = "The rain in georgia"
txt = "The rain in guemilia"
x = re.search(r"\bg\w+", txt)

print(x.group())