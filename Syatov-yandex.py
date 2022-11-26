a = int(input())
b = int(input())
a1 = 0
if a == 12 or a==6 and b != 0:
    print(str(a),str(60-b))
elif a == 12 or a==6 and b == 0:
        print(str(a),str(b))
elif b == 0 and a != 6 or a != 12:
    print(12-a,60-b)
else :
    print(12-a,60-b)
