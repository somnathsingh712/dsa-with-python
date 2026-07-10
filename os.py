import os

def disk(path):
    total=os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.path.listdir(path):
            childpath=os.path.join(path,filename)
            total+=disk(childpath)

    return total

print(disk("D:\pythondsa\chess.py"))