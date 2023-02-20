#!/usr/bin/env bash

# originals2txt.sh - given a few configurations, extract plain text from files

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# Feburary 13, 2023 - first investigations


# configure
SUBDIRECTORIES=( 2021_09 2022_03 )
TXT='./txt'
REFLECTIONS='./reflections'
PREFIX='reflection_'

# make sane
rm -rf $REFLECTIONS
mkdir $REFLECTIONS

# process each subdirectory
for SUBDIRECTORY in ${SUBDIRECTORIES[@]}; do
	
	# re-initialize
	INDEX=0
	
	# find and process all files
	find $TXT/$SUBDIRECTORY -type f | while read FILE; do
	
		# parse
		SOURCE=$( basename $FILE )
		EXTENSION="${SOURCE##*.}"
		
		# increment
		let INDEX=INDEX+1
		
		# create new name for the file
		TARGET=$PREFIX$( printf %05d $INDEX )
		TARGET=$REFLECTIONS/$TARGET-$SUBDIRECTORY.$EXTENSION
		
		# debug
		echo "$FILE"   >&2
		echo "$TARGET" >&2
		echo           >&2
		
		# do the work; copy the file to the new subdirectory
		cp $FILE $TARGET
		
	done
	
done

# done, for real
exit
