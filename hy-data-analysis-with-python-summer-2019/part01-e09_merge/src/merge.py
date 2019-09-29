#!/usr/bin/env python3

def merge(L1, L2):
    """merges two lists which are sorted in 
    ascending order into a sorted list in  ascending order"""
    lst = []
    n = len(L2) + len(L1)
    index1 = 0
    index2 = 0
    for i in range(n):
        if index2 < len(L2) and index1 < len(L1):
            if L1[index1] < L2[index2] :
                lst.append(L1[index1])
                index1 += 1
            else:
                lst.append(L2[index2])
                index2 += 1
        elif index2 == len(L2):
            lst.append(L1[index1])
            index1 += 1
        elif index1 == len(L1):
            lst.append(L2[index2])
            index2 += 1
        else: #shouldn't be reached!
            pass
    return lst



def main():
    lst1 = [1,2,3]
    lst2 = [1,3,5]
    lst3 = [1,2,5,7,9]
    print(merge(lst3, lst2))
    print(merge(lst1, lst2))

if __name__ == "__main__":
    main()
