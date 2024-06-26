while True:
    try:
        x=input("Fraction: ")
        y,z=x.split("/")
        fraction=(int(y)/int(z))*100
        if fraction>=99 and fraction<=100:
            print("F")
            break
        elif int(y)>int(z):
            pass
        elif fraction<=1:
            print("E")
            break
        else:
            print("{0:.0f}".format(round(fraction,0))+"%")
            break
    except (ValueError,ZeroDivisionError):
        pass
