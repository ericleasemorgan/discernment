#!/usr/bin/env python

# dispersion.py - given a few configurations, output a dispersion plot

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# February 27, 2023 - first cut


# configure
CARREL  = 'jegier-reflections-2023'
LEXICON = './etc/lexicon.txt'

# require
from   nltk import word_tokenize
import nltk
import rdr

# initialize
library = rdr.configuration( 'localLibrary' )
corpus  = library/CARREL/( rdr.ETC )/( rdr.CORPUS )
with open( LEXICON ) as handle : lexicon = handle.read().splitlines()

# read the text and tokenize
with open( corpus ) as handle : text = handle.read()
words = word_tokenize( text )

# do the work and done
nltk.draw.dispersion_plot( words, lexicon )
exit()
