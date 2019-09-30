#!/usr/bin/env python3

def reverse_dictionary(d):
    dikt = {}
    for key, value in d.items():
        for val in value:
            try:
                a = dikt[val]
                a = list(a)
                a.append(key)
                dikt[val] = a
            except KeyError:
                dikt[val] = key
    return dikt

def reverse_dictionary(d):
    dikt = {}
    pairs = list(zip(d.values(), d.keys()))
    for tupple in pairs:
        if len(tupple[0]) > 1:
            for s in tupple[0]:
                # s Finnish word, tupple[1] english word
                if s in dikt:
                    vals = list(dikt[s])
                    vals.append(tupple[1])
                else:
                    vals = tupple[1]
                dikt[s] = vals
        elif len(tupple[0]) == 1:
            s = tupple[0][0]
            if s in dikt:
                vals = list(dikt[s])
                vals.append(tupple[1])
            else:
                vals = tupple[1]
            dikt[s] = vals
    return dikt

def main():
    pass

if __name__ == "__main__":
    main()
