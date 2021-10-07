from collections import Counter, defaultdict
import math, re
import kenlm
import operator
import itertools
import pdb
import os

model = kenlm.Model('bnc.prune.arpa')

def words(text): return re.findall(r'\w+|[,.?]', text.lower())

WORDS = Counter(words(open('big.txt').read()))

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return float(WORDS[word] / N)


def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)


def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


def suggest(word):
    '''return top 5 words as suggestion, original_word as top1 when original_word is correct'''
    suggest_P = {}
    edits_set = edits1(word).union(set(edits2(word)))
    for candidate in known(edits_set):
        suggest_P[candidate] = P(candidate)
    if word in WORDS:
        suggest_P[word] = 1
    suggest_can = sorted(suggest_P, key=suggest_P.get, reverse=True)[:5]
    
    return suggest_can

###### Task1 ######
def spelling_check(sentence):
    sentence = sentence.split()
    candidate, wrong, start = [], {}, 0
    ## TODO ##
    with open("big.txt", "r") as f: corpus = f.read()
    tokens = re.findall(r"[\w]+", corpus.lower())
    for i, sen in enumerate(sentence):
        if sen not in tokens: wrong[i] = suggest(sen)
    for index in wrong:
        try:
            if ' '.join(sentence[start:index]) != "":
                sen = [w + " " + ' '.join(sentence[start:index]) for w in pre_sen]
            else:
                sen = pre_sen
            concated_sen = [a + " " + b for a in sen for b in wrong[index]]
            start = index + 1
            pre_sen = concated_sen
        except:
            sen = [' '.join(sentence[start:index])]
            concated_sen = [a + " " + b for a in sen for b in wrong[index]]
            start = index + 1
            pre_sen = concated_sen
    candidate = [w + " " + ' '.join(sentence[start:]) for w in pre_sen]
    # model = kenlm.Model(os.path.join('../kenlm/lm', 'test.arpa'))
    model = kenlm.Model('bnc.prune.arpa')
    best = [candidate[0], model.score(candidate[0], bos = True, eos = True) / len(candidate[0])]
    for can in candidate:
        if (model.score(can, bos = True, eos = True) / len(can)) > best[1]:
            best = [can, model.score(can, bos = True, eos = True) / len(can)]
    
    return best[0], candidate


print("Task 1 Spelling Check")
task1_input = 'he sold everythin escept the housee'
print("Text:",task1_input,"\n")
print("Candidates:")
task1_result, task1_candidate = spelling_check(task1_input)
for i in task1_candidate[:30]:
    print(i)
print("Number of Candidate:", len(task1_candidate))
print()
print("Result:", task1_result,"\n\n\n")


###### Task2 ######
atcs = {"", "the", "a", "an"}
preps = {"", "about", "at", "by", "for", "from", "in", "of", "on", "to", "with"}

def prep_check(sentence):
    sentence = sentence.split()
    candidate, suggestion, start = [], {}, 0
    ## TODO ##
    for i, sen in enumerate(sentence):
        if sen in atcs:
            suggestion[i] = atcs
        elif sen in preps:
            suggestion[i] = preps

    for index in suggestion:
        try:
            if ' '.join(sentence[start:index]) != "":
                sen = [w + " " + ' '.join(sentence[start:index]) for w in pre_sen]
            else:
                sen = pre_sen
            concated_sen = [a + " " + b if b != "" else a + b for a in sen for b in suggestion[index]]
            start = index + 1
            pre_sen = concated_sen
        except:
            sen = [' '.join(sentence[start:index])]
            concated_sen = [a + " " + b if b != "" else a + b for a in sen for b in suggestion[index]]
            start = index + 1
            pre_sen = concated_sen
    candidate = [w + " " + ' '.join(sentence[start:]) for w in pre_sen]
    # model = kenlm.Model(os.path.join('../kenlm/lm', 'bnc.prune.arpa'))
    model = kenlm.Model('bnc.prune.arpa')
    best = [candidate[0], model.score(candidate[0], bos = True, eos = True) / len(candidate[0])]
    for can in candidate:
        if (model.score(can, bos = True, eos = True) / len(can)) > best[1]:
            best = [can, model.score(can, bos = True, eos = True) / len(can)]
    
    return best[0], candidate
    

print("Task 2 Preposition and Article Check")
task2_input = 'look on an picture in the right'
print("Text:",task2_input,"\n")
task2_result, task2_candidate = prep_check(task2_input)
print("Candidates:")
for i in task2_candidate[:30]:
    print(i)
print("Number of Candidate:", len(task2_candidate))
print()
print("Result:", task2_result,"\n\n\n")


def process_sent(sent):
    ## TODO ##
    candidate1,_ = spelling_check(sent)
    candidate2,_ = prep_check(candidate1)

    return candidate2
    
    
print("Task 3 Combination")
task3_input = 'we descuss a possible meamin by that'
print("Text:",task3_input,"\n")
comb_result = process_sent(task3_input)
print("Result:", comb_result)