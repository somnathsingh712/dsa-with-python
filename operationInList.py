# YOU WANT TO KEEP A LIMITED HISTORY OF THE LAST FEW ITEMS SEEN DURING ITERATION OR DURING SOME OTHER KIND OD PROCESSING

from collections import deque

def search(lines, pattern, history=5):
    prevlines = deque(maxlen=history)

    for line in lines:
        if pattern in line:
            yield line, prevlines
        prevlines.append(line)