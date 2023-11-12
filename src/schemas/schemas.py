import re
from fastapi import HTTPException
from pydantic import BaseModel
from pydantic import field_validator

PHONE_NUMBER_MATCH = re.compile(r"^\+?[0-9]+$")


class UserData(BaseModel):
    phone: str
    address: str

    @field_validator('phone')
    def validate_number(cls, val):
        if not PHONE_NUMBER_MATCH.match(val):
            HTTPException(status_code=422, detail='Number is incorrect')
        return val



