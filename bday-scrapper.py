import re
#data = ''
#with open("copy.html","r") as myfile:
#    data = myfile.read().replace('\n',' ')
data = open("copy.html","r")
output = open("output.in","w+")
for lines in data:
    a = re.findall(r"aria-label\=\"[a-zA-Z0-9]*\s[a-zA-Z0-9]*\s\([0-9]*\/[0-9]*\)",lines)
#python bday-scrapper.py < output.in


    