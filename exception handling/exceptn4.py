#no of except: reduced and err is printed
try:
 a=int(input('a='))
 b=int(input('b='))
 print("a/b=",a/b)

except (ValueError,ZeroDivisionError) as err :
    print('input a digit or no num is divisible by zero')
    print(err)
