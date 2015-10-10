from collections import defaultdict, Counter
from itertools import ifilter
import os
import pickle

def pairwise(iterable):
    it = iter(iterable)
    last = next(it)
    for curr in it:
        yield last, curr
        last = curr

valid = set('abcdefghijklmnopqrstuvwxyz ')

def valid_pair((last, curr)):
    return last in valid and curr in valid

def make_markov(text, markov):
    lowercased = (c.lower() for c in text)
    for p, q in ifilter(valid_pair, pairwise(lowercased)):
        markov[p][q] += 1
    return markov

def genrandom(model, n):
    curr = choice(list(model))
    for i in xrange(n):
        yield curr
        if curr not in model:   # handle case where there is no known successor
            curr = choice(list(model))
        d = model[curr]
        target = randrange(sum(d.values()))
        cumulative = 0
        for curr, cnt in d.items():
            cumulative += cnt
            if cumulative > target:
                break

if __name__ == '__main__':
    markov = defaultdict(Counter)
    for fn in os.listdir('.'):
        with open(fn, 'r') as f:
            for line in f:
                try:
                    make_markov(line.split()[1], markov)
                except IndexError:
                    pass
    with open('markov.pkl', 'w') as f:
        pickle.dump(markov, f)
