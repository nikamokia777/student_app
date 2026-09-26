from pydantic import BaseModel

class SubjectCreate(BaseModel):
    title : str
    duration : int

class SubjectResponse(BaseModel):
    id : int
    title : str
    duration : int
class config:
    from_attributes = True

