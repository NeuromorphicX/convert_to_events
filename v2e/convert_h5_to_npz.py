import sys, os, h5py, numpy as np, pathlib

h5_path = sys.argv[1]
stem = str(pathlib.Path(h5_path).with_suffix(''))
npz_path = f"{stem}.npz"

with h5py.File(h5_path, "r") as f:
    ds = f[list(f.keys())[0]]
    arr = ds[()]  # load whole dataset

if arr.dtype.names is None:
    t = arr[:, 0]
    x = arr[:, 1]
    y = arr[:, 2]
    p = arr[:, 3]
else:
    names = arr.dtype.names
    if "t" in names:
        t = arr["t"]
    elif "ts" in names:
        t = arr["ts"]
    else:
        raise RuntimeError(f"No timestamp field in {names}")
    x = arr["x"]; y = arr["y"]; p = arr["p"]

x = x.astype(np.uint16)
y = y.astype(np.uint16)
p = p.astype(np.uint8)

t = t.astype(np.float64)
t0 = float(t[0]) if t.size > 0 else 0.0
t_us = np.round((t - t0) * 1e6).astype(np.uint32)

if t_us.size > 0:
    dt = np.empty_like(t_us)
    dt[0] = t_us[0]
    dt[1:] = np.diff(t_us)
else:
    dt = t_us

np.savez_compressed(
    npz_path,
    dt=dt, x=x, y=y, p=p,
    meta=np.array([960, 540, t0], dtype=np.float64)
)

os.remove(h5_path)
print(f"wrote {npz_path} and deleted {h5_path}")
