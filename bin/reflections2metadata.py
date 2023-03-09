#!/usr/bin/env python

# reflections2metadata.py - given a few configurations, output Reader metadata file
# usage: ./bin/reflections2metadata.py > ./reflections/metadata.csv


# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# Feburary 27, 2023 - first cut


# configure
REFLECTIONS = './reflections'
PATTERN     = '*.txt'
COLUMNS     = [ 'file', 'date' ]

# require
from pathlib import Path
import pandas as pd

# process each reflection; create a list of metadata values
metadata    = []
reflections = Path( REFLECTIONS )
for reflection in reflections.glob( PATTERN ) :

	# parse
	file = reflection.name
	date = file.split( '-' )[ 1 ].split( '_' )[ 0 ]
	
	# update
	metadata.append( [ file, date ] )

# convert the metadata to a dataframe, output, and done
metadata = pd.DataFrame( metadata, columns=COLUMNS )
print( metadata.to_csv( index=False ) )
exit()

