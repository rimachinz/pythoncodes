#run the code in try & else
while True:
  try:
   a=int(input('a='))
   b=int(input('b='))
   print("a/b=",a/b)
  except Exception as e:
     print('something went wrong')
     print(e)
else:
    print('remaining code executed')
    
