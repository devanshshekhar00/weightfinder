print("welcome to the weight checker\n")

inp1 = input("Enter the first 2 letters of the planet you wish to check you'r weight in\n")


def weight(a):
    if a == "ju":
        var1 = float(input("ENTER WEIGHT\n"))
        woju = var1*2.4
        print("you'r wieght on jupiter is " + str(woju))
    elif a == "Ma":
        var2 = float(input("ENTER WEIGHT\n"))
        woma = var2*0.38
        print("you'r weight on mars is " + str(woma))
    elif a == "ur":
        var3 = float(input("ENTER WEIGHT\n"))
        wour = var3*0.886
        print("You'r weight on uranus is " + str(wour))
    elif a == "ne":
        var4 = float(input("ENTER WEIGHT\n"))
        wone = var4*0.11366
        print("You'r weight on neptune " + str(wone))
    elif a == "sa":
        var5 = float(input("ENTER WEIGHT\n"))
        wosa = var5*1.08
        print("You'r weight on saturn" + str(wosa))
    elif a == "me":
        var6 = float(input("ENTER WEIGHT\n"))
        wome = var6*3.7
        print("You'r weight on mercury " + str(wome))
    elif a == "ve":
        var7 = float(input("ENTER WEIGHT\n"))
        wove = var7*0.9
        print("You'r weight on venus is " + str(wove))
    else:
        print("ENTER A VALID INPUT")










weight(inp1)


