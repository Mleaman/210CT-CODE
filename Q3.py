def perfsquare(n):
  x=0
  y=0
  while y<=0 :
    if x*x<n:
      x=x+1
    elif x*x !=n:
      print (n, "is not a perfect square!!")
      return 0
    else:
      print (n, "Is a perfect square!")
      return 1
  
print (perfsquare(15))
    