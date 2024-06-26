from datetime import date
import inflect
import sys
p = inflect.engine()

def main():
    try:
        birth=input("Date of birth: ")
        diff=date.today()-date.fromisoformat(birth)
        print(f"{diff_to_min(diff.days)} minutes")
    except ValueError:
        sys.exit(1)
def diff_to_min(days):
    min=days*1440
    return p.number_to_words(min, andword="").capitalize()

if __name__ == "__main__":
    main()
