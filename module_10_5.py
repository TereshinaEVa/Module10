import multiprocessing
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        string_file = f.readlines()
        for i in string_file:
            all_data.append(i)

"""start_time = datetime.now()

filenames = [f'./Files/file {number}.txt' for number in range(1,5)]
for name in filenames:
    read_info(name)
end_time = datetime.now()
print(end_time - start_time)"""

if __name__ == '__main__':
    start_time = datetime.now()
    with multiprocessing.Pool(processes=2) as pool:
        filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]
        pool.map(read_info, filenames)
    end_time = datetime.now()

    print(end_time - start_time)

#lines: 0:00:25.380893
#multiprocessing: 0:00:11.626563 (у меня комп слабенький, поэтому только при использовании двух процессов имеет смысл)
