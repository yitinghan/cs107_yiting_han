#!/usr/bin/env bash
grep '[0-9]' apollo13.txt | wc -l > apollo_out.txt  # 1404
grep --help | grep "\-\-count" 
find ./ -maxdepth 1 -type f -name "*.py" | wc -l 
find ./ -type f ! -perm -o=rw | wc -l # file2 file4 file5
find ./ -maxdepth 1 ! -perm -o=rw -type f -or ! -perm -o=rw -type d | wc -l # file2 subdirecotry2


