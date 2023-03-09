#!/usr/bin/env python

# carrel2sentences.py - given a few configuration, output a set of sentences


# configure
CARREL  = 'jegier-reflections-2023'
LEXICON = './etc/lexicon-stems.txt'

# require
from   nltk.tokenize import sent_tokenize
import rdr
import sys

# initialize
library = rdr.configuration( 'localLibrary' )
corpus  = library/CARREL/( rdr.ETC)/( rdr.CORPUS )
with open( corpus )  as handle : corpus  = handle.read()
with open( LEXICON ) as handle : lexicon = handle.read().splitlines()

# get and process all sentences
sys.stderr.write( "Tokenizing corpus into sentences.\n" )
sentences = sent_tokenize( corpus )
for sentence in sentences :

	# process each lexicon stem
	for stem in lexicon :
	
		# output, conditionally
		if sentence.count( stem ) > 0 : print( sentence, '\n' )

# done
exit()