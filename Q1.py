from random import randint
num = [1,4,3,9,2,5,2,6]

def shufflelist(x):
   if len(x) > 1:
      i = len(x) -1
      while i > 0:
          y = randint(0, i)
          x[i], x[y] = x[y], x[i]
          i -= 1
      return x

print (shufflelist(num))

