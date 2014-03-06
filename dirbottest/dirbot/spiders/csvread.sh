#!/bin/bash
while IFS=, read col1 col2
do
    echo "I got:$col1"
done < items22.csv
