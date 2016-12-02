def voweldestroyer(string):
  vowels= ["a", "e", "i", "o", "u"]
  answer =""
  for x in string:
    if x not in vowels:
      answer=answer+x
  return answer
  
print (voweldestroyer("Thanks For the Memories"))