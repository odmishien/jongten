class Question:
    def __init__(self, man, pin, sou, win_tile, figure):
        self.man = man
        self.pin = pin
        self.sou = sou
        self.win_tile = win_tile
        self.figure = figure

    def get_man(self):
        return self.man

    def get_pin(self):
        return self.pin

    def get_sou(self):
        return self.sou

    def get_win_tile(self):
        return self.win_tile

    def get_figure(self):
        return self.figure
