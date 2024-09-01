import queue
from threading import  Thread
from time import sleep
from random import randint

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        wait_1 = randint(3, 10)
        sleep(wait_1)


class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        n = 1
        guest_1 = list(guests)
        for i in range(len(self.tables)):
            Table(n).guest =guest_1[i]
            print(f'{guest_1[i]} сел(-а) за стол номер {n}')
            n += 1
        else:
            self.queue.put(i)
            print(f'{guest_1[i]} в очереди')

    def discuss_guests(self):
        ...


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
