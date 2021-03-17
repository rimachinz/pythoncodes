#exception with else
try:
 a=int(input('a='))
 b=int(input('b='))
 print("a/b=",a/b)
except Exception as e:
    print('something went wrong')
    print(e)
else:
    print('no exception caught')
