from pydantic import BaseModel, Field
import curses
from typing import Optional
from .tcolor import TColor

class TEditor(BaseModel):
    cols: int = Field(..., gt=0)
    rows: int = Field(..., gt=0)
    color: TColor
    screen: Optional[curses.window] = None

    def __init__(self, cols: int, rows: int, color: TColor):
        super().__init__(cols=cols, rows=rows, color=color)
        self.screen = curses.initscr()
        self.rows, self.cols = self.screen.getmaxyx()
        self.screen.bkgd(' ', curses.color_pair(1))
        self.screen.clear()


