def main():
    time=input("What time is it? ")
    x=convert(time)
    if x>=7 and x<=8:
        print("breakfast time")
    elif x>=12 and x<=13:
        print("lunch time")
    elif x>=18 and x<=19:
        print("dinner time")

def convert(time):
    if "a.m." in time or "p.m." in time:
        hours_minutes, pm_am= time.split(" ")
        hours, minutes,= hours_minutes.split(":")
        if pm_am=="p.m." and int(hours)!=12:
            hours=int(hours)+12
    else:
        hours, minutes,= time.split(":")
    hours=int(hours)+(float(minutes)/60)
    return hours

if __name__ == "__main__":
    main()
