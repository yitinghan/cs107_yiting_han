#!/usr/bin/env bash
for each in $(ls); do
    if [ -f "$each" ]; then 
            echo "$each $(cat $each | wc -l)"
    fi
done