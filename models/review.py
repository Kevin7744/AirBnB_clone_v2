#!/usr/bin/python3
"""Contains the Review model"""
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

class Review(BaseModel):
    """Implements the Review model"""
    place_id = ""
    user_id = ""
    text = ""
