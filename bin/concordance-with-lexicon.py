#!/usr/bin/env python

# concordance-with-lexicon.py - given a few configurations, concordance a carrel


# configure
CARREL  = 'jegier-reflections-2023'
LEXICON = './etc/lexicon.txt'
WIDTH   = 60

# require
import rdr

# initialize
with open( LEXICON ) as handle : lexicon = handle.read().splitlines()

# process each word in the given lexicon
for word in lexicon :

	# do the work and output
	for line in rdr.concordance( CARREL, query=word, width=WIDTH ) : print( line )
	
# done; too easy
exit()
