year = int (input("Enter the year:"))
if((year % 4 == 0) or (year % 400 == 0)):
  print("%d is a Leap year",%year)
else:
  print("%d is not the leap year",%year)
