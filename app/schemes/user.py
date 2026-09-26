from pydantic import BaseModel, Field, model_validator, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username : str = Field(min_length= 3, max_length= 50, description= 'the username of student')
    email : EmailStr = Field(min_length= 6, max_length= 100, description= ' the email of student')
    password : str = Field(min_length= 8, max_length= 200, description = 'the password of a user')
    confirm_password : str = Field(min_length= 8, max_length= 200, description = 'the confirmation password')

@model_validator(mode='before')
def password_match(cls, value):
        password = value.get('password')
        confirm_password = value.get('confirm_password')
        if password != confirm_password:
            raise ValueError('passwords do not match')
        return value

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: EmailStr
    registered_at: datetime

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = Field(default=None, min_length=3, max_length=50)
    email: Optional[EmailStr] = Field(default=None, min_length=6, max_length=100)
    old_password: Optional[str] = Field(default=None, min_length=8, max_length=200)
    new_password: Optional[str] = Field(default=None, min_length=8, max_length=200)

    @model_validator(mode='after')
    def validate_password_change(self):
        if self.new_password and not self.old_password:
            raise ValueError('old_password is required to set a new_password')
        return self


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class config:
    from_attributes = True


    


