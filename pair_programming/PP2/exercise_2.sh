#!/usr/bin/env bash
# File: exercise_2.sh
# Created：Mon Sept 13 2021
# Coder: Yiting Han
# Sharer: Nadine Lee
# Listener: Kishan Venkataramu

for each in $(ls); do 
    if [ -x "$each" ]; then
        echo $each
    fi
done


