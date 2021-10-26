import sys
import pdb
import os

def update(ans, index):
    ans[0] += 1
    ans[index] += 1

    return ans

# python mapper.py < data/wiki1G.txt | sort | python reducer.py > skipgram.tsv
if __name__== "__main__" :
    steps, pre_word = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5], " "
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        word, distance = ' '.join(line.split()[:2]), int(line.split()[-1])        
        if word != pre_word:
            if pre_word == " ":
                pre_word = word
                t = [0 for g in range(11)]
                t = update(t, steps.index(distance))
            else:
                # print(word.split()[0] + "\t" + word.split()[1] + "\t" + str(t[0]) + "\t" + str(t[1]) + "\t" + str(t[2]) + "\t" + str(t[3]) + "\t" + str(t[4]) + "\t" + str(t[5]) + "\t" + str(t[6]) + "\t" + str(t[7]) + "\t" + str(t[8]) + "\t" + str(t[9]) + "\t" + str(t[10]))
                print(pre_word.split()[0] + "\t" + pre_word.split()[1] + "\t" + str(t[0]) + "\t" + str(t[1]) + "\t" + str(t[2]) + "\t" + str(t[3]) + "\t" + str(t[4]) + "\t" + str(t[5]) + "\t" + str(t[6]) + "\t" + str(t[7]) + "\t" + str(t[8]) + "\t" + str(t[9]) + "\t" + str(t[10]))
                pre_word = word
                t = [0 for g in range(11)]
                t = update(t, steps.index(distance))
        else:
            t = update(t, steps.index(distance))
        
    print(word.split()[0] + "\t" + word.split()[1] + "\t" + str(t[0]) + "\t" + str(t[1]) + "\t" + str(t[2]) + "\t" + str(t[3]) + "\t" + str(t[4]) + "\t" + str(t[5]) + "\t" + str(t[6]) + "\t" + str(t[7]) + "\t" + str(t[8]) + "\t" + str(t[9]) + "\t" + str(t[10]))

        

        # [ TODO ] collect the output from shuffler and generate reducer output
        # Now you need to calculate the skip-gram frequency with its distance information.
        # Input: 
        #   "{pivot}\t{word}\t{distance}\t{count}"
        # Output: 
        #   "{pivot}\t{word}\t{total_freq}\t{-5}\t{-4}\t{-3}\t{-2}\t{-1}\t{1}\t{2}\t{3}\t{4}\t{5}"
        # Example:
        #   See the sample output file given by TA.
        # Steps: 
        #   1) Parse the input from shuffler
        #   2) Check if this is the same skipgram
        #   3) If so, add the frequency according to its distance
        #   4) If not, output the previous skipgram data
        # ...
