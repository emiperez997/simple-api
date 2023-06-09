from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    done = Column(Boolean)