# Video Conversion Scripts

This project contains `.sh` files for converting videos from the `INPUT_DIR` to the specified output directory.

## Usage

1. Place your video files in the `INPUT_DIR`.
2. Run the appropriate `.sh` script to start the conversion process.
3. The script converts the input videos into .h5 files, which are heavy [make sure you have enough space] [adjust the pos_thres, neg_thres to reduce the size].
4. By default, I have converted .h5 file into .npz to reduce the size, can comment the line  `python convert_h5_to_npz.py "${OUTPUT_DIR}/${fname}.h5"` if only .h5 is needed [ .aedat is not available for 960x540 resolution. ]
5. Converted videos will be saved in the output directory.

## Example

```bash
chmod +x preprocess_v2e_po_train.sh
./preprocess_v2e_po_train.sh 
```

## Requirements

- Bash shell
- [V2E](https://github.com/SensorsINI/v2e) installed
- Required video conversion tools (e.g., ffmpeg)

