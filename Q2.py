def countzeros(n):
  a=0
  i=0
  while i<5:
    if n % 10 == 0:
      a += 1
      n = n/10
    else:
      i+=1
      return a
      
print (countzeros(500))