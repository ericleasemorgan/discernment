#!/usr/bin/env python


# configure
CARREL  = 'jegier-reflections-2023'
LEXICON = './etc/lexicon-vectors.txt'
TOPN    = 128
HEADER  = [ 'source', 'target', 'weight' ]

# require
import rdr

# initialize
with open( LEXICON ) as handle: lexicon = handle.read().splitlines()
rdr.checkForSemanticIndex( CARREL )

# start the output
print( '\t'.join( HEADER ) )

# process each word in the lexicon
for word in lexicon :

	# do the work and process each result
	results = rdr.word2vec( CARREL, type='similarity', query=word, topn=TOPN ).splitlines()
	for result in results :

		# parse and output
		( similarity, score ) = result.split( '\t' )
		print( '\t'.join( [ word, similarity, str( score ) ] ) )

# done
exit()
