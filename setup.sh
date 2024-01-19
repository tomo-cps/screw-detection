#!/bin/bash

DATA_DIR="data"

mkdir -p "$DATA_DIR/train/images" "$DATA_DIR/train/labels"
mkdir -p "$DATA_DIR/valid/images" "$DATA_DIR/valid/labels"

move_files() {
  local filetype=$1
  local counter=0
  local files=( $(ls $DATA_DIR/*.$filetype) )

  for file in "${files[@]}"; do
    local filename=$(basename -- "$file")
    local number=$(echo $filename | grep -o -E '[0-9]+' | head -1 )

    if [[ $number -lt 8 ]]; then
      mv "$file" "$DATA_DIR/train/$2"
    else
      mv "$file" "$DATA_DIR/valid/$2"
    fi
  done
}

# Move the images and labels
move_files "jpg" "images"
move_files "txt" "labels"
move_files "xml" "labels"
