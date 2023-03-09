#!/usr/bin/env python

# lexicon2frequencies.py - given a few configurations, output a stream of CSV denoting frequencies

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# February 27, 2023 - first cut; not elegant


# configure
CARREL  = 'jegier-reflections-2023'
LEXICON = './etc/lexicon.txt'
COLUMNS = [ 'word', 'frequency' ]

# require
import rdr
import pandas as pd

# initialize
with open ( LEXICON ) as handle : lexicon = handle.read().splitlines()

# process each word in the lexicon; count & tabluate lexicon frequencies
frequencies = []
for word in lexicon :
	
	# find and process the given words and their likenesses
	results = rdr.ngrams( CARREL, size=1, query=word, count=True ).splitlines()
	for result in results :
	
		# update, conditionally
		if result not in frequencies : frequencies.append( result )
		
# stuff the result into a dataframe, coerce the frequency column, and sum it
frequencies                = [ frequency.split( '\t' ) for frequency in frequencies ]
frequencies                = pd.DataFrame( frequencies, columns=COLUMNS )
frequencies[ 'frequency' ] = pd.to_numeric( frequencies[ 'frequency' ] )
total_lexicon              = frequencies[ 'frequency' ].sum()

# count & tabulate all words in the corps, sans stop words
corpus = rdr.ngrams( CARREL, count=True ).splitlines()
corpus = [ word.split( '\t' ) for word in corpus ]

# stuff the result into a dataframe, coerce the frequencies column, and sum
corpus                = pd.DataFrame( corpus, columns=COLUMNS )
corpus[ 'frequency' ] = pd.to_numeric( corpus[ 'frequency' ] )
total_corpus          = corpus[ 'frequency' ].sum()

# calcuate the difference between total words and lexicon words
difference = total_corpus - total_lexicon

# update the frequencies, output, and done
frequencies.loc[ len( frequencies.index ) ] = [ 'non-lexicon words', int( difference ) ] 
print( frequencies.to_csv( index=False ) )
exit()


