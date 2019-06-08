from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from datatime import datatime

engine = create_engine('sqlite:///employees.sqlite')
engine.echo = True

Base = declarative_base()

Session = sessionmaker(bind=engine)

session = Session()
