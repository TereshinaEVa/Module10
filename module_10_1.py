from threading import Thread

import requests
from time import sleep
from datetime import datetime

def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for n in range(1, word_count + 1):
            f.write(f'Какое-то слово № {n}' + '\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
wite_words(10, 'examle1.txt')
wite_words(30, 'examle2.txt')
wite_words(200, 'examle3.txt')
wite_words(100, 'examle4.txt')
time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}')

time_start = datetime.now()
file_5 = Thread(target=wite_words, args=(10, 'examle5.txt'))
file_6 = Thread(target=wite_words, args=(30, 'examle6.txt'))
file_7 = Thread(target=wite_words, args=(200, 'examle7.txt'))
file_8 = Thread(target=wite_words, args=(100, 'examle8.txt'))

file_5.start()
file_6.start()
file_7.start()
file_8.start()

file_5.join()
file_6.join()
file_7.join()
file_8.join()
time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}')