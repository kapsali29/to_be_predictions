from collections import Counter

from nltk import RegexpTokenizer
from nltk.util import ngrams
from nltk.corpus import stopwords


def read_and_clean_corpus(filepath):
    """
    Using that function you are able to read and clean the training corpus
    :param filepath: corpus file
    :return:
    """
    tokenizer = RegexpTokenizer(r'\w+')
    exclude = set(['am', 'are', 'were', 'was', 'is', 'been', 'being', 'be'])
    stop_words = set(stopwords.words('english'))
    stop_words.difference_update(exclude)
    with open(filepath, encoding="utf8", errors="ignore") as f:
        corpus = f.read()
    words = tokenizer.tokenize(corpus)
    unigrams = [word.lower() for word in words if
                word not in stop_words and word != "" and not word.isdigit() and len(word) > 1]
    return unigrams


def calculate_unigrams_probs(unigrams):
    """
    Using that function you are able to calculate unigram propabilities based the corpus.
    :param unigrams: list of unigrams
    :return: dict of probs
    """
    probs_dict = {}
    unigram_collections = Counter(unigrams)
    for word in unigram_collections.keys():
        probs_dict[word] = unigram_collections[word] / len(unigrams)
    return probs_dict, unigram_collections


def find_bigrams(unigrams):
    """
    Using that function we transform unigrams to bigrams
    :param unigrams: list of unigrams
    :return:
    """
    bigrams = [gram for gram in ngrams(unigrams, 2)]
    bigram_collection = Counter(bigrams)
    return bigrams, bigram_collection
