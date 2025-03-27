import my_select
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.postgres_db import DATABASE_URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

print(my_select.select_1(Session()))
