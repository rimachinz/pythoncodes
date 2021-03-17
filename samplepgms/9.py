#input 3 digit nos and print all possible combination
a = int(input())
b = int(input())
c = int(input())
x = [a, b, c]
y = [a, b, c]
z = [a, b, c]
print(x)
v= [(i*100+j*10+k) for i in x for j in y for k in z]
print(v)
