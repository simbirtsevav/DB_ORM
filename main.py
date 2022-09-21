import sqlalchemy
import psycopg2
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Stock, Sale, Shop


DSN = 'postgresql://postgres:admin@localhost:5432/ORM'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


def find_publisher(publishers):

    try:
        int(publishers)
        for publ in session.query(Publisher).filter(Publisher.publisher_id == publishers).all():
            print(publ)
    except:
        for publ in session.query(Publisher).filter(Publisher.publisher_name == publishers).all():
            print(publ)

find_publisher(input(f'введите Id или издателя: '))

session.close()





