from pydantic import BaseModel, Field
from typing import Optional, Tuple, List

class TBuffer(BaseModel):
    buffer: List[str]
    cursor_x: int = Field(..., ge=0)
    cursor_y: int = Field(..., ge=0)
    selection: Optional[Tuple[int, int]] = None

    def __init__(self, buffer: List[str], cursor_x: int =0, cursor_y: int=0, selection: Optional[Tuple[int, int]] = None):
        super().__init__(buffer=buffer, cursor_x=cursor_x, cursor_y=cursor_y, selection=selection)

    

    





