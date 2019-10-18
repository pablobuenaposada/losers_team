import threading
import time
import random
from losers.wiregame import WireGame

INIT_TIME = 10
INIT_RESEARCH = 100
INIT_HAPPINESS = 100
INIT_PRODUCTION = 100
RESTART_WAITING_TIME = 2
RESOURCE_DELTA = 10


class Main:
    # resources
    happiness = INIT_HAPPINESS
    research = INIT_RESEARCH
    production = INIT_PRODUCTION

    # result message
    result = ""

    # time things
    time = INIT_TIME
    last_time = 0
    five_last_time = 0
    restart_time = 0

    too_fast = False

    #games
    wg = WireGame()

    def __init__(self):
        t = threading.Thread(target=self.main)
        t.start()

    def second_passed(self):
        if time.time() - self.last_time >= 2:
            self.last_time = time.time()
            return True

    def five_second_passed(self):
        if time.time() - self.five_last_time >= 10:
            self.five_last_time = time.time()
            return True

    def get_random_event(self):
        event_list = [
            {"result": "Anarchy", "research_delta": 0,  "happiness_delta": 0, "production_delta": 0},
            {"result": "Our colonys engineers go on strike and the production slows down", "research_delta": 0,  "happiness_delta": 0, "production_delta": -RESOURCE_DELTA},
            {"result": "BBQ day increases heavily the consumption, people are unhappy", "research_delta": 0,  "happiness_delta": -RESOURCE_DELTA, "production_delta": 0},
            {"result": "Our scientists are ill because bad chemicals leaked in the lab", "research_delta": -RESOURCE_DELTA,  "happiness_delta": 0, "production_delta": 0},
            {"result": "Severe pests spread throughout the colony, we need immediate action", "research_delta": 0,  "happiness_delta": -RESOURCE_DELTA, "production_delta": 0},
            {"result": "Recent rainfalls improved the agricultural production, people are very happy with the abundance of food", "research_delta": 0,  "happiness_delta": 0, "production_delta": RESOURCE_DELTA},
            {"result": "Our researchers just discovered a new resource that can be eaten", "research_delta": RESOURCE_DELTA,  "happiness_delta": RESOURCE_DELTA, "production_delta": RESOURCE_DELTA},
            {"result": "Thanks to a new discovery, our colony uses less energy", "research_delta": -RESOURCE_DELTA,  "happiness_delta": RESOURCE_DELTA, "production_delta": 0},
        ]
        return event_list[random.randint(0,7)]

    def main(self):
        while True:
            if self.time > 0:
                if self.second_passed():
                    self.time = self.time - 1
                    self.too_fast = False
                    self.research = self.research - 1
                    self.happiness = self.happiness - 1
                    self.production = self.production - 1

                if not self.too_fast and self.wg.hit_wire():
                    self.research = self.research - 10
                    self.too_fast = True

                if not self.too_fast and self.wg.hit_end():
                    self.research = self.research + 50
                    self.too_fast = True

                if self.five_second_passed():
                    random_result = self.get_random_event()
                    self.result = random_result["result"]
                    self.research = self.research + random_result["research_delta"]
                    self.happiness = self.happiness + random_result["happiness_delta"]
                    self.production = self.production + random_result["production_delta"]

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
                    self.prodcution = INIT_PRODUCTION
