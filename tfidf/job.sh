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
	-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
	-D stream.map.output.field.separator=# 			\
    -D stream.num.map.output.key.fields=4               \
    -D mapreduce.map.output.key.field.separator=#      \
    -D mapreduce.partition.keycomparator.options="-k1,1 -k2,2nr" \
    -D mapreduce.job.reduces=1					\
    -files   $WCDIR/wdMap.py,$WCDIR/wdReduce.py \
    -mapper  $WCDIR/wdMap.py                        \
    -reducer $WCDIR/wdReduce.py                     \
    -input   Word/'*'                                   \
    -output  Out