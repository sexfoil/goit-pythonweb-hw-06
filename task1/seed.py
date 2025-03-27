from faker import Faker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Student, Group, Teacher, Subject, Grade
import random
from datetime import datetime, timedelta

# Налаштування бази даних
DATABASE_URL = 'postgresql://user:password@localhost/dbname'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

fake = Faker()

def populate_data():
    session = Session()
    
    # Створення груп
    groups = [Group(name=f"Group {i}") for i in range(1, 4)]
    session.add_all(groups)
    session.commit()
    
    # Створення викладачів
    teachers = [Teacher(name=fake.name()) for _ in range(4)]
    session.add_all(teachers)
    session.commit()
    
    # Створення предметів
    subjects = [Subject(name=f"Subject {i}", teacher=random.choice(teachers)) for i in range(1, 8)]
    session.add_all(subjects)
    session.commit()
    
    # Створення студентів
    students = [Student(name=fake.name(), group=random.choice(groups)) for _ in range(40)]
    session.add_all(students)
    session.commit()
    
    # Створення оцінок
    for student in students:
        for _ in range(random.randint(10, 20)):  # Кількість оцінок
            subject = random.choice(subjects)
            grade = random.uniform(2, 5)  # Оцінка між 2 і 5
            date = fake.date_between(start_date="-1y", end_date="today")
            session.add(Grade(student=student, subject=subject, grade=grade, date=date))
    
    session.commit()
    session.close()

if __name__ == "__main__":
    populate_data()
    