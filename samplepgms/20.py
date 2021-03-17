#print prime nos using Sieve of Eratosthenes
# n=int(input())
# count = 0
# for i in range(2, n//2, 1):
#     if n % i == 0:
#         count+=1
#     if count == 1:
#         print(" not prime")
#     break
#print prime nos in a range
start_range = int(input())
end_range = int(input())

for i in range(start_range, end_range+1, 1):
    if i > 1:
        for j in range(2, i, 1):
            if i % j == 0:
                break
        else:
            print(i, end=" ")


