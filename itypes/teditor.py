from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from .tcolor import TColor
from .tbuffer import TBuffer
import curses
from curses import wrapper
import os


class TEditor(BaseModel):
    cols: int = Field(..., ge=0)
    rows: int = Field(..., ge=0)
    color: TColor
    screen: Optional[curses.window] = None
    buffer: TBuffer
    row: int = Field(..., ge=0)
    col: int = Field(..., ge=0)

    model_config = ConfigDict(arbitrary_types_allowed=True)  # Разрешаем любые типы

    def __init__(self,  rows: int, cols: int, color: TColor, buffer: TBuffer, row: int = 0, col: int =0):
        super().__init__(cols=cols, rows=rows, color=color, buffer=buffer, row=row, col=col)
        self.row = row
        self.col = col

    def _main(self, stdscr):
        # Получаем размеры терминала
        max_y, max_x = stdscr.getmaxyx()
        # Проверяем и корректируем размеры окна
        self.rows = min(self.rows, max_y)
        self.cols = min(self.cols, max_x)
        
        self.screen = curses.newwin(self.rows, self.cols, 0, 0)
        #self.screen.keypad(True)
        self.screen.clear()
        
        self.run()

    def init_colors(self, id: int = 1):
        curses.start_color()
        curses.init_pair(id, self.color.text, self.color.bg)  # (id, текст, фон)
        
        # Заливаем весь экран синим с белым текстом
        self.screen.bkgd(' ', curses.color_pair(id))  # ' ' - заполнитель фона
        self.screen.clear()  # Очистка с применением фона

    def set_color(self, bg:int = Field(..., ge=0, le=255), text:int = Field(..., ge=0, le=255)):
        self.color.bg = bg
        self.color.text = text

    def check_cursor(self):
        if self.col >= self.cols:
            self.col = self.cols - 1
            
        if self.col < 0:
            self.col = 0
        
        if self.row >= self.rows:
            self.row = self.rows - 1

        if self.row < 0:
            self.row = 0

    def run(self):
        try:
            self.init_colors()
            self.screen.keypad(True)  # Включаем обработку специальных клавиш
        
            while True:
                key = self.screen.getch()
                print(f"{key=}")
                if key == curses.KEY_UP:
                    self.row -= 1
                elif key == curses.KEY_DOWN:
                    self.row += 1
                elif key == curses.KEY_LEFT:
                    self.col -= 1
                elif key == curses.KEY_RIGHT:
                    self.col += 1
                elif key == 8:
                    self.col -= 1                 
                    self.check_cursor()
                    self.screen.addch(self.row, self.col, ' ')
                    
                elif key in [10, 13, curses.KEY_ENTER]:  # Enter может быть 10, 13 или KEY_ENTER
                    self.row += 1
                    self.col = 0        
                elif key == 17: # Ctrl+Q
                    break
                else:
                    self.screen.addch(self.row, self.col, chr(key))
                    self.col += 1

                self.check_cursor()
                self.screen.move(self.row, self.col)
                self.screen.refresh()
        finally:
            curses.endwin()

    def start(self):
        wrapper(self._main)

            

