# Text-Generator
JetBrains - Python Core - project

Generates 10 sentence from corpus file. Beginning of the chain is a randomly chosen Head from the model (not just any word from the corpus). 
When predicting the next word, the model takes the concatenation of the last two tokens of the chain separated by a space and feds the model to
find new word from set of trigrams based on number of occurrences in corpus.

Model is based on list of trigrams from corpora. It consists of Heads and Tails, but Heads consist of two-separated tokens concatenated into a single string.
The Tails consist of one token. 

