lst = []
num = int (input("Enter how many number:"))
for n in range(num):
  number = int(input("enter numbers:"))
  lst.append(number)
  print("Maximum number amoung the numbers:",max(lst))
