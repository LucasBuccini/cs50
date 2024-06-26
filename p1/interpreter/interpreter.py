expression=input("Expression: ")
x, y, z = expression.split(" ")
x=float(x)
z=float(z)
if y=="/":
    expression=x/z
elif y=="*":
    expression=x*z
elif y=="-":
    expression=x-z
elif y=="+":
    expression=x+z
else:
    print("invalid")
print(expression)


