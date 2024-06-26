x=input("Input: ")
y=["A","E","I","O","U","a","e","i","o","u"]
for i in range (len(y)):
    x=x.replace(y[i],"")
print(f"Output: {x}")

