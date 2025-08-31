from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    username:str
    password:str
    
class Token(BaseModel):
    access_token:str
    token_type:str
    
class NotesRequest(BaseModel):
    title:str
    content:str