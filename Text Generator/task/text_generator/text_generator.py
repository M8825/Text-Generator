from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams
from collections import Counter
from random import choice, choices
import re

file = open(input(), 'r', encoding='utf-8').read()

corpus = WhitespaceTokenizer().tokenize(file)
bgrms = list(bigrams(corpus))


# Create dictionary of unique head and all available keys.
chain = {}
for head, tail in bgrms:
    chain.setdefault(head, []).append(tail)

for _ in range(10):
    new_line = []
    c = 0
    while True:
        if c == 0:  # When sentence starts with lower case
            head_word = choice(corpus)
            is_start = bool(re.match(r'^[A-Z].*[^.?!]$', head_word) )
            if not is_start: continue
            else:
                new_line.append(head_word)

        tails = Counter(chain[head_word]).most_common()

        # Create list of Tails and Counts
        tails_lst, weights_lst = [], []
        for word, count in tails:
            tails_lst.append(word)
            weights_lst.append(count)
        next_word = ''.join(choices(tails_lst, weights=weights_lst))  # choices() returns [] we need str()

        head_word = next_word  # New head for next tails
        new_line.append(next_word)

        if c >= 3:
            is_end = bool(re.match(r'.*[.?!]$', head_word))
            if is_end: break
        c += 1

    print(*new_line, sep=' ', end='\n')
