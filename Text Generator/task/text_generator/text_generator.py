from nltk.tokenize import WhitespaceTokenizer
from nltk.probability import FreqDist

file = open(input(), 'r', encoding='utf-8').read()

corpus = WhitespaceTokenizer().tokenize(file)
total_words = FreqDist(corpus).N()
unique_words = FreqDist(corpus).B()


print('Corpus statistics')
print('All tokes: ', total_words)
print('Unique tokes', unique_words, '\n')

while True:
    usr_inp = input()

    if usr_inp == 'exit':
        break
    else:
        try:
            index = int(usr_inp)
            print(corpus[index])
        except (ValueError, TypeError):
            print('Type Error. Please input an integer.')
        except IndexError:
            print('Index Error. Please input an integer that is in the range of the corpus.')
