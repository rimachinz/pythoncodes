while True:
  try:
    a=int(input('a='))
    b=int(input('b='))
    print(a/b)
    #break
#except (ZeroDivisionError,ValueError) as err:
    #print('no cant be divided by zero or invalid literal')
    #print(err)
  except Exception as e:
    print('something went wrong')
    print(e)
  else:
    print('code executed')
    break



