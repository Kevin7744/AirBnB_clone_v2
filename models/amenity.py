#!/usr/bin/python3
"""Contains the Amenity model"""
from models.base_model import BaseModel
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    """Implements the Amenity model"""
    name = ""
