#!/usr/bin/env python

# bigrams-with-lexicon.py - given a few configurations, concordance a carrel


# configure
CARREL = 'jegier-reflections-2023'
STEMS  = './etc/lexicon-stems.txt'

# require
import rdr

# initialize
with open( STEMS ) as handle : stems = handle.read().splitlines()

query = '|'.join( stems )
rdr.ngrams( CARREL, size=2, query=query, count=True, wordcloud=True )