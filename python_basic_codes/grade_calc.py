s1=int(input("enter the mark for subject 1: "))
s2=int(input("enter the mark for subject 2: "))
s3=int(input("enter the mark for subject 3: "))
s4=int(input("enter the mark for subject 4: "))
s5=int(input("enter the mark for subject 5: "))
per=((s1+s2+s3+s4+s5)/500)*100
if per>=90:
  grade="A"
elif per>=75 and per<90:
  grade="B"
elif per>=60 and per<75:
  grade="C"
elif per>=40 and per<60:
  grade="D"
else:
  grade="Fail"
print("result",grade)
