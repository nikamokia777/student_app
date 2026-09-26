from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.database import Base


class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    join_date = Column(DateTime, default=datetime.utcnow)

    student = relationship('Student', back_populates='enrollments')
    subject = relationship('Subject', back_populates='enrollments')
