#!/usr/bin/env python

# filenames2metadata.py - given a few configurations, output a CSV file for the Reader

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# Feburary 15, 2023 - first investigations
# Feburary 16, 2023 - tweeked configurations


# configure
TXT     = './reflections'
PATTERN = '*.txt'
COLUMNS = [ 'file', 'title', 'date' ]

# require
import pandas as pd
from pathlib import Path
import sys

# initialize
txt      = Path( TXT )
metadata = []

# process each file in the given directory
for file in txt.glob( PATTERN ) :

	# parse
	name  = file.name
	parts = name.replace( '.txt', '' )
	parts = parts.split( '-' )
	
	# parse some more
	title = parts[ 0 ]
	date  = parts[ 1 ]
	
	# create a record, and update the list of records
	record = [ name, title, date ]
	metadata.append( record )
	
# create a dataframe, output, and done
metadata = pd.DataFrame( data=metadata, columns=COLUMNS )
print( metadata.to_csv( index=False ) )
exit()
