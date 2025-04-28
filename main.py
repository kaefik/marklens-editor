import curses
from curses import wrapper
from itypes.teditor import TEditor
from itypes.tcolor import  TColor
from itypes.tbuffer import TBuffer

def main():

    app_buffer = TBuffer([])

    color = TColor(curses.COLOR_WHITE,  curses.COLOR_BLUE)
    editor = TEditor(30, 50, color, buffer=app_buffer, x=30, y=10)

    editor.start()



if __name__ == "__main__":
    main()


