def prime(n):
  y=2
  while True:
    for i in range(y,n):
      if n % i == 0:
        print (n, "is not prime")
        return True
      else:
        print (n, "is prime")
        return False
  
prime(9)