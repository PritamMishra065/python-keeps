from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    hashed_password = Column(String, nullable=False)
    
    # Relationship: one user can have many notes
    notes = relationship("Note", back_populates="owner", cascade="all, delete-orphan")


class Note(Base):
    __tablename__ = 'notes'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    owner = relationship("User", back_populates="notes")
