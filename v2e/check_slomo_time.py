import h5py
import numpy as np

def inspect_h5(h5_path, n=5):
    with h5py.File(h5_path, "r") as f:
        obj = f["events"]
        if isinstance(obj, h5py.Group):
            t = np.array(obj["t"])
            x = np.array(obj["x"])
            y = np.array(obj["y"])
            p = np.array(obj["p"])
        else:  # dataset shape (N,4)
            events = obj[:]
            t, x, y, p = events[:,0], events[:,1], events[:,2], events[:,3]

    print(f"Total events: {len(t):,}")
    print("\nSample events (first few):")
    for i in range(min(n, len(t))):
        print(f"{i}: t={t[i]:.6f}, x={int(x[i])}, y={int(y[i])}, p={int(p[i])}")
        
    # for i in range(0, 1000):
    #     print(f"{i}: t={t[i]:.6f}")

    return t, x, y, p


# Example usage:
h5_path = "/common/home/users/s/shrsabbella.2024/scratchDirectory/test/po_test_slomo_3/anima5_s.h5"
t, x, y, p = inspect_h5(h5_path)
print(x.max()+1, y.max()+1)
