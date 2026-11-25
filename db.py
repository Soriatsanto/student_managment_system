# ==========================================
# db.py  ->  Connection to the database
# ==========================================
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

# MySQL server address. Format: mysql+pymysql://USERNAME:PASSWORD@HOST:PORT
# XAMPP: username is root and the password is empty
# SERVER_URL = "mysql+pymysql://root:root@localhost:3306/alchemyBD"
SERVER_URL = "postgresql+psycopg2://hello_mm7l_user:3XK7VbPHSmd1RKOFnu1ZwCu53meheQF2@dpg-dc36q03rjlhs73evobg0-a.oregon-postgres.render.com/hello_mm7l"



engine = create_engine(SERVER_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


# Opens a database session for each request
# and closes it when the work is done.
# Used in routers like this:  db: Session = Depends(get_db)
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
