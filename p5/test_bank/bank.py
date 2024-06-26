def main():
    greeting=input("Gretting: ").lower().strip().split(",")[0]
    value(greeting)
    print(f'${value(greeting)}')
def value(gret):
    if gret[:5]=="hello":
        return 0
    elif (gret[0])=="h":
        return 20
    else:
        return 100
if __name__ == "__main__":
    main()
