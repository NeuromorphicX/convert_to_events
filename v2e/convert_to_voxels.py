#!/usr/bin/env python3
import os
import h5py
import numpy as np
from tqdm import tqdm

# ====== USER PARAMETERS ======
fps = 24
frames_in_between = 5  # → effective 144 fps
input_path = "/common/home/users/s/shrsabbella.2024/scratchDirectory/test/h5sample/anima5_s.h5"
output_dir = "/common/home/users/s/shrsabbella.2024/scratchDirectory/test/h5sample/voxel_rel"
os.makedirs(output_dir, exist_ok=True)

# ====== LOAD EVENTS ======
print(f"Reading {input_path} ...")
with h5py.File(input_path, "r") as f:
    ds = f[list(f.keys())[0]]
    arr = ds[()]
    if arr.dtype.names is None:
        t, x, y, p = arr[:, 0], arr[:, 1], arr[:, 2], arr[:, 3]
    else:
        t = arr["t"] if "t" in arr.dtype.names else arr["ts"]
        x, y, p = arr["x"], arr["y"], arr["p"]

t = t.astype(np.float64)
x = x.astype(np.uint16)
y = y.astype(np.uint16)
p = p.astype(np.uint8)
print(f"Loaded {len(t):,} events.")

# ====== NORMALIZE TIMESTAMPS ======
# make timestamps relative (start at 0)
t = t - t.min()
duration = t.max() - t.min()

# compute total number of frames purely by desired fps
effective_fps = fps * (frames_in_between + 1)
sub_interval = duration / (effective_fps * (duration / 1.0))  # ensure evenly spaced
t_bins = np.linspace(t.min(), t.max(), int(np.ceil(duration * effective_fps)) + 1)
num_bins = len(t_bins) - 1
print(f"Generating {num_bins} frames at {effective_fps:.1f} fps (auto-normalized)")

# ====== SORT EVENTS ======
sort_idx = np.argsort(t)
t, x, y, p = t[sort_idx], x[sort_idx], y[sort_idx], p[sort_idx]
width, height = int(np.max(x)) + 1, int(np.max(y)) + 1

# ====== FRAME GENERATION ======
start_idx = 0
basename = os.path.splitext(os.path.basename(input_path))[0]

for seg_idx in tqdm(range(num_bins), desc="Generating frames", ncols=80):
    t1 = t_bins[seg_idx + 1]
    end_idx = np.searchsorted(t, t1, side="left")

    if end_idx == start_idx:
        frame = np.zeros((height, width), np.float32)
    else:
        xv, yv, pv = x[start_idx:end_idx], y[start_idx:end_idx], p[start_idx:end_idx]
        weights = np.where(pv > 0, 1.0, -1.0)
        flat_idx = yv * width + xv
        frame = np.bincount(flat_idx, weights=weights, minlength=width * height).reshape(height, width)
    start_idx = end_idx

    np.save(os.path.join(output_dir, f"{basename}_frame_{seg_idx:06d}.npy"), frame)

print(f"✅ Done! {num_bins} frames saved to {output_dir}")
