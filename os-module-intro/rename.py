import os

path = os.path.dirname(os.path.abspath(__file__))

for i in range(0, 100):

    os.rename(
        f"{path}/data/Day{i+1}", f"{path}/data/Tutorial{i+1}"
    )