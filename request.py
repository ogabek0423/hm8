import multiprocessing
import requests

def make_request(url):
    response = requests.get(url)
    with open("", "w") as file:
        file.write(response.text)
    print(f"Response from {url}: {response.text}")

def main():
    urls = ["https://kun.uz/", "https://lms.tuit.uz/"]

    # Create processes
    processes = [multiprocessing.Process(target=make_request, args=(url,)) for url in urls]

    # Start processes
    for process in processes:
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("Main process continues execution.")


if __name__ == "__main__":
    main()
