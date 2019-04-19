n = int(input("Enter a number limit:"))
list= []
for i in input().split():
  list.append(int(i))
list.sort()
print(list[0], end='    ')
print(list[-1],end = '')
