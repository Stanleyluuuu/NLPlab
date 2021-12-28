import pdb
from itertools import groupby
from operator import itemgetter
import fileinput

def inverted_index_reduce(items):
    for word, word_lines in groupby(items, key=itemgetter(0)):
        line_numbers, sorted = [line_no for line_no in word_lines], {}
        for line in line_numbers:
            if "_" in line:
                w = " ".join(line[:-1])
                need = [n for n in line[:-1] if n != "_"]
                same_lines = [l for l in line_numbers if len(l) == len(line) and "_" not in l and set(need).issubset(l)]
                if w not in sorted: sorted[w] = same_lines
            else:
                w = " ".join(line[:-1])
                sorted[w] = line
        for (key, value) in sorted.items():
            big = []
            if type(value[0]) == list:
                for v in value:
                    w = " ".join(v)
                    big.append(w)
                yield key, big
            else:
                w = [" ".join(value)]
                yield key, w

if __name__ == '__main__':
    iterable = map(str.split, fileinput.input())
    for word, line_numbers in inverted_index_reduce(iterable):
        print(word, *line_numbers, sep='\t')