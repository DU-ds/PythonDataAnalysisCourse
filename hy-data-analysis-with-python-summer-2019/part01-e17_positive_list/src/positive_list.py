#!/usr/bin/env python3

def positive_list(L):
    return list(filter(lambda x : x > 0, L))

def main():
    print(positive_list([1,-2,3,-4,5]))

if __name__ == "__main__":
    main()
