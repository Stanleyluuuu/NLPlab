import os
import re
import pdb
import numpy as np

def unigram(text):
    """ [TODO] Get the 1-gram list from string
    @param text: given string
    @return: a list of token
    """
    text = text.lower()
    tokens = re.findall(r"[\w]+", text)

    return tokens

def bigram(text):
    """ [TODO] Get the 2-gram list """
    text, n = text.lower(), 2
    tokens = re.findall(r"[\w]+", text)
    tokens = [tokens[i:i+n] for i in range(len(tokens)) if (i+n-1) <= len(tokens) - 1]
    tokens = [' '.join(t) for t in tokens]

    return tokens

def calculate_frequency(tokens):
    frequency = {}
    for t in tokens:
        try:
            frequency[t] += 1
        except:
            frequency[t] = 1
            
    return frequency

def P_mle(uni_freq, bi_freq, word: str, pre_word: str = None):
    """ [TODO] Return the P(word|pre_word), which should be a float """
    if pre_word == None:
        N = sum(uni_freq.values())
        p_w = uni_freq[word] / N
    else:
        w = ' '.join((pre_word, word))
        try:
            p_w = bi_freq[w] / uni_freq[pre_word]
        except:
            p_w = 0 / uni_freq[pre_word]
        
    return p_w

def sentence_prob(uni_freq, bi_freq, sentence: str, P):
    """ Calculate the probability of a given sentence with given P-model.
    @param sentence: the given sentence
    @param P: the probability model to use. (like your `P_mle` above)
    @return: a float indicating the probability
    """
    words = unigram(sentence)
    sen_prob = 0
    for i in range(1, len(words)):
        a = P(uni_freq, bi_freq, words[i], words[i-1])
        # print("P({}|{}) = {}".format(words[i], words[i-1], a))
        sen_prob += np.log(a + 1e-20)
        print(np.log(a + 1e-20))

    return sen_prob

def P_add1(uni_freq, bi_freq, word: str, pre_word: str):
    """ [TODO] Return the P(word|pre_word) with Laplace smoothing. """
    w = ' '.join((pre_word, word))
    try:
        p_w = (bi_freq[w] + 1) / (uni_freq[pre_word] + sum(uni_freq.values()))
    except:
        p_w = 1 / (uni_freq[pre_word] + sum(uni_freq.values()))

    return p_w

if __name__ == "__main__":        
    with open(os.path.join('data', 'big.txt'), 'r') as f:
        corpus = f.read()
    uni_freq = calculate_frequency(unigram(corpus)) # [TODO] calculate the 1-gram frequency of the corpus
    bi_freq = calculate_frequency(bigram(corpus)) # [TODO] calculate the 2-gram frequency of the corpus
    p1 = P_mle(uni_freq, bi_freq, 'book', 'read')
    p2 = P_mle(uni_freq, bi_freq, 'books', 'read')
    print(f'p1: {p1}; \np2: {p2}')

    p1 = P_mle(uni_freq, bi_freq, 'books', 'a')
    p2 = P_mle(uni_freq, bi_freq, 'book', 'a')
    print(f'p1: {p1}; \np2: {p2}')

    p1 = P_mle(uni_freq, bi_freq, 'have', 'he')
    p2 = P_mle(uni_freq, bi_freq, 'has', 'he')
    print(f'p1: {p1}; \np2: {p2}')

    p1 = sentence_prob(uni_freq, bi_freq, 'He have to take the medicine.', P=P_mle)
    p2 = sentence_prob(uni_freq, bi_freq, 'He has to take the medicine.', P=P_mle)
    print(f'p1: {p1}; \np2: {p2}')

    sentence_prob(uni_freq, bi_freq, "He has to eat medicine.", P=P_mle)

    p1 = P_add1(uni_freq, bi_freq, 'medicine', 'eat')
    p2 = P_add1(uni_freq, bi_freq, 'medicine', 'take')
    print(f'p1: {p1}; \np2: {p2}')    

    test_cases = [
                'He have to take the medicine.',
                'He has to eat the medicine.',
                'He has to take the medicine.'
                ]

    for sent in test_cases:
        print(sent, sentence_prob(uni_freq, bi_freq, sent, P=P_add1))

    test_cases = [
                'He is looking to a job.',
                'He is looking for a job.'
                ]

    for sent in test_cases:
        print(sent, sentence_prob(uni_freq, bi_freq, sent, P=P_add1))

    sent = "He school nice and happy."
    print(sent, sentence_prob(uni_freq, bi_freq, sent, P=P_add1))
    sent = "He went to school yesterday and had a nice time there."
    print(sent, sentence_prob(uni_freq, bi_freq, sent, P=P_add1))
    sent = "He is"
    print(sent, sentence_prob(uni_freq, bi_freq, sent, P=P_add1))
    sent = "He are"
    print(sent, sentence_prob(uni_freq, bi_freq, sent, P=P_add1))
    sent = "He am"
    print(sent, sentence_prob(uni_freq, bi_freq, sent, P=P_add1))