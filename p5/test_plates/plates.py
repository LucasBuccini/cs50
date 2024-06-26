def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 6>=len(s) and 2<=(len(s)) and s[0:2].isalpha() and s.isalnum():
        if s.isalpha():
            return True
        for x in s:
            if x.isdigit():
                position=s.index(x)

                if s[position: ].isdigit() and int(x)!=0:
                    return True
                else:
                    return False

    else:
        return False
main()
