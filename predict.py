import os
import re
from collections import Counter
from os import listdir

from os.path import isfile, join

from estimate_models import read_and_clean_corpus, find_bigrams

dashes = ["----", "-----", "---", "--"]
w2 = ["am", "is", "be"]
w3 = ["are", "was"]
w4 = ["were", "been"]
w5 = ["being"]
data_dir = "/test"
inputs = [f for f in listdir(os.getcwd() + data_dir) if isfile(join(os.getcwd() + data_dir, f))]

unigrams = read_and_clean_corpus("corpus.txt")
unigrams_collection = Counter(unigrams)
bigrams, bigrams_collection = find_bigrams(unigrams)


def calc_lang_model(unigrams_collection, bigrams_collection, word1, word2):
    """
    Using that function we calculate the bigram language model
    :param probs_dict: dict of unigram probabilities
    :param bigrams: list of bigrams
    :param bigrams_collection: bigrams frequeuncy dict
    :return:
    """
    paronomasths = len(unigrams_collection)
    arithmhths = 1
    if word1 in unigrams_collection.keys():
        paronomasths += unigrams_collection[word1]
    if (word1, word2) in bigrams_collection.keys():
        arithmhths += bigrams_collection[(word1, word2)]
    return arithmhths / paronomasths

    bigrams_prob = {}
    unique_bigrams = list(set(bigrams))
    for bigram in unique_bigrams:
        bigrams_prob[bigram] = bigrams_collection[bigram] / unigrams_collection[bigram[0]]
    return bigrams_prob


def process_input(file):
    """
    The following function process test files
    :param file: file path
    :return:
    """
    words = []
    with open(file, encoding="utf8") as inp:
        lines = inp.readlines()
        for i in range(len(lines)):
            if i == 0:
                continue
            else:
                words += lines[i].split(" ")
    return words


def predict_occurence(file_words, bigrams_collection, unigrams_collection):
    file_words_cp = file_words
    w5indices = [i for i, x in enumerate(file_words) if x == "-----"]
    w4indices = [i for i, x in enumerate(file_words) if x == "----"]
    w3indices = [i for i, x in enumerate(file_words) if x == "---"]
    if w5indices:
        for indx in w5indices:
            file_words_cp[indx] = "being"

    if w4indices:
        for indx in w4indices:
            prob1 = calc_lang_model(unigrams_collection, bigrams_collection, file_words[indx - 1], "were")
            prob2 = calc_lang_model(unigrams_collection, bigrams_collection, file_words[indx - 1], "been")
            print("The probabilities are {}, {}".format(str(prob1), str(prob2)))
            if prob1 > prob2:
                file_words_cp[indx] = "were"
            else:
                file_words_cp[indx] = "been"

    if w3indices:
        for indx in w3indices:
            prob1 = calc_lang_model(unigrams_collection, bigrams_collection, file_words[indx - 1], "are")
            prob2 = calc_lang_model(unigrams_collection, bigrams_collection, file_words[indx - 1], "was")
            print("The probabilities are {}, {}".format(str(prob1), str(prob2)))
            if prob1 > prob2:
                file_words_cp[indx] = "was"
            else:
                file_words_cp[indx] = "are"
    print(file_words_cp)


ws = process_input("test/input00.txt")
predict_occurence(ws, bigrams_collection, unigrams_collection)
