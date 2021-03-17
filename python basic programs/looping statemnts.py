

for i in "hello":
    print(i)

for i in "hello":
    print(i, end="")

for i in "hello":
    print(i, end=" ")

for i in "hello":
    print(i, end="/")

for i in range(1, 5):
    print(i)


#for i in range(1, 5, 2):
    print(list(range(1, 5, 2)))

for i in 'hello':
    if i == 'e':
       break
    print(i)
print('end')
    

for i in 'hello':
    if i == 'e':
       continue
    print(i)
print('end')


for letter in 'python':
    if letter == 'h':
        break
    print('current letter:',letter)

for letter in 'python':
    if letter == 'h':
        continue
    print('current letter:', letter)

genre = ['pop', 'rock', 'jazz']
# iterate over the list using index
for i in range(len(genre)):
    print("I like", genre[i])
