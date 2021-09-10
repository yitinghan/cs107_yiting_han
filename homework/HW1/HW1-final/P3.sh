#!/bin/bash
grep '[0-9]' apollo13.txt | wc -l > apollo_out.txt  # 1404
# Part C 
find ./ -maxdepth 1 -type f -name "*.py" | wc -l 
# subdirectories?
