def check(str):
  p = set(str)
  s={'0','1'}
  if s == p or p == {'0'} or p =={'1'}:
    print("yes")
  else:
    print("No")
if __name__ == "__main__":
  str = int(input())
  check(string)
