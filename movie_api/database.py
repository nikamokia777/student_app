from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
DATABASE_URL = 'postgresql+psycopg2://postgres:Mokia123$@localhost:1940/movie_db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


                       
