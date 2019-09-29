#!/usr/bin/env python3

def reverse_dictionary(d):
    for key, value in d:
        for val in value:
            try:
                a = dikt[val]
                key = list(*a).append(key)
                dikt[val] = key
            except:
                dikt[val] = key
    return {}

def main():
    pass

if __name__ == "__main__":
    main()
