from pydantic import BaseModel, Field

class TColor(BaseModel):
    text: int = Field(..., ge=0, le=255)
    bg: int = Field(..., ge=0, le=255) 

    def __init__(self, text: int, bg: int):
        super().__init__(text=text, bg=bg)

    def __str__(self):
        return f"TColor(text={self.text}, bg={self.bg})"


