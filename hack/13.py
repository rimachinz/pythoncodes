t = int(input())
if 1 <= t <= 100:



    def find_longest_common_subseq(str1, str2):
        count = 0
        for i in str1:
            if i in str2:
                print(i, end=",")
                count += 1
                str2 = str2.replace(i, "", 1)

        print(count)
        if count == 0:
            print('()')


    while t > 0:
        str1 = input()
        l1=len(str1)
        str2 = input()
        l2=len(str2)
        if 0 < l1 <= 10 and 0 < l2 <= 10:
            find_longest_common_subseq(str1, str2)
            t -= 1
        else:
            print("String Length Exceeded")
else:
    print("Limit Exceeded")