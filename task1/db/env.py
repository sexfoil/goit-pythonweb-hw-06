import os
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from sqlalchemy.orm import declarative_base
from alembic import context

Base = declarative_base()

# Встановіть шлях до бази даних PostgreSQL
config = context.config
config.set_main_option('sqlalchemy.url', 'postgresql://user:password@localhost/dbname')
target_metadata = Base.metadata

