#run the code and break if no exception
while True:
 try:
  a=int(input('a='))
  b=int(input('b='))
  print("a/b=",a/b)
  break
 except Exception as e:
    print('something went wrong')
    print(e)
