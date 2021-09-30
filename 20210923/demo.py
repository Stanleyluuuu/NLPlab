import re
from collections import Counter
import pdb
import os

def tokenize(text):
    # [ TODO ] transform to lower case
    text = text.lower()
    # [ TODO ] seperate the words
    tokens = re.findall(r"[\w]+", text)
        
    return tokens

def calculate_frequency(tokens):
    frequency = {}
    for t in tokens:
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

file_path = os.path.join('./data', 'BAWE.txt')
BAWE_unigram = []
#### [ TODO ] calculate document frequency of unigram in BAWE
BAWE_frequency = {}
with open(file_path, 'r') as f:
    for text in f.readlines():
        for sen in text.split("."):
            frequency = calculate_frequency(tokenize(sen))
            for b in frequency:
                try:
                    BAWE_frequency[b] += 1
                except:
                    BAWE_frequency[b] = 1

# Read Web1T Data
file_path = os.path.join('data', 'Web1T_unigram.txt')
Web1T_unigram_counter = {}
with open(file_path, 'r') as f:
    for line in f.readlines():
        line=line.rstrip("\n").split("\t")
        Web1T_unigram_counter[line[0]] = int(line[1])

Web1T_unigram_Rank = {}
#### [ TODO ] Rank unigrams for Web1T
Web1T_sorted = {k: v for k, v in sorted(Web1T_unigram_counter.items(), key=lambda item: item[1], reverse=True)}
rank, number = 0, 1e200
for k in Web1T_sorted:
    if Web1T_sorted[k] < number:
        rank += 1
    Web1T_unigram_Rank[k] = rank
    number = Web1T_sorted[k]
    
# {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
BAWE_unigram_Rank = {}
#### [ TODO ] Rank unigrams for BAWE
BAWE_sorted = {k: v for k, v in sorted(BAWE_frequency.items(), key=lambda item: item[1], reverse=True)}
rank, number = 0, 1e200
for k in BAWE_sorted:
    if BAWE_sorted[k] < number:
        rank += 1
    BAWE_unigram_Rank[k] = rank
    number = BAWE_sorted[k]

ranking_ratio = {}
for k in BAWE_unigram_Rank:
    try:
        ratio = Web1T_unigram_Rank[k] / BAWE_unigram_Rank[k]
    except:
        ratio = 1 / BAWE_unigram_Rank[k]
    ranking_ratio[k] = ratio
sorted_ranking_ratio = {k: v for k, v in sorted(ranking_ratio.items(), key=lambda item: item[1], reverse=True)}
rank, fill = 1, ' '
print(f'{"Rank":{fill}{"<"}{6}}', f'{"unigram":{fill}{"<"}{40}}', f'{"Rank Ratio":{fill}{"<"}{20}}')
for k in sorted_ranking_ratio:
    print(f'{str(rank):{fill}{"<"}{6}}', f'{k:{fill}{"<"}{40}}', f'{sorted_ranking_ratio[k]:{fill}{"<"}{20}}')
    rank += 1
    if rank > 30:
        break

#### [TODO]
file_path = os.path.join('./data', 'BAWE.txt')
#### [ TODO ] calculate document frequency of bigram in BAWE
BAWE_frequency_bigram = {}
with open(file_path, 'r') as f:
    for text in f.readlines():
        for sen in text.split("."):
            frequency = calculate_frequency(get_ngram(tokenize(sen), n=2))
            for b in frequency:
                try:
                    BAWE_frequency_bigram[b] += 1
                except:
                    BAWE_frequency_bigram[b] = 1

# Read Web1T Data
file_path = os.path.join('data', 'Web1T_bigram.txt')
Web1T_bigram_counter = {}
with open(file_path, 'r') as f:
    for line in f.readlines():
        line=line.rstrip("\n").split("\t")
        Web1T_bigram_counter[line[0]] = int(line[1])


Web1T_bigram_Rank = {}
#### [ TODO ] Rank bigrams for Web1T
Web1T_sorted = {k: v for k, v in sorted(Web1T_bigram_counter.items(), key=lambda item: item[1], reverse=True)}
rank, number = 0, 1e200
for k in Web1T_sorted:
    if Web1T_sorted[k] < number:
        rank += 1
    Web1T_bigram_Rank[k] = rank
    number = Web1T_sorted[k]

BAWE_bigram_Rank = {}
#### [ TODO ] Rank unigrams for BAWE
BAWE_sorted = {k: v for k, v in sorted(BAWE_frequency_bigram.items(), key=lambda item: item[1], reverse=True)}
rank, number = 0, 1e200
for k in BAWE_sorted:
    if BAWE_sorted[k] < number:
        rank += 1
    BAWE_bigram_Rank[k] = rank
    number = BAWE_sorted[k]

#### [TODO] calculate all rank ratios of bigrams in BAWE
ranking_ratio_bigram = {}
for k in BAWE_bigram_Rank:
    try:
        ratio = Web1T_bigram_Rank[k] / BAWE_bigram_Rank[k]
    except:
        ratio = 1 / BAWE_bigram_Rank[k]
    ranking_ratio_bigram[k] = ratio

#### [ TODO ] show the result
sorted_ranking_ratio_bi = {k: v for k, v in sorted(ranking_ratio_bigram.items(), key=lambda item: item[1], reverse=True)}
rank, fill = 1, ' '
print(f'{"Rank":{fill}{"<"}{6}}', f'{"unigram":{fill}{"<"}{40}}', f'{"Rank Ratio":{fill}{"<"}{20}}')
for k in sorted_ranking_ratio_bi:
    print(f'{str(rank):{fill}{"<"}{6}}', f'{k:{fill}{"<"}{40}}', f'{sorted_ranking_ratio_bi[k]:{fill}{"<"}{20}}')
    rank += 1
    if rank > 30:
        break