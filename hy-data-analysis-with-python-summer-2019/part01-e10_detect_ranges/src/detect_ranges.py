#!/usr/bin/env python3


def detect_ranges(L):
    l = sorted(L)
    l2 = []
    li = []
    n = len(l) - 1
    for i in range(n):
        if l[i] + 1 == l[i+1]:
            li.append(i)
            li.append(i+1)
            if(i+1 == n): 
            # list ends with a sequence
                index1 = min(li)
                index2 = max(li)
                l2.append((l[index1], l[index2] + 1))       
        elif len(li) > 0:
        # end of a sequence detected
            index1 = min(li)
            index2 = max(li)
            l2.append((l[index1], l[index2] + 1)) 
            # i is index2 + 1
            # +1 since it's like range(k, l)
            li = [] 
            # reset list of indices
        else:
            l2.append(l[i])
            # not a part of a range, nor one past a range
            if(i + 1 == n):
                l2.append(l[i+1])
    return l2

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(sorted(L))
    print(result)

if __name__ == "__main__":
    main()

