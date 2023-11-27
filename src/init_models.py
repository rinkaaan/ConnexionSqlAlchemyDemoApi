from sqlalchemy.orm import declarative_base

Base = declarative_base()

from src.resources.pet.model import Pet
