s = [int(i) for i in input().split()]
a = s[0]
b = s[1]
c = s[2]
if a == 0:
    print ("Уравнение не является квадратным")
else:
    if (b*b - 4*a*c<0) :
        print("уравнение не имеет действительных решений")
    else:
        x1 = (-b + (b*b - 4*a*c)**0.5)/(2*a)
        x2 =(-b - (b*b - 4*a*c)**0.5)/(2*a)
        print(x1,x2)