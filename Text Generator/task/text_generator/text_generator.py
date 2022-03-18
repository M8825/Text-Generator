from nltk.tokenize import WhitespaceTokenizer
from nltk.probability import FreqDist
from nltk import bigrams
from collections import Counter

file = open(input(), 'r', encoding='utf-8').read()

corpus = WhitespaceTokenizer().tokenize(file)
bgrms = list(bigrams(corpus))
total_bigrams = FreqDist(bgrms).N()

print(f'Number of bigrams: {total_bigrams}')

while True:
    usr_inp = input()

    if usr_inp == 'exit': break
    else:
        try:
            # Create dictionary of unique head and all available keys.
            chain = {}
            for head, tail in bgrms:
                chain.setdefault(head, []).append(tail)
            tails = Counter(chain[usr_inp]).most_common()  # TODO Maybe check usr_inp type?
            print('Head:', usr_inp)

            for word, count in tails:
                print('Tail:', word, ' Count:', count)

        except (ValueError, TypeError):
            print('Type Error. Please input an integer.')
        except IndexError:
            print('Index Error. Please input an integer that is in the range of the corpus.')
        except KeyError:
           print('Key Error. The requested word is not in the model. Please input another word.')