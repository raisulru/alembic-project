from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
DATABASE_URI = 'postgresql://postgres:postgres@localhost/alemb'
from .models import User
