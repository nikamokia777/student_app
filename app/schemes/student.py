from pydantic import BaseModel
class StudentCreate(BaseModel):
    first_name : str
    last_name : str
    email : str
class StudentResponse(BaseModel):
    id : int
    first_name : str
    last_name : str
    email : str
class Config:
    from_attributes = True