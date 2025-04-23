import curses
from curses import wrapper




def main(stdscr):
    # initscr - инициализирует окно, запуская свое окно
    screen = curses.initscr()

    # # addstr - Позволяет печатать текст без сложностей
    # # К слову, данная система поддерживает Юникод, поэтому кириллица ей не страшна
    # # Первые два аргумента передают позицию текста. [Сначала строка, потом столбец] (столбцы по своей сути количество пробельных отступов)
    # screen.addstr( 0, 10, "(0, 0)")
    # screen.addch(5, 5, "!")

    # Инициализация цветов
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)  # (id, текст, фон)
    
    # Заливаем весь экран синим с белым текстом
    stdscr.bkgd(' ', curses.color_pair(1))  # ' ' - заполнитель фона
    stdscr.clear()  # Очистка с применением фона
    

    rows, cols = stdscr.getmaxyx()
    print(f"{rows=}, {cols=}")

    col=0
    row=0
    while True:
        key = screen.getch()
        if key == curses.KEY_UP:
            row -= 1
        elif key == curses.KEY_DOWN:
            row += 1
        elif key == curses.KEY_LEFT:
            col -= 1
        elif key == curses.KEY_RIGHT:
            col += 1
        elif key in [10, 13, curses.KEY_ENTER]:  # Enter может быть 10, 13 или KEY_ENTER
            row += 1
            col = 0        
        elif key == 17:
            break
        else:
            screen.addch(row, col, chr(key))
            col += 1

        screen.move(row, col)  # Устанавливаем курсор в текущую позицию
        screen.refresh()
            
    
    # napms позволяет выставить задержку в мс
    # curses.napms(3000)
    # endwin завершает сессию и возвращает нас в обычную консоль!
    curses.endwin()

if __name__ == "__main__":
    wrapper(main)


