import re
import collections
import itertools
import scipy.spatial.distance

import numpy as np

sentences = []
with open('sentences.txt', 'r') as f:
    for line in f:
        sentences.append(list([_f for _f in re.split('[^a-z]', line.lower()) if _f]))

all_words = np.array(list(collections.OrderedDict.fromkeys(list(itertools.chain.from_iterable(sentences))).keys()))
all_sentences = np.array(sentences)


def count(a, b):
    result = np.zeros(len(a))
    for k, v in np.ndenumerate(a):
        if np.in1d(a[k], b):
            result[k] += 1
    return result


def count_all(a, b):
    result = np.zeros([len(b), len(a)])
    for k, v in np.ndenumerate(b):
        result[k[0]] = count(a, v)
    return result


index_matrix = count_all(all_words, all_sentences)
for v in index_matrix:
    print((scipy.spatial.distance.cosine(index_matrix[0], v)))