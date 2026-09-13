# multiprocessing in python - multiple processes run concurrently.
#  module in Python allows you to run multiple independent processes concurrently, enabling true parallelism.


import multiprocessing
import requests
import os


def downloadFile(url, name):
    print(f"Started downloading {name}")

    response = requests.get(url)
    response.raise_for_status()

    with open(f"files/file{name}.jpg", "wb") as f:
        f.write(response.content)

    print(f"Finished downloading {name}")


if __name__ == "__main__":
    os.makedirs("files", exist_ok=True)

    url = "https://picsum.photos/200/300"

    processes = []

    for i in range(5):
        p = multiprocessing.Process(
            target=downloadFile,
            args=(url, i)
        )
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print("All downloads completed!")