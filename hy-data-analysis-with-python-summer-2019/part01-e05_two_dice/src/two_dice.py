#!/usr/bin/env python3

def main():
    for i in range(1,7):
        for h in range(1,7):
            if i + h == 5:
                print("(" + str(i) + "," + str(h) + ")")


if __name__ == "__main__":
    main()
