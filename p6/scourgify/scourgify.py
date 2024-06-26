import sys
import csv

def main():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:]!='.csv':
            sys.exit("Not a CSV file")
        else:
            clean(sys.argv[1],sys.argv[2])
def clean(x,y):
    try:
        with open(x) as file:
            reader=csv.DictReader(file)
            with open(y,'w') as file2:
                writer=csv.DictWriter(file2, fieldnames=['first','last','house'])
                writer.writeheader()
                for rows in reader:
                    last,first=rows['name'].split(', ')
                    house=rows['house']
                    writer.writerow({'first':first,'last':last,'house':house})

    except FileNotFoundError:
        sys.exit(f'Could not read {x}')

if __name__ == "__main__":
    main()
