from pydantic import BaseModel, Field


class TokenizeRequest(BaseModel):
    text: str = Field(..., min_length=1, example="วันนี้คือวันจันทร์")


class TokenizeResponse(BaseModel):
    texttoken: str = Field(..., example="วัน นี้ คือ วัน จันทร์")