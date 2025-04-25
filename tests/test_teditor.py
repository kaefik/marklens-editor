import pytest
from unittest.mock import MagicMock, patch
from itypes.teditor import TEditor
from itypes.tcolor import TColor
from itypes.tbuffer import TBuffer

@patch('curses.initscr')
def test_teditor_initialization(mock_initscr):
    # Настраиваем мок
    mock_screen = MagicMock()
    mock_screen.getmaxyx.return_value = (24, 80)
    mock_initscr.return_value = mock_screen
    
    color = TColor(text=15, bg=0)
    buffer = TBuffer(buffer=["test"])
    editor = TEditor(cols=80, rows=24, color=color, buffer=buffer)
    
    assert editor.cols == 80
    assert editor.rows == 24
    assert editor.color == color
    assert editor.buffer == buffer
    assert editor.row == 0
    assert editor.col == 0

@patch('curses.initscr')
def test_cursor_movement(mock_initscr):
    # Настраиваем мок
    mock_screen = MagicMock()
    mock_screen.getmaxyx.return_value = (24, 80)
    mock_initscr.return_value = mock_screen
    
    color = TColor(text=15, bg=0)
    buffer = TBuffer(buffer=["test"])
    editor = TEditor(cols=80, rows=24, color=color, buffer=buffer)
    
    # Проверка границ курсора по вертикали
    editor.row = -1
    editor.check_cursor()
    assert editor.row == 0
    
    editor.row = 25
    editor.check_cursor()
    assert editor.row == 23
    
    # Проверка границ курсора по горизонтали
    editor.col = -1
    editor.check_cursor()
    assert editor.col == 0
    
    # При выходе за правую границу переходим на следующую строку
    editor.row = 0
    editor.col = 80
    editor.check_cursor()
    assert editor.col == 0
    assert editor.row == 1 