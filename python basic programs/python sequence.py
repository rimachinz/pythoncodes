    


s = '{}{}{}'.format('a','b','c')
print(s)
s = '{} {} {} '.format('a', 'b', 'c')
print(s)
s = '{}/{}/{}'.format('a', 'b', 'c')
print(s)
s = '{2}{0}{1}'.format('a', 'b', 'c')
print(s)
x ='ipsr'
y='solutions'
z ='ltd'
s='{}{}{}'.format(x, y, z)
print(s)
binary ="{0:b}".format(8)
print (binary)
dec = 344

print("The decimal value of", dec,"is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")
hexa = "{0:x}".format(15)
print(hexa)
octa = "{0:o}".format(8)
print(octa)



app ="{0:.4f}".format(1.42855714)
print(app)
x ='ipsr'
y ='solutions'
z ='ltd'

align = '{:<15}/{:^15}/{:>15}'.format(x,y,z)
print(align)
a=['eng', 'maths']
a.append('bio')
print(a)
a.insert(2, 'geo')
print(a)
b=['mal', 'hindi']
print(min(b))

a.extend(b)
print(a)
b.extend(a)
print(b)
a=[1, 2, 3, 4, 5]
print(sum(a))
a=[1, 2, 3, 4, 5, 6, 2, 2]
print(a.count(2))
print(len(a))
print(a.index(3))
print(max(a))
print(min(a))
print(b)
print(max(b))
a = [1, 2, 3, 4, 5, 6, 5, 5]

print(a.index(2))
print(sorted(a))
a.sort(reverse=True)
print(a)
a.sort(reverse=False)
print(a)
print(a.pop())

y = a.remove(2)
print(a)
del(a[3])
print(a)
