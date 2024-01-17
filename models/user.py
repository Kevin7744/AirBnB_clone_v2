#!/usr/bin/python3
#!/usr/bin/python3
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel):
    """User class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""