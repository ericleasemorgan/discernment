#!/usr/bin/env bash

# originals2txt.sh - given a few configurations, extract plain text from files

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# Feburary 13, 2023 - first investigations


# configure
CONSUMERS=24
FINDS=( .pdf .docx )
ORIGINALS='./originals'
PATTERN='*.txt'
REPLACE=''
STAGING='./staging'
SUBDIRECTORIES=( 2021_09 2022_03 )
TIKA='./lib/tika-app.jar'
TXT='./txt'

# make sane
rm    -rf $STAGING
mkdir -p  $STAGING
rm    -rf $TXT
mkdir -p  $TXT

# process each subdirectory
for SUBDIRECTORY in ${SUBDIRECTORIES[@]}; do

	# make sane
	mkdir -p $STAGING/$SUBDIRECTORY
	mkdir -p $TXT/$SUBDIRECTORY
	
	# find and process all files
	find $ORIGINALS/$SUBDIRECTORY -type f | while read FILE; do
	
		# parse
		SOURCE=$( basename $FILE )
					
		# debug
		echo "$ORIGINALS/$SUBDIRECTORY/$SOURCE" >&2
		echo "$STAGING/$SUBDIRECTORY/$SOURCE"   >&2
		echo                                    >&2
		
		# do the work; copy the file to the new subdirectory
		cp "$ORIGINALS/$SUBDIRECTORY/$SOURCE" "$STAGING/$SUBDIRECTORY/$SOURCE"
		
	done
	
	# transform all the staged files to plain text
	java -jar $TIKA -numConsumers $CONSUMERS -t -i $STAGING/$SUBDIRECTORY -o $TXT/$SUBDIRECTORY

	# remove bogus file name extensions
	for FIND in ${FINDS[@]}; do rename $FIND "$REPLACE" $TXT/$SUBDIRECTORY/$PATTERN; done

done

# done, for real
exit
