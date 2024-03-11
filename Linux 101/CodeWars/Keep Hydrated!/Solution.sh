#!/bin/bash
time=$1
liters=$( echo $1 * 0.5 | bc ) #use command line calculator 'bc'.
result=$(echo $liters | awk -F '.' '{print $1}') # Use awk to split & take first collumn element.
echo "${result:-0}" # :- is a default value assignment operator, if empty, 0 is the default value.
