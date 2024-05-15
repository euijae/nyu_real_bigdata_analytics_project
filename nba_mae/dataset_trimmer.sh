#!/bin/bash

# Define the root directory of your dataset
root_dir="./dataset"

# Define the directory where the processed files will be saved
output_dir="./trimmed_dataset"

# Create the output directory if it doesn't exist
mkdir -p "$output_dir"

# Function to process each video file
process_video() {
    local input_path="$1"
    local output_path="$2"
    
    # Get the duration of the video in seconds
    duration=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$input_path")
    
    # Calculate the start time for the last 5 seconds
    start_time=$(echo "$duration - 5" | bc)
    
    # Use ffmpeg to clip the last 5 seconds of the video
    ffmpeg -ss "$start_time" -i "$input_path" -t 5 -c copy "$output_path"
}

# Export the function so it can be used in subshells
export -f process_video

# Use find to iterate over all video files and process them
find "$root_dir" -type f -name "*.mp4" -exec bash -c 'process_video "$0" "${0/#$root_dir/$output_dir}"' {} \;
