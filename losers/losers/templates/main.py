import threading
import time

INIT_TIME = 10
INIT_RESEARCH = 100
INIT_HAPPINESS = 100
RESTART_WAITING_TIME = 2


class Main:
    # resources
    happiness = INIT_HAPPINESS
    research = INIT_RESEARCH

    # result message
    result = ""

    # time things
    time = INIT_TIME
    last_time = 0
    restart_time = 0

    def __init__(self):
        t = threading.Thread(target=self.main)
        t.start()

    def second_passed(self):
        if time.time() - self.last_time >= 2:
            self.last_time = time.time()
            return True

    def main(self):
        while True:
            if self.time > 0:
                if self.second_passed():
                    self.time = self.time - 1

                    self.research = self.research - 1
                    self.happiness = self.happiness - 1

            else:
                self.result = "You lose"
                if self.second_passed():
                    self.restart_time = self.restart_time + 1
                if self.restart_time > RESTART_WAITING_TIME:
                    self.time = INIT_TIME
                    self.restart_time = 0
                    self.result = ""

                    self.research = INIT_RESEARCH
                    self.happiness = INIT_HAPPINESS
