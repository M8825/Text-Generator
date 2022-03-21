from nltk.tokenize import WhitespaceTokenizer
from nltk import trigrams
from collections import Counter
from random import choice, choices
import re

file = open(input(), 'r', encoding='utf-8').read()

corpora = WhitespaceTokenizer().tokenize(file)  # Create corpora based of spaces between words
tri_grams = list(trigrams(corpora))

# Create dictionary of unique 2 word <head> and 1 word <tail>.
chain = {}
for head_one, head_two, tail in tri_grams:
    chain.setdefault(f'{head_one} {head_two}', []).append(tail)

for _ in range(10):
    new_line = []
    c = 0
    while True:
        if c == 0:  # Find proper start word for sentence
            head_word = choice(list(chain.keys()))
            is_start = bool(re.match(r'^[A-Z].*[^.?!]\s', head_word))  # Check if word matches beginning of the sentence
            if not is_start: continue                                  # criteria
            else:
                new_line.append(head_word)

        tails = Counter(chain[head_word]).most_common()

        # Create list of Tails and Counts
        tails_lst, weights_lst = [], []
        for word, count in tails:
            tails_lst.append(word)
            weights_lst.append(count)
        next_word = ''.join(choices(tails_lst, weights=weights_lst))  # choices() returns [] we need str()

        new_line.append(next_word)
        head_word = ' '.join(' '.join(new_line).split()[-2:])  # New <head> consists last 2 words in developing line

        if c >= 2:
            is_end = bool(re.match(r'.*[.?!]$', head_word))  # Check if word matches end of the sentence criteria
            if is_end: break
        c += 1

    print(*new_line, sep=' ', end='\n')  # Print each line.
