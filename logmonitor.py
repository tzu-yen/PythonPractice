import time
def tail(f):
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line
