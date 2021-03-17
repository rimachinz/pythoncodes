def FinallyTest():
    try:
        x=int(input('x'))
        y=int(input('y'))
        print(x/y)
        return 1
    except Exception as err:
        print(err)
        return 0
    finally:
        print('its finally clause')
result=FinallyTest()
print(result)
