a=[]
num = int(input("How many numbers in sort:"))
for i in range(num):
  nums=int(input("enter a value in sort "))
  a.append(nums)
b=sorted(a)
print(b)
c=int(input("enter a vaue:"))
for i range(len(b)):
  if b[i]>c:
    index = i
    break d = b[:i]+[c]+b[i:]
    print(d)
