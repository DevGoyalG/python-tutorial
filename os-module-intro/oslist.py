import os

path = os.path.dirname(os.path.abspath(__file__))

folders = os.listdir(f"{path}/data")

for folder in folders:
    print(folder)
    print(os.listdir(f"{path}/data/{folder}"))