#!/usr/bin/python3
"""A module containing the State model"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel):
    """Implements the State model for any state object"""
    name = ""
