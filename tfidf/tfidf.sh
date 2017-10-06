#!/bin/bash

WCDIR=/home/tfidf
STREAMINGJAR=share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar

bin/hadoop jar $STREAMINGJAR                        \
    -files   $WCDIR/wcMap.py,$WCDIR/wcReduce.py \
    -mapper  $WCDIR/wcMap.py                      \
    -reducer $WCDIR/wcReduce.py                   \
    -input   Gutenberg/'*'                          \
    -output  Output