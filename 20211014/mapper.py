import sys
import pdb
import re

def preprocess(text):
    # preprocess/tokenize the sentence
    processed_data = re.findall('[a-z]+', text.lower())
    
    return processed_data

def _map(text: str):
    tokens = preprocess(text)
    steps = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
    for i in range(len(tokens)):
        for s in steps:
            if i + s >= 0 and i + s <= len(tokens) - 1:
                # w = ' '.join([tokens[i], tokens[i + s]])
                print(tokens[i] + "\t" + tokens[i + s] + "\t" + str(s) + "\t" + str(1))
    
    
    # [ TODO ] generate the mapper output
    # Output: "{pivot}\t{word}\t{distance}\t{count}"
    # Example: 
    #   predict is  -3  1
    #   predict used    -2  1
    #   predict the -1  1
    #   predict the 1   1
    #   ...
    
if __name__== "__main__" :
    for line in sys.stdin:
        _map(line)
        # break # for the sake of this practice, just test the first page now
        
     