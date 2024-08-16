from threading import Thread

import requests

class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        fight = 100
        day = 0
        while fight >= 0:
            if fight == 100:
                print(f'{self.name}, на нас напали!')
                fight -= self.power
            else:
                day += 1
                print(f'{self.name}, сражается {day} день(дня)..., осталось {fight} воинов.')
                fight -= self.power
        else:
            print(f'{self.name} одержал победу спустя {day} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')

