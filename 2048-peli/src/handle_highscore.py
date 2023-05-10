import os


class HandleHighscore:
    def __init__(self):
        self.init_high = 0
        self.highscore = 0
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(script_dir, "data", "highscore")

    def initialize_highscore(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            self.init_high = int(file.readline())
        self.highscore = self.init_high
        return self.highscore

    def initialize_init_high(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            self.init_high = int(file.readline())
        return self.init_high

    def update(self, highscore):
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write(str(highscore))
        self.init_high = highscore
        return self.init_high
