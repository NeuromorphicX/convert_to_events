#!/bin/bash
set -euo pipefail

INPUT_DIR="/common/home/users/s/shrsabbella.2024/scratchDirectory/test/sample"
OUTPUT_DIR="/common/home/users/s/shrsabbella.2024/scratchDirectory/test/po_test_slomo"

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
    --vid_orig None \
    --batch_size 8 \
    --vid_slomo "${OUTPUT_DIR}/${fname}.avi" \
    --overwrite

  # python convert_h5_to_npz.py "${OUTPUT_DIR}/${fname}.h5"

  echo "Finished $fname."
done

# find "$OUTPUT_DIR" -maxdepth 1 -type f -name "*.npz" -ls
# --avi_frame_rate 24 \
# --dvs_exposure duration 0.0417 \