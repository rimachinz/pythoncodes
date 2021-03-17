# reverse string
# a=input('a=')
a='hello'
l=len(a)
# for i in a[::-1]:
#     print(i,end="")
# using function
# def reverse(string):
#     string = string[::-1]
#     return string
# print(reverse(a))

def reverse(string):
    string = "".join(reversed(string))
    return string
print(reverse(a))


