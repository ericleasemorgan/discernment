#!/usr/bin/env bash

# list-names.sh - given a directory, output all the authors of the contained files
# usage: ./list-names.sh <directory> | sort | uniq


if [[ -z $1 ]]; then
	echo "Usage: $0 <directory" >&2
	exit
fi

DIRECTORY=$1

find $DIRECTORY -type f | while read FILE; do

	BASENAME=$( basename $FILE )
	AUTHOR=$( echo $BASENAME | cut -d '_' -f1 )
	echo -e "$FILE\t$AUTHOR"
	
done
exit
