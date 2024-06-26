import sys
def count_sys():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    else:
        file_name=sys.argv[1]
        file_split=file_name.split(".")
        if file_split[1]=="py":
            line_count=count_line(file_name)
            print(line_count)
        else:
            sys.exit("Not a Python file")
def count_line(file_name):
    try:
        with open(file_name,"r") as file:
            linhas=file.read().splitlines()
            count=0
            for line in linhas:
                if not line.lstrip().startswith("#") and line.lstrip()!="":
                    count+=1
            return count
    except:
        sys.exit('File does not exist')
count_sys()
