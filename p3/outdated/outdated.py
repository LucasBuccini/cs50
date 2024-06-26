lista=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date=input("Date :").title().strip()
        if "/" in date:
            x,y,z= date.split("/")
            if int(x)<=12 and int(y)<=31 and len(z)==4:
                print(f'{z}-{x:0>2}-{y:0>2}')
                break
        if "," in date:
            x,y,z= date.replace(",","").split()
            if x in lista and int(y)<=31:
                print(f'{z}-{lista.index(x)+1:0>2}-{y:0>2}')
                break
    except ValueError:
        pass
