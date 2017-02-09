import collections
import itertools
import re

import scipy.spatial.distance

# Same as pa1, but without numpy

sentences = []
with open('sentences.txt', 'r') as f:
    for line in f:
        sentences.append(list([_f for _f in re.split('[^a-z]', line.lower()) if _f]))

words = list(collections.OrderedDict.fromkeys(list(itertools.chain.from_iterable(sentences))).keys())


def count(a, b):
    result = [0] * len(a)
    for k, v in enumerate(a):
        result[k] = b.count(a[k])
    return result


def count_all(a, b):
    result = [[0] * len(a)] * len(b)
    for k, v in enumerate(b):
        result[k] = count(a, v)
    return result


index_matrix = count_all(words, sentences)
for v in index_matrix:
    print((scipy.spatial.distance.cosine(index_matrix[0], v)))
