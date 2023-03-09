#!/usr/bin/env bash

# collocations.sh - a front-end to collocations.py
# usage: ./bin/collocations.sh > ./tmp/collocations.tsv

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# February 27, 2023 - first investigations


# configure
COLLOCATIONS='./bin/collocations.py'
HEADER="source\ttarget\tweight"

# output the header, do the work, and done
echo -e $HEADER
$COLLOCATIONS
exit
