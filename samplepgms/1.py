#calculate avg of nos in a list

print(l)

# using built in functions
# a=sum(l)
# b=len(l)
# avg=a/b
# print(avg)
#w/o built in functions
sum=0
count=0
for i in l:
    sum+=i
    count+=1
print(sum)
avg=sum/count
print(avg)
