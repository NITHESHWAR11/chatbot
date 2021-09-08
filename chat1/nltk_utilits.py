import nltk
import numpy as np

# nltk.download('punkt')

def tokenize(sentence):
    """
    Tokenizes a sentence into words
    :param sentence:
    :return:
    """
    return nltk.word_tokenize(sentence)

def stem(word):
    """
    Stems a word
    :param word:
    :return:
    """
    return nltk.PorterStemmer().stem(word.lower())

def bag_of_words(tokensed_sentence, all_words):
    """
    Creates a bag of words from a tokenized sentence
    :param tokensed_sentence:
    :param all_words:
    :return bag_of_words: 
    """
    bag = []
    tokensed_sentence = [stem(word) for word in tokensed_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokensed_sentence:
            bag[idx] = 1.0
    return bag