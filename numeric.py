s = input("Enter a values:")
d=l=0
for c in s:
  if c.isdigit():
    d = d+1
  else:
    pass
print("digits",d)
