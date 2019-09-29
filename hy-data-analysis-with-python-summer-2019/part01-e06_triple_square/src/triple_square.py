#!/usr/bin/env python3


def triple(a):
    """returns a*3"""
    return a*3
def square(a):
    """returns a squared"""
    return a*a
def main():
    i = 1
    for i in range(1,11):
        trip = triple(i)
        sqr = square(i)
        if sqr <= trip:
            print("triple(%d)==%d square(%d)==%d" % (i, trip, i, sqr))
        else:
            break


if __name__ == "__main__":
    main()
