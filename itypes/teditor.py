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
    x: int = Field(..., ge=0)
    y: int = Field(..., ge=0)
    frame_right_row: int = Field(..., ge=0)
    frame_right_col: int = Field(..., ge=0)
    frame_left_row: int = Field(..., ge=0)
    frame_left_col: int = Field(..., ge=0)

    model_config = ConfigDict(arbitrary_types_allowed=True)  # Разрешаем любые типы

    def __init__(self,  rows: int, cols: int, color: TColor, buffer: TBuffer, row: int = 0, col: int = 0,  x:int = 0, y:int = 0, frame_right_row: int = 0, frame_right_col: int = 0,  frame_left_row: int = 0, frame_left_col: int = 0 ):
        """
        rows: int - количество строк (высота окна)
        cols: int - количество столбцов (ширина окна)
        color: TColor - цвет (текст, фон)
        buffer: TBuffer - буфер (строки)
        row: int - строка (текущая строка)
        col: int - столбец (текущий столбец)
        x: int - координата верхнего левого угла окна редактора с которой будет выводиться само окно на экране - столбец
        y: int - координата верхнего левого угла окна редактора с которой будет выводиться само окно на экране - строка
        frame_left_row - левая (верхняя) координата фрейма (окна) который перемещается по буферу - номер  строки
        frame_left_col - левая (верхняя) координата фрейма (окна) который перемещается по буферу - номер столбца
        frame_right_row - правая (нижняя) координата фрейма (окна) который перемещается по буферу - номер  строки
        frame_right_col - правая (нижняя) координата фрейма (окна) который перемещается по буферу - номер столбца
        """

        super().__init__(cols=cols, rows=rows, color=color, buffer=buffer, row=row, col=col, x =x, y = y, frame_right_row = frame_right_row, frame_right_col = frame_right_col, frame_left_row = frame_left_row, frame_left_col = frame_left_col )

        self.frame_right_row = self.frame_left_row + self.rows
        self.frame_right_col = self.frame_left_col + self.cols
        
        

    def _main(self, stdscr):
        # Получаем размеры терминала
        max_y, max_x = stdscr.getmaxyx()
        
        # Проверяем и корректируем размеры окна
        self.rows = min(self.rows, max_y - self.y)
        self.cols = min(self.cols, max_x - self.x)
        
        # Проверяем, что окно не выходит за пределы экрана
        if self.y + self.rows > max_y or self.x + self.cols > max_x:
            raise ValueError("Window dimensions exceed terminal size")
            
        self.screen = curses.newwin(self.rows, self.cols, self.y, self.x)
        self.screen.keypad(True)
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
                #print(f"{key=}")
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

            

