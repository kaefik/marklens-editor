from pydantic import BaseModel, Field

class TColor(BaseModel):
    text: int = Field(..., ge=0, le=255)
    bg: int = Field(..., ge=0, le=255) 