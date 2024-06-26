def main():
    num=input("Fraction: ")
    percent=convert(num)
    print(gauge(percent))
def convert(fraction):
    while True:
        y,z=fraction.split("/")
        try:
            fraction=(int(y)/int(z))*100
            if int(y)>int(z):
                fraction=input("Fraction: ")
                pass
            else:
                return fraction
        except (ValueError,ZeroDivisionError):
            pass


def gauge(percentage):
    if percentage>=99 and percentage<=100:
        return "F"

    elif percentage<=1:
        return "E"
    else:
        percentage=("{0:.0f}".format(round(percentage,0))+"%")
        return percentage

if __name__ == "__main__":
    main()
