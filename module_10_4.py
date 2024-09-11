import queue
from threading import Thread
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
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
         for guest in guests:
            for table_seat in self.tables:
                if table_seat.guest is None:
                    guest.start()
                    table_seat.guest = guest
                    print(f'{guest.name} сел(-а) за стол номер {table_seat.number}')
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table_seat in self.tables:
                if table_seat.guest and not table_seat.guest.is_alive():
                    print(f'{table_seat.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table_seat.number} свободен')
                    table_seat.guest = None
                    if not self.queue.empty():
                        table_seat.guest = self.queue.get()
                        table_seat.guest.start()
                        print(f'{table_seat.guest.name} сел(-а) за стол номер {table_seat.number}')
                        #break



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
# Обслуживание гостей
cafe.discuss_guests()