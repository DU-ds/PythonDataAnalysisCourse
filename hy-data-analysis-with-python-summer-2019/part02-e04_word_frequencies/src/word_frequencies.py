#!/usr/bin/env python3

def word_frequencies(filename):
    dikt = {}
with open(filename, "r") as f:
    lst = f.readlines()
    lst2= []
    lst = list(map(lambda x: x.split(), lst))
for x in lst:
    for e in x:
        lst2.append(e.strip("""!"#$%&'()*,-./:;?@[]_"""))
    # lst = list(map((lambda x: e.strip("""!"#$%&'()*,-./:;?@[]_""") for e in x), lst))
    for s in lst2:
        if s in dikt:
            dikt[s] += 1
        else:
            dikt[s] = 1

def main():
    print(word_frequencies(filename='R:/Git/PythonDataAnalysisCourse/hy-data-analysis-with-python-summer-2019/part02-e04_word_frequencies/src/alice.txt'))

if __name__ == "__main__":
    main()

