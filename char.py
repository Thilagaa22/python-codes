str = input("Enter a string:")
count = 0
for i in str:
  if i.isspace() != True:
    count = count + 1
print("Total number of char:",count)
