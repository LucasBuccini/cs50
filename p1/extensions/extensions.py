code=input("File name: ").lower().strip().split(".")[-1]

if code=="jpeg" :
    print("image/jpeg")
elif code=="gif":
    print("image/gif")
elif code=="jpg":
    print("image/jpeg")
elif code=="png":
    print("image/png")
elif code=="pdf":
    print("application/pdf")
elif code=="txt":
    print("text/plain")
elif code=="zip":
    print("application/zip")
else:
    print("application/octet-stream")
