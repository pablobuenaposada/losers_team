import threading
import time
from random import randint


class Main:
    happiness = 0
    research = 0
    time = 666
    last_time = 0

    def __init__(self):
        t = threading.Thread(target=self.main)
        t.start()

    def minute_passed(self):
        if time.time() - self.last_time >= 2:
            self.last_time = time.time()
            return True

    def main(self):
        while True:
            if self.minute_passed():
                self.time = self.time - 1

            self.research = randint(1, 100)
