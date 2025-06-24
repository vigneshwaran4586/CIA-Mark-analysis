#calculating the CIA marks
c = int(input("Enter your first internal mark out of 70 :"))
if(c<=70):
    d = float((c / 70) * 7.5)
    print("Your internal first internal mark out of 70 is :", d)
else:
    print("You entered the incorrect match !")
h = int(input("Enter your second internal mark out of 70 :"))
if(h<=70):
    n = float((h / 70) * 7.5)
    print("Your second internal mark out of 70 is :", n)
else:
    print("You entered the incorrect match !")
e = int(input("Enter your mark out of 100 :"))
if(e<=100):
    f = int((e / 100) * 10)
    print("Your internal mark out of 100 is :", f)
    j = d
    k = n
    l = f
    m = int(j + k + l)
    print("The total internal mark you scored is :", m,"out of 25")
else:
    print("You entered the incorrect match !")
