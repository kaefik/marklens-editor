from pydantic import BaseModel, Field
from typing import Optional, Tuple, List

class TBuffer(BaseModel):
    buffer: List[str]
    cursor: int = Field(..., ge=0)
    selection: Optional[Tuple[int, int]] = None

    def __init__(self, buffer: List[str], cursor: int, selection: Optional[Tuple[int, int]] = None):
        super().__init__(buffer=buffer, cursor=cursor, selection=selection)

    def __str__(self):
        return ''.join(self.buffer)

    def __repr__(self):
        return f"TBuffer(buffer={self.buffer}, cursor={self.cursor}, selection={self.selection})"

    def __len__(self):
        return len(self.buffer)

    def __getitem__(self, index: int):
        return self.buffer[index]

    def __setitem__(self, index: int, value: str):
        self.buffer[index] = value

    def __delitem__(self, index: int):
        del self.buffer[index]

    def __contains__(self, item: str):
        return item in self.buffer

    def __iter__(self):
        return iter(self.buffer)

    def __next__(self):
        return next(self.buffer)

    def __add__(self, other: str):
        return self.buffer + other

    





