import threading

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        print(f"Data read from  {file_path}: \n {data}")

def main():
    file_path1 = 'file1txt'
    file_path2 = 'file2txt'
    file_path3 = 'file3txt'
    file_path4 = 'file4txt'
    file_path5 = 'file5txt'

    thread1 = threading.Thread(target=read_file, args=(file_path1,))
    thread2 = threading.Thread(target=read_file, args=(file_path2,))
    thread3 = threading.Thread(target=read_file, args=(file_path3,))
    thread4 = threading.Thread(target=read_file, args=(file_path4,))
    thread5 = threading.Thread(target=read_file, args=(file_path5,))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()

    print("Main thread continues execution.")

if __name__ == "__main__":
    main()