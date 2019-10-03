#!/usr/bin/env python3

def extract_numbers(s):
    lst = s.split()
    lst2 = []
    for e in lst:
        try:
            e = int(e)
        except ValueError:
            try:
                e = float(e)
            except ValueError:
                pass #skip, not an int or float
            else:
                lst2.append(e)
        else:
            lst2.append(e)
        

    return lst2

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
