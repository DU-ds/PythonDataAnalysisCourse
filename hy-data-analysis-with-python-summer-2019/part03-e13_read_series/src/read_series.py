#!/usr/bin/env python3
import pandas as pd

def read_series():
    index_list = []
    value_list = []
    while True:
        line = input()
        if line == "":
            break
        split_line = line.split()
        if len(split_line) == 2:
            index_list.append(split_line[0])
            value_list.append(split_line[1])
        else:
            raise ValueError("Malformed line: " + line + "\n")
    return pd.Series(value_list, index = index_list)

def main():
    s = read_series()
    print("Inputs: ", s)

if __name__ == "__main__":
    main()
