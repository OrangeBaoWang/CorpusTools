
import sys
import os

from corpustools.corpus.classes import Word

from corpustools.neighdens.neighborhood_density import neighborhood_density


def test_basic_corpus_nd(unspecified_test_corpus):
    calls = [({'corpus': unspecified_test_corpus,
                    'query':unspecified_test_corpus.find('mata'),
                    'max_distance':1},1.0),
            ({'corpus': unspecified_test_corpus,
                    'query':unspecified_test_corpus.find('nata'),
                    'max_distance':2},3.0)]

    for c,v in calls:
        result = neighborhood_density(**c)
        assert(abs(result[0]-v) < 0.0001)


def test_basic_corpus_mutation_minpairs(unspecified_test_corpus):
    calls = [({'corpus': unspecified_test_corpus,
                    'query':Word(**{'transcription': ['s', 'ɑ', 't', 'ɑ']},
                    'max_distance':1},2)]

    for c,v in calls:
        result = find_mutation_minpairs(**c)
        assert(result[0] == v)
        assert(result[1] == 'x')  # also check the identities of the minpairs rather than just their count