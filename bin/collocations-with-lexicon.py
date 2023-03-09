#!/usr/bin/env python

# collocations.py = given a few configurations, output a list of collocations

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# February 27, 2023 - first investigations; fun, finally


# configure
CARREL  = 'jegier-reflections-2023'
LEXICON = './etc/lexicon.txt'
WINDOW  = 12

# require
from nltk              import word_tokenize
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
import rdr
import sys

# get all words in the given carrel; read the corpus
sys.stderr.write( "Step #1 of 5: Reading corpus\n" )
library = rdr.configuration( 'localLibrary' )
corpus  = library/CARREL/( rdr.ETC )/( rdr.CORPUS )
with open( corpus ) as handle : corpus = word_tokenize( handle.read() )

# get stopwords
sys.stderr.write( "Step #2 of 5: Reading stop words\n" )
stopwords = library/CARREL/( rdr.ETC )/( rdr.STOPWORDS )
with open( stopwords ) as handle : stopwords = handle.read().splitlines()

# get the lexicon
sys.stderr.write( "Step #3 of 5: Reading lexicon\n" )
with open( LEXICON ) as handle : lexicon = handle.read().splitlines()

# create a finder object and remove stopwords from it
sys.stderr.write( "Step #4 of 5: Modeling\n" )
finder = BigramCollocationFinder.from_words( corpus, window_size=WINDOW )
finder.apply_word_filter( lambda word : not word.isalpha() or word in stopwords )

# score the bigrams (collocations) and process each one
sys.stderr.write( "Step #5 of 5: Reading model\n" )
collocations = finder.score_ngrams( BigramAssocMeasures().likelihood_ratio  )
for collocation in collocations :

	# parse
	terms = collocation[ 0 ]
	score = collocation[ 1 ]
	
	# parse some more
	first  = terms[ 0 ]
	second = terms[ 1 ]
	
	# check for lexicon term
	if ( first in lexicon ) or ( second in lexicon ) :
	
		# output
		print( '\t'.join( [ first, second, str( score ) ]) )

# done
exit()

