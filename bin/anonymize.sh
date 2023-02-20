#!/usr/bin/env bash

# anonymize.sh - given a few configurations, remove name from bunches o' files

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# February 14, 2023 - first cut; never done this in bash
# February 16, 2023 - finally got it to work


# configure
FILES=( ./etc/names-2022_spring.txt ./etc/names-2021_fall.txt )
TXT='./txt'

# initialize
NAMES=''

# process all files of names; get all names
for FILE in ${FILES[@]}; do NAMES=$NAMES$( cat $FILE ); done

# process each name
while IFS= read -r PARTS; do

    # re-initialize
    NAME=''
    	
    # process each part of the name; create a real name
    for PART in $PARTS; do
    	
    	# normalize and update
    	NORMALIZED=$( echo "${PART:0:1}" | tr [[:lower:]] [[:upper:]] )${PART:1}
    	NAME="$NORMALIZED $NAME"
   
	done
    
    # remove the trailing space; dumb
    NAME=$( echo $NAME | sed s/\w$// )
    
	# create a key
	KEY=$( echo $PARTS | tr -d ' ' )

    # debug
    echo $KEY  >&2
    echo $NAME >&2
    find $TXT -name "*$KEY*"
    
    # do the work; efficient, mostly
    find $TXT -name "*$KEY*" | xargs sed -i "s/${NAME}//g"
		
done <<< $NAMES

# fini
exit
