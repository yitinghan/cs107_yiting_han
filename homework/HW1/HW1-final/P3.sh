#!/usr/bin/env bash
grep '[0-9]' apollo13.txt | wc -l > apollo_out.txt  # 1404
grep --help | grep "\-\-count" 
find ./ -maxdepth 1 -type f -name "*.py" | wc -l 
find ./ -type f ! -perm -o=rw | wc -l # file2 file4 file5
find ./ -maxdepth 1 -type d,f !  -perm -o=w -and -type d,f ! -perm -o=r | wc -l  # no read and no write file2 subdirecotry2


