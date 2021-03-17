#error typed in more except:
try:
 a=int(input('a='))
 b=int(input('b='))
 print("a/b=",a/b)

except ValueError :
    print('input a digit')
except ZeroDivisionError :
        print('no num is divisible by zero')

