#!/usr/bin/env bash
# File: exercise_1.sh
# Created：Mon Sept 13 2021
# Coder: Yiting Han
read -r -p "Please select a file to commit: " FILE 
git add $FILE
git status
read -r -p "Do you wish to continue? (Y or N) " RESPONSE
if [ "$RESPONSE" == "Y" ]; then
    read -r -p "Please enter a commit message: " MESSAGE 
    git commit -m "$MESSAGE"
    git status
    read -r -p "Do you wish to continue? (Y or N) " ANSWER
    if [ "$ANSWER" == "Y" ]; then 
        git push
    else 
        exit 1
    fi
else 
    exit 1
fi




