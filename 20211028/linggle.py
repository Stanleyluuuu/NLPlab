#!/usr/bin/env python
# -*- coding: utf-8 -*-
from operator import itemgetter
from itertools import product
from heapq import nlargest
import logging
import pdb


MAX_LEN = 5


def parse_ngramstr(text):
    ngram, count = text.rsplit(maxsplit=1)
    return ngram, int(count)


def parse_line(line):
    query, *ngramcounts = line.strip().split('\t')
    return query, tuple(map(parse_ngramstr, ngramcounts))


def expand_query(query):
    # TODO: write your query expansion, e.g.,
    #  "in/at afternoon" -> ["in afternoon", "at afternoon"]
    #  "listen ?to music" -> ["listen music", "listen to music"]
    # pdb.set_trace()
    words, ans = query.split(), []
    ans = []
    for i, w in enumerate(words):
        if "/" in w:
            combinations = w.split("/")
            for com in combinations: ans.append(query.replace(query.split()[i], com))
        elif "?" in w:
            w = w.replace("?", "")
            ans.append(query.replace(" " + query.split()[i], ""))
            ans.append(query.replace(query.split()[i], w))
        elif "*" == w:
            ans.append(query.replace(" " + query.split()[i], ""))
            ans.append(query.replace(query.split()[i], "_"))
    if len(ans) == 0: ans.append(query)
    
    return ans

def extend_query(query):
    # TODO: write your query extension, 
    # e.g., can tolerate missing/unnecessary determiners
    return [query]


def load_data(lines):
    logging.info('Loading...', end='')
    # read linggle data
    linggle_table = {query: ngramcounts for query, ngramcounts in map(parse_line, lines)}
    logging.info('ready.')
    return linggle_table


def linggle(linggle_table):
    q = input('linggle> ')

    # exit execution keyword: exit()
    if q == 'exit()':
        return

    # extend and expand query
    queries = [
        simple_query
        for query in extend_query(q)
        for simple_query in expand_query(query)
    ]
    # gather results
    ngramcounts = {item for query in queries if query in linggle_table for item in linggle_table[query]}
    # output 10 most common ngrams
    ngramcounts = nlargest(10, ngramcounts, key=itemgetter(1))
    if len(ngramcounts) > 0:
        print(*(f"{count:>7,}: {ngram}" for ngram, count in ngramcounts), sep='\n')
    else:
        print(' '*8, 'no result.')
    print()

    return True

if __name__ == '__main__':
    import fileinput
    # If the readline module was loaded, then input() will use it to provide elaborate line editing and history features.
    # https://docs.python.org/3/library/functions.html#input
    import readline
    # with open("./data/Template_linggle_DIY/bnc.linggle.sample.txt", "r") as f:
        # datas = f.readlines()
    linggle_table = load_data(fileinput.input())
    while linggle(linggle_table):
    # while linggle(datas):
        pass