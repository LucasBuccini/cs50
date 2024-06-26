import sys
import csv
from tabulate import tabulate
menu=[]
def count_sys():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    else:
        file_name=sys.argv[1]
        file_split=file_name.split(".")
        if file_split[1]=="csv":
            tabela=criar_tabela(file_name)
            print(tabulate(tabela, headers='firstrow', tablefmt="grid"))
        else:
            sys.exit('Not a CSV file')
def criar_tabela(file_name):
    try:
        with open(file_name) as file:
            reader=csv.reader(file)
            for row in reader:
                menu.append({'Pizza':row[0],'Small':row[1],'Large':row[2]})
            return menu
    except FileNotFoundError:
        sys.exit('File does not exist')
count_sys()

