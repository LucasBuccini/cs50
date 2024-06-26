lista={}
while True:
    try:
        item=input().upper()
        if item in lista:
            lista[item]+=1
        else:
            lista[item]=1

    except EOFError:
        for x in sorted(lista.keys()):
            print(lista[x], x)

        break


