
import h5py
import numpy as np
import sys

def inspect_h5(h5_path):
    with h5py.File(h5_path, "r") as f:
        events = f["events"][:]  
        
        t = events[:,0]
        x = events[:,1]
        y = events[:,2]
        p = events[:,3]

        width  = int(x.max()) + 1
        height = int(y.max()) + 1
        duration = (t.max() - t.min()) / 1e6 

        print(f"{h5_path}")
        print(f"  Events:     {len(events):,}")
        print(f"  Resolution: {width} x {height}")
        print(f"  Duration:   {duration:.2f} seconds")

if __name__ == "__main__":
    for path in sys.argv[1:]:
        inspect_h5(path)
