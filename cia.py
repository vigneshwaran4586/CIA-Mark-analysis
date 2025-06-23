#calculating the CIA marks
for i in range(1,5):
    if (i == 1):
        c = int(input("Enter your first internal mark out of 70 :"))
        d = float(c / 70) * 7.5
        print("Your internal first internal mark out of 70 is :", d)
    elif (i == 2):
        h = int(input("Enter your second internal mark out of 70 :"))
        n = float(h / 70) * 7.5
        print("Your second internal mark out of 70 is :", n)
    elif (i == 3):
        e = int(input("Enter your mark out of 100 :"))
        f = float(e / 100) * 10
        print("Your internal mark out of 100 is :", f)
    elif(i==4):
        j = d
        k = n
        l = f
        m = int(j + k + l)
        print("The total internal mark you scored is :", m,"out of 25")
