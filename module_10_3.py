from threading import Thread, Lock
from time import sleep
from random import randint

class Bank():
    def __init__(self):
        self.balance = randint(50, 500)
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            cash_in = randint(50, 500)
            self.balance += cash_in
            print(f'Пополнение: {cash_in}. Баланс: {self.balance}.')
            if self.balance >= 500 and  self.lock ==  self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            self.lock.locked()
            cash_out = randint(50, 500)
            print(f'Запрос на {cash_out}.')
            if cash_out <= self.balance:
                self.balance -= cash_out
                print(f'Снятие: {cash_out}. Баланс: {self.balance}.')
            else:
                print('Запрс отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)

bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')