#!/usr/bin/python3
"""Contains the City model"""
from models.base_model import BaseModel
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel):
    """Implements the City class"""
    state_id = ""
    name = ""
