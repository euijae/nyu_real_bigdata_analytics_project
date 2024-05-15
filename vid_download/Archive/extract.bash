#!/bin/bash

# Name of the input and output files
inputFile="input.txt"
outputFile="output.csv"

# Create or clear the outputFile
> "$outputFile"

# Add CSV headers
echo "game_id,game_date" >> "$outputFile"

# Read the inputFile line by line
while IFS= read -r line; do
    # Check if the line contains game_id
    if [[ "$line" =~ game_id ]]; then
        # Extract game_id
        gameId="${line#*: }"
    fi
    
    # Check if the line contains game_date
    if [[ "$line" =~ game_date ]]; then
        # Extract game_date
        gameDate="${line#*: }"
        # Write the pair to the outputFile
        echo "$gameId,$gameDate" >> "$outputFile"
    fi
done < "$inputFile"
