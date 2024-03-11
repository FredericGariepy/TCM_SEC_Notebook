#!/bin/bash
length=$1
width=$2
height=$3
volume=$(echo $1 * $2 * $3 | bc) #bc is a command-line calculator that handles floating-point operation.
echo $volume
