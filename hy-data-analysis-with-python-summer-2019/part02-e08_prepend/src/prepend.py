#!/usr/bin/env python3

class Prepend(object):
    
    def __init__(self, s):
        self.start = s
    
    def write(self, s):
        print(self.start + s)

def main():
    prep = Prepend("Don't forget to ")
    prep.write("be awesome")

if __name__ == "__main__":
    main()
