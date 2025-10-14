import numpy as np, sys

npz_path = sys.argv[1]
E = np.load(npz_path)

dt = E["dt"]   
x  = E["x"]   
y  = E["y"]  
p  = E["p"]   
meta = E["meta"]

t_us = np.cumsum(dt, dtype=np.uint64)  
t = t_us / 1e6 + meta[2]            

print("=== Verification for", npz_path, "===")
print("Events:", len(t))
print("Resolution:", int(meta[0]), "x", int(meta[1]))
print("Time range: %.6f s → %.6f s (%.3f s span)" % (t.min(), t.max(), t.max()-t.min()))
print("x: [%d, %d], y: [%d, %d]" % (x.min(), x.max(), y.min(), y.max()))
print("p polarity values:", np.unique(p))
