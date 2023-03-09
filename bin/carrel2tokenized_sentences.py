#!/usr/bin/env python


# configure
CARREL    = 'jegier-reflections-2023'
SENTENCES = 'reader.tok'
SUBSTRING = 'discernment'

# require
import rdr

# initialize
library   = rdr.configuration( 'localLibrary' )
sentences = library/CARREL/( rdr.ETC)/SENTENCES

# create list of tokenized sentences (./etc/reader.tok); very poorly implemented!
rdr.checkForSemanticIndex( CARREL )

# get and process all sentences
sentences = rdr.Sentences( sentences )
for sentence in sentences :

	# check for the given word
	if sentence.count( SUBSTRING ) > 0 :
	
		# output
		print( sentence )

# done
exit()