#!/bin/bash

value() {
    local arg=$1
    if [ "$arg" -ge 0 ]; then
        echo 1
    else
        echo 0
    fi
}
x=$(value "$1")
y=$(value "$2")

if [ "$x" -eq 1 ] && [ "$y" -eq 1 ]; then
  echo 1
elif [ "$x" -eq 0 ] && [ "$y" -eq 1 ]; then
  echo 2
elif [ "$x" -eq 0 ] && [ "$y" -eq 0 ]; then
  echo 3
else
  echo 4
fi
