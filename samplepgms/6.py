# take mark of 5 subjects and display grade
for i in range(5):
    marks = [int(i) for i in input().split()]
    for i in marks:
        if 0 < i <= 30:
            print(i, "E grade")
        elif 30 < i <= 45:
            print(i, "D grade")
        elif 45 < i <= 60:
            print(i, "C grade")
        elif 60 < i <= 80:
            print(i, "B grade")
        else :
            print(i, "A grade")
