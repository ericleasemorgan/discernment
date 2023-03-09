#!/usr/bin/env python

# carrel2sentences.py - given a few configuration, output a set of sentences


# configure
CARREL = 'jegier-reflections-2023'
STEM   = 'discern'

# require
from   nltk.tokenize import sent_tokenize
import rdr
import sys

# initialize
library = rdr.configuration( 'localLibrary' )
corpus  = library/CARREL/( rdr.ETC)/( rdr.CORPUS )
with open( corpus )  as handle : corpus  = handle.read()

# get and process all sentences
sys.stderr.write( "Tokenizing corpus into sentences.\n" )
sentences = sent_tokenize( corpus )
for sentence in sentences :
	
		# output, conditionally
		if sentence.count( STEM ) > 0 : print( sentence, '\n' )

# done
exit()