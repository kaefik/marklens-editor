import curses

class TColor:
    def __init__(self, text, bg):
        self.text = text
        self.bg = bg

class TEditor:
    def __init__(self, cols, rows):
        self.screen = curses.initscr()
        self.rows, self.cols = self.screen.getmaxyx()
        self.screen.bkgd(' ', curses.color_pair(1))
        self.screen.clear()


