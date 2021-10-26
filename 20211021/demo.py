import numpy as np
import pdb
import collections

def C1_filter(base_word, pt=False):
### [TODO]
    f_bar, std, filtered_by_C1 = np.mean([int(col[2]) for col in collocates if col[0] == base_word]), np.std([int(col[2]) for col in collocates if col[0] == base_word]), {}
    for col in collocates:
        if col[0] == base_word:
            word, freq = col[1], int(col[2])
            strength = round((freq - f_bar) / std, 3)
            if strength > k0:
                filtered_by_C1[word] = {"strength":strength}
                if pt: print("{}{}".format(word, filtered_by_C1[word]))

    return filtered_by_C1

def C2_filter(base_word, filtered_by_C1, pt=False):
### [TODO]
    filtered_by_C2 = {}
    for col in collocates:
        if col[0] == base_word and col[1] in filtered_by_C1:
            word, pi_bar = col[1], int(col[2]) / 10
            up = [(int(col[i]) - pi_bar)**2 for i in range(3, 13)]
            spread = round(sum(up) / 10, 2)
            if spread >= U0:
                filtered_by_C2[word] = {"strength":filtered_by_C1[word]["strength"], "spread":spread}
                if pt: print("{}{}".format(word, filtered_by_C2[word]))
    
    return filtered_by_C2

def C3_filter(base_word, filtered_by_C2, pt=False):
### [TODO]
    filtered_by_C3, step = {}, {3:-5, 4:-4, 5:-3, 6:-2, 7:-1, 8:1, 9:2, 10:3, 11:4, 12:5}
    for col in collocates:
        if col[0] == base_word and col[1] in filtered_by_C2:
            word, pi_bar, spread = col[1], int(col[2]) / 10, filtered_by_C2[col[1]]["spread"]
            criterion = round(pi_bar + (k1 * np.sqrt(spread)), 3)
            for i in range(3, 13):
                pij = int(col[i])
                if pij >= criterion:
                    filtered_by_C3[(base_word, word, step[i])] = {"strength":filtered_by_C2[word]["strength"], "spread":filtered_by_C2[word]["spread"], "peak":criterion, "count":pij}
                    if pt: print("{}{}".format((base_word, word, step[i]), filtered_by_C3[(base_word, word, step[i])]))
    
    return filtered_by_C3
                
def find_strongest_collocation(base_word, filtered_by_C3):
### [TODO]
    max, max_str, max_count = None, 0, 0
    for i in filtered_by_C3:
        if filtered_by_C3[i]["strength"] > max_str: max, max_str, max_count = i, filtered_by_C3[i]["strength"], filtered_by_C3[i]["count"]
        elif filtered_by_C3[i]["strength"] == max_str:
            if filtered_by_C3[i]["count"] > max_count:
                max, max_str, max_count = i, filtered_by_C3[i]["strength"], filtered_by_C3[i]["count"]
    print(max)

def combination(base_word):
### [TODO]
    c1 = C1_filter(base_word)
    c2 = C2_filter(base_word, c1)
    c3 = C3_filter(base_word, c2)
    find_strongest_collocation(base_word, c3)

#### here are some hyperparameter
k0 = 1
k1 = 1
U0 = 10
base_word = "depend"
## read file here

with open("./data/AKL_skipgram.tsv", "r") as f:
    collocates = [s.split() for s in f.readlines()]
filtered_by_C1 = C1_filter(base_word, pt=True)
print("\n\n\n")
filtered_by_C2 = C2_filter(base_word, filtered_by_C1, pt=True)
print("\n\n\n")
filtered_by_C3 = C3_filter(base_word, filtered_by_C2, pt=True)
print("\n\n\n")
find_strongest_collocation(base_word, filtered_by_C3)
print("\n\n\n")

AKL_verbs = ['argue', 'can', 'consist', 'contrast', 'favour', 'lack', 'may', 
            'neglect', 'participate', 'present', 'rely', 'suggest']
for base_word in AKL_verbs:
    combination(base_word)
