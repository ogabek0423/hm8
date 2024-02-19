import multiprocessing
import time


def write_to_file(file_path, data):
    time.sleep(3)
    with open(file_path, 'w') as file:
        file.write(data+"\n")
        print(f"Data written to {file_path}")

def main():
    file_path1 = 'filtxt'
    file_path2 = 'file2xt'
    file_path3 = 'file3xt'
    file_path4 = 'file'
    file_path5 = 'file'

    data1 = '1-fayl malumot'
    data2 = '2-fayl malumot'
    data3 = "3-fayl malumot"
    data4 = "4-fayl malumot"
    data5 = "5-fayl malumot"


    process1 = multiprocessing.Process(target=write_to_file, args=(file_path1, data1))
    process2 = multiprocessing.Process(target=write_to_file, args=(file_path2, data2))
    process3 = multiprocessing.Process(target=write_to_file, args=(file_path3, data3))
    process4 = multiprocessing.Process(target=write_to_file, args=(file_path4, data4))
    process5 = multiprocessing.Process(target=write_to_file, args=(file_path5, data5))

    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()

    print("Main process continues execution.")

if __name__ == "__main__":
    main()
