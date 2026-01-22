# factorial
def fact():
  n=int(input("Enter number to find factorial: "))
  fact=1 #  1*2*3*4*5
  for i in range(1,n+1):  #5
    fact=fact*i   #24*5
  print(f"factorial of {n}:{fact}")
fact()


