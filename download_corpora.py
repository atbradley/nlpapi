# -*- coding: utf-8 -*-
"""
Downloads the necessary NLTK models and corpora required to support
all of newspaper's features. Modify for your own needs.
"""
import nltk
import os
from dotenv import load_dotenv
load_dotenv()

download_dir = os.getenv('NLTK_DATA')

REQUIRED_CORPORA = [
    'brown',  # Required for FastNPExtractor
    'punkt',  # Required for WordTokenizer
    #'maxent_treebank_pos_tagger',  # Required for NLTKTagger
    #'movie_reviews',  # Required for NaiveBayesAnalyzer
    #'wordnet',  # Required for lemmatization and Wordnet
    'stopwords'
]

def main():
    for each in REQUIRED_CORPORA:
        print(('Downloading "{0}"'.format(each)))
        nltk.download(each, download_dir=download_dir)
    print("Finished.")

if __name__ == '__main__':
    main()
