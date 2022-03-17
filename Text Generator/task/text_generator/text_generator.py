from nltk.tokenize import WhitespaceTokenizer
from nltk.probability import FreqDist
from nltk import bigrams

file = open(input(), 'r', encoding='utf-8').read()

corpus = WhitespaceTokenizer().tokenize(file)
bgrms = list(bigrams(corpus))
total_bigrams = FreqDist(bgrms).N()

print(f'Number of bigrams: {total_bigrams}')

while True:
    usr_inp = input()

    if usr_inp == 'exit':
        break
    else:
        try:
            index = int(usr_inp)
            bgrm_index = bgrms[index]
            print('Head:', bgrm_index[0], 'Tail:', bgrm_index[1])
        except (ValueError, TypeError):
            print('Type Error. Please input an integer.')
        except IndexError:
            print('Index Error. Please input an integer that is in the range of the corpus.')
