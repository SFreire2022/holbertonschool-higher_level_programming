#!/usr/bin/python3
"""
class definition of a State and an instance Base
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """ State Class definition """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
