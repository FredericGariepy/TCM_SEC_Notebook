#!/bin/bash
dad_years_old=$1
son_years_old=$2
years=$(( ( $2 * 2 ) - $1 )) # solving linear equation
echo $((years < 0 ? -years : years)) # echo Absolute value
