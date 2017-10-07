#!/bin/bash

WCDIR=/home/tfidf
STREAMINGJAR=share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar

printf "WORD COUNT MAP-REDUCE\n\n"
bin/hadoop jar $STREAMINGJAR                        \
    -files   $WCDIR/wcMap.py,$WCDIR/wcReduce.py \
    -mapper  $WCDIR/wcMap.py                      \
    -reducer $WCDIR/wcReduce.py                   \
    -input   Gutenberg/'*'                          \
    -output  Word

printf "\nTFIDF MAP-REDUCE\n\n"
bin/hadoop jar $STREAMINGJAR                            \
    -files   $WCDIR/wdMap.py,$WCDIR/wdReduce.py \
    -mapper  $WCDIR/wdMap.py                        \
    -reducer $WCDIR/wdReduce.py                     \
    -input   Word/'*'                                   \
    -output  Output