import re
from collections import Counter
import pdb

def words(text): return re.findall(r"w", text.lower())
with open("big.txt", "r") as f:
    t = f.read()

def calculate_frequency(tokens):
    frequency = {}
    for t in tokens:
        try:
            frequency[t] += 1
        except:
            frequency[t] = 1
    """
    Sample output: 
    {
        'the': 79809, 
        'project': 288,
        ...
    }
    """
    return frequency

def print_top_n(counter, n = 10):
    top_n = [(counter[t], t) for t in counter]
    for i in sorted(top_n, reverse=True)[:n]:
        print("{} {}".format(i[1], i[0]))

def get_ngram(tokens, n=2):
    tokens = [tokens[i:i+n] for i in range(len(tokens)) if (i+n-1) <= len(tokens) - 1]
    tokens = [' '.join(t) for t in tokens]
    
    return tokens

a = "Hello! I'm your TA!"
tokens = re.findall(r"[\w]+", t.lower())
print(re.findall(r"[\w]+", a.lower()))
counter = calculate_frequency(tokens)
c = print_top_n(counter)

get_ngram(tokens)
pdb.set_trace()