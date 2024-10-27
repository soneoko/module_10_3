from threading import Lock, Thread
from random import choice
from time import sleep
class Bank:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        random_up = [i for i in range(1, 501)]
        for _ in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            x = choice(random_up)
            self.balance += x
            print(f'Пополнение: {x}. Баланс: {self.balance}')
            sleep(0.001)



    def take(self):
        random_low = [i for i in range(1, 501)]
        for _ in range(100):
            x = choice(random_low)
            print(f'Запрос на {x}')
            if x > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            else:
                self.balance -= x
                print(f'Снятие: {x}. Баланс: {self.balance}')

bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')