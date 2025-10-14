import numpy as np

def read_aedat2(path, res):
    with open(path, "rb") as f:
        while True:
            pos = f.tell()
            line = f.readline()
            if not line.startswith(b"#"):
                f.seek(pos)  
                break

        data = np.fromfile(f, dtype=[("addr", ">u4"), ("ts", ">u4")])

    addr = data["addr"]
    ts = data["ts"]

    if res == (240, 180):
        x = (addr >> 0) & 0xFF
        y = (addr >> 8) & 0xFF
        p = (addr >> 16) & 0x1
    elif res == (346, 260):
        x = (addr >> 0) & 0x3FF
        y = (addr >> 10) & 0x1FF
        p = (addr >> 19) & 0x1
    elif res == (960, 540): 
        x = (addr >> 0) & 0x3FF
        y = (addr >> 10) & 0x1FF
        p = (addr >> 19) & 0x1
    else:
        raise ValueError("Unsupported resolution")

    return x, y, p, ts

x, y, p, ts = read_aedat2("/common/home/users/s/shrsabbella.2024/shape_of_motion_events/v2e/po_test/ani12_new_f.aedat", (960, 540))
print("Events:", len(ts))
print("Resolution:", x.max()+1, y.max()+1)
print("Time range:", ts.min(), ts.max())
