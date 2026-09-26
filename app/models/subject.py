from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    duration = Column(Integer)

    enrollments = relationship('Enrollment', back_populates='subject')
