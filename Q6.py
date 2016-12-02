def reverse(string):
  answer =""
  for x in string:
    answer=x+answer
  return answer
print (reverse("hello"))