from pydantic import BaseModel, Field

class AuthenticationModel(BaseModel):
    userName: str
    email: str  
    password: str = Field(..., min_length=6, max_length=16)  # Password length between 6 and 16

    class Config:
        min_anystr_length = 6  
        anystr_strip_whitespace = True 