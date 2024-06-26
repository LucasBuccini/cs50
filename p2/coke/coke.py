x=50
while x>0:
    print(f"Amount Due: {x}")
    n=int(input("Insert Coin: "))
    if n==25:
        x-=n
    if n==10:
        x-=n
    if n==5:
        x-=n
    else:
        x=x
if x<=0:
    x=-x
    print(f"Change Owed: {x}")



