def main():
    word=input()
    print(shorten(word))


def shorten(word):
    y=["A","E","I","O","U","a","e","i","o","u"]
    for i in range (len(y)):
        word=word.replace(y[i],"")
    return word
if __name__ == "__main__":
    main()
