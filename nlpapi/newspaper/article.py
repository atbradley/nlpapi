
import json
import os
import re

import falcon
import newspaper
import nltk
from nltk.corpus import stopwords


class ArticleResource(object):
    def __init__(self):
        self.stopwords = stopwords.words(os.getenv("STOPWORD_LANGUAGE"))
        self.nlp = os.getenv("DO_NEWSPAPER_NLP") in ('0', 'False', 'no')
        
    def enrich_article(self, article):
        article.download()
        article.parse()
        
        if self.nlp:
            article.nlp()
            
        article.download()
        
        article.tokens = nltk.word_tokenize(article.text)
        article.pos_tags = nltk.pos_tag(article.tokens)
        article.word_freqs = nltk.FreqDist(word.lower() for word in article.tokens)
        article.pos_freqs = nltk.FreqDist(word[1] for word in article.pos_tags)
        
        article.word_freqs_nosw = [word for word in article.word_freqs.items()\
                         if word[0] not in self.stopwords and not re.match('\W', word[0])]
                         
    def on_get(self, req, resp):
        outp = {}
        doc = req.params.get('a', False)
        
        if not doc:
            #TODO: Send an error message.
            return 
        
        a = newspaper.Article(doc)
        self.enrich_article(a)
        
        outp = {
            'url':              doc,
            'title':            a.title,
            'text':             a.text,
            'tokens':           a.tokens,
            'pos_tags':         a.pos_tags,
            'word_freqs':       dict(a.word_freqs),
            'word_freqs_nosw':  dict(a.word_freqs_nosw)
        }
        
        if self.nlp:
            outp['summary'] = a.summary
            outp['keywords'] = a.keywords
        
        # Create a JSON representation of the resource
        resp.body = json.dumps(outp, ensure_ascii=False)