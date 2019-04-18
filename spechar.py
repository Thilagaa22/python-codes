import re
x = input("Enter a words:")
count = re.sub('[\w]+','',x)
print(len(count))
