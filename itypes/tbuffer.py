from pydantic import BaseModel, Field
from typing import Optional, Tuple, List

class TBuffer(BaseModel):
    buffer: List[str]
    cursor_x: int = Field(..., ge=0)
    cursor_y: int = Field(..., ge=0)
    selection: Optional[Tuple[int, int]] = None

    def __init__(self, buffer: List[str], cursor_x: int =0, cursor_y: int=0, selection: Optional[Tuple[int, int]] = None):
        super().__init__(buffer=buffer, cursor_x=cursor_x, cursor_y=cursor_y, selection=selection)

    
    def __str__(self):
        return "\n".join(self.buffer)
    
    def __repr__(self):
        return f"TBuffer(buffer={self.buffer}, cursor_x={self.cursor_x}, cursor_y={self.cursor_y}, selection={self.selection})"
    
    def __len__(self):
        return len(self.buffer)
    
    def add_line(self, row: int, line: str):
        self.buffer.insert(row, line)

    def del_line(self, row: int):
        self.buffer.pop(row)

    def add_char(self, row: int, col: int, char: str):
        self.buffer[row] = self.buffer[row][:col] + char + self.buffer[row][col:]

    def delete_char(self, row: int, col: int):
        self.buffer[row] = self.buffer[row][:col] + self.buffer[row][col+1:]

    def replace_char(self, row: int, col: int, char: str):
        self.buffer[row] = self.buffer[row][:col] + char + self.buffer[row][col+1:]

    def replace_line(self, row: int, line: str):
        self.buffer[row] = line

    def __getitem__(self, index: int) -> str:
        """Получение строки из буфера по индексу."""
        return self.buffer[index]    









