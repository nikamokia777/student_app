from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Student
from app.schemes.student import StudentCreate, StudentResponse
from typing import List
from app.models.subject import Subject
from app.models.enrollment import Enrollment


router = APIRouter(prefix='/students', tags=['Students'])
@router.post('/' ,response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(**student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@router.get('/', response_model=List[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students

@router.get('/{student_id}', response_model=StudentResponse)
def get_student(student_id : int , db : Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail='Student not found')
    return student

@router.delete('/{student_id}')
def delete_student(student_id : int , db : Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
            raise HTTPException(status_code=404, detail='Student not found')
    db.delete(student)
    db.commit()
    return({'message': 'student deleted'})

@router.post('/{student_id}/subjects/{subject_id}')
def enroll_student(student_id: int, subject_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail='Student not found')

    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
        raise HTTPException(status_code=404, detail='Subject not found')

    enrollment = Enrollment(student_id=student_id, subject_id=subject_id)
    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)
    return {'message': 'Student enrolled', 'join_date': enrollment.join_date}

@router.delete('/{student_id}/subject/{subject_id}')
def unenroll_student(student_id: int, subject_id: int, db: Session = Depends(get_db)):
    enrollment = db.query(Enrollment).filter(
        Enrollment.student_id == student_id,
        Enrollment.subject_id == subject_id
    ).first()
    if not enrollment:
        raise HTTPException(status_code=404, detail='Enrollment not found')

    db.delete(enrollment)
    db.commit()
    return {'message': 'Student removed from this subject'}




    
