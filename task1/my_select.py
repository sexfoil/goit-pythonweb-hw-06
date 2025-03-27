from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from models import Student, Grade, Subject, Group, Teacher


def select_1(session: Session):
    """5 студентів із найбільшим середнім балом з усіх предметів"""
    return session.query(Student.name, func.avg(Grade.grade).label('avg_grade'))\
        .join(Grade)\
        .group_by(Student.id)\
        .order_by(desc('avg_grade'))\
        .limit(5).all()


def select_2(session: Session, subject_id):
    """Студент із найвищим середнім балом з певного предмета"""
    return session.query(Student.name, func.avg(Grade.grade).label('avg_grade'))\
        .join(Grade)\
        .filter(Grade.subject_id == subject_id)\
        .group_by(Student.id)\
        .order_by(desc('avg_grade'))\
        .first()


def select_3(session: Session, subject_id):
    """Середній бал у групах з певного предмета"""
    return session.query(Group.name, func.avg(Grade.grade).label('avg_grade'))\
        .join(Student).join(Grade)\
        .filter(Grade.subject_id == subject_id)\
        .group_by(Group.id).all()


def select_4(session: Session):
    """Середній бал на потоці"""
    return session.query(func.avg(Grade.grade).label('avg_grade')).scalar()


def select_5(session: Session, teacher_id):
    """Курси, які читає певний викладач"""
    return session.query(Subject.name)\
        .filter(Subject.teacher_id == teacher_id).all()


def select_6(session: Session, group_id):
    """Список студентів у певній групі"""
    return session.query(Student.name)\
        .filter(Student.group_id == group_id).all()


def select_7(session: Session, group_id, subject_id):
    """Оцінки студентів у певній групі з певного предмета"""
    return session.query(Student.name, Grade.grade)\
        .join(Grade).filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()


def select_8(session: Session, teacher_id):
    """Середній бал, який ставить певний викладач зі своїх предметів"""
    return session.query(func.avg(Grade.grade).label('avg_grade'))\
        .join(Subject).filter(Subject.teacher_id == teacher_id).scalar()


def select_9(session: Session, student_id):
    """Список курсів, які відвідує певний студент"""
    return session.query(Subject.name)\
        .join(Grade).filter(Grade.student_id == student_id).distinct().all()


def select_10(session: Session, student_id, teacher_id):
    """Список курсів, які певному студенту читає певний викладач"""
    return session.query(Subject.name)\
        .join(Grade)\
        .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)\
        .distinct().all()
