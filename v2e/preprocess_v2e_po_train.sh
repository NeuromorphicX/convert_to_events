#!/bin/bash
INPUT_DIR="/common/home/users/s/shrsabbella.2024/scratchDirectory/train"
OUTPUT_DIR="/common/home/users/s/shrsabbella.2024/scratchDirectory/train/po_train"

mkdir -p "$OUTPUT_DIR"

for f in "$INPUT_DIR"/*.mp4; do
  fname=$(basename "$f" .mp4)
  echo "Processing $fname..."

  python v2e.py \
    --input "$f" \
    --output_folder "$OUTPUT_DIR" \
    --output_width 960 \
    --output_height 540 \
    --dvs_h5 "${OUTPUT_DIR}/${fname}.h5" \
    --pos_thres 0.25 \
    --neg_thres 0.25 \
    --no_preview \
    --disable_slomo \
    --overwrite

  python convert_h5_to_npz.py "${OUTPUT_DIR}/${fname}.h5"

  echo "Finished $fname."
done

find "$OUTPUT_DIR" -maxdepth 1 -type f -name "*.npz" -ls
