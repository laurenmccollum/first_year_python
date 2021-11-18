#tells you if the entered number is prime or not
x = int(input("Enter x"))

i=x-1
while i>0:
  if i==x:
    i+=-1
  elif i==1:
    print("Prime")
    break
  elif x%i==0:
    print("Not prime")
    break
  else:
    i+=-1
