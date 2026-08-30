import os

path = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists(f"{path}/data"):
    os.mkdir(f"{path}/data")

for i in range(0, 100):
    os.mkdir(f"{path}/data/Day{i+1}")
    os.mkdir