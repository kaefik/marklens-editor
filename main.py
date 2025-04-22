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

    x=0
    y=0
    while True:
        key = screen.getch()
        if key == curses.KEY_UP:
            y -= 1
        elif key == curses.KEY_DOWN:
            y += 1
        elif key == curses.KEY_LEFT:
            x -= 1
        elif key == curses.KEY_RIGHT:
            x += 1
        elif key == curses.KEY_ENTER:
            y+=1
            x=0
        elif key == 17:
            break
        else:
            screen.addch(y, x, chr(key))
            x+=1
            
        screen.refresh()
            
    
    # napms позволяет выставить задержку в мс
    # curses.napms(3000)
    # endwin завершает сессию и возвращает нас в обычную консоль!
    curses.endwin()

if __name__ == "__main__":
    wrapper(main)


