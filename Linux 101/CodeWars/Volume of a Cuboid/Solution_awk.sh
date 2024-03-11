#!/bin/bash
length=$1
width=$2
height=$3

volume=$(awk -v l="$length" -v w="$width" -v h="$height" 'BEGIN { print l * w * h }')

echo $volume
