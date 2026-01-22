num=int(input("Enter a number: "))
rev=0
while num!=0:
  rem=num%10  #it gives the last digit i.e., 4 in first iteration
  rev=rev*10+rem   #rev*10=> ex. 0*10=0 and 4*10=40
  num=num//10      #it removes only last number
print("Reverse: ",rev)