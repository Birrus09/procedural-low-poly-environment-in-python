import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))


import proc_noise

file1 = open("Worlds/World1.txt", "w")

for i in range(108*72):
    file1.write(str(proc_noise.Noise1[i]) + "\n")

file1.close()
