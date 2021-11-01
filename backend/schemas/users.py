#use of schemas is to validate the type of data we are going to get from users


from typing import Optional
from pydantic import BaseModel, Emailstr


class UserCreate(BaseModel):
    username : str
    email : Emailstr
    password : str
