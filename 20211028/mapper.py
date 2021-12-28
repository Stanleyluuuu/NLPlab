import pdb
import fileinput
import random

def cal(word, leng):
    result = []
    for w in word:
        for i in range(leng):
            q = w.split(" ")
            if i > 0:
                q[i] = "_"
                result.append(" ".join(q))

    return result

def blank(word, leng):
    word, possible = [word], []
    for a in range(leng - 1):
        word = cal(word, leng)
        possible.extend(word)
    result = list(set(possible))
    
    return result

def inverted_index_map(lines):
    for line in lines:
        info = [g[:-1] if g.endswith("\n") else g for g in line.split("\t")]
        word, leng, count, results = info[0], len(info[0].split(" ")), info[1], []
        results.append(word)
        if leng > 1:
            results.extend(blank(word, leng))
            for r in results:
                yield r, count
        else:
            yield word, count

if __name__ == '__main__':
    for word, count in inverted_index_map(fileinput.input()):
        print(word + "\t" + count)