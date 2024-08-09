import random
import time


class SpeedChallenge():
    """
        call clicked_key to step game.
        returns score as a string or "loss"
    """

    def __init__(self, callback: function):
        self.POSSIBLE_KEYS = ("g", "e", "a", "r", "o", "s", "p", "c")
        self.current_correct_key = random.choice(self.POSSIBLE_KEYS)
        self.correct_entries = 0
        self.start_time = time.time()
        self.time_taken = 0
        self.points = 0
        self.POINT_DECREMENT_AMOUNT = 50
        self.POINT_INCREMENT_AMOUNT = 100
        self.LOWER_THRESHOLD = -1000
        self.UPPER_THRESHOLD = 1000
        self.SCALEFACTOR = 1
        self.callback = callback

    def show_game(self):
        print(self.c)

    def clicked_key(self, key_selection: str):
        if key_selection == self.current_correct_key:
            self.points += self.POINT_INCREMENT_AMOUNT
            self.current_correct_key = self.get_random_key()

        elif key_selection != self.current_correct_key:
            self.points -= self.POINT_DECREMENT_AMOUNT
            self.current_correct_key = self.get_random_key()

        if self.points >= self.UPPER_THRESHOLD:
            self.win()

        if self.points <= self.LOWER_THRESHOLD:
            self.loss()

    def win(self):
        self.time_taken = self.get_time_taken()
        score = self.calculate_score()
        self.callback(str(score))

    def loss(self):
        self.callback("loss")

    def calculate_score(self) -> int:
        return ((self.points / self.time_taken) * self.SCALEFACTOR)

    def get_time_taken(self) -> float: return time.time() - self.start_time

    def get_random_key(self) -> str: random.choice(self.POSSIBLE_KEYS)
