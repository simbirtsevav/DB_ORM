import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'

    publisher_id = sq.Column(sq.Integer, primary_key=True)
    publisher_name = sq.Column(sq.String(length=60), unique=True)

    def __str__(self):
        return f'{self.publisher_id}: {self.publisher_name}'

class Shop(Base):
    __tablename__ = 'shop'

    shop_id = sq.Column(sq.Integer, primary_key=True)
    shop_name = sq.Column(sq.String, nullable=False)

class Book(Base):
    __tablename__ = 'book'

    book_id = sq.Column(sq.Integer, primary_key=True)
    book_title = sq.Column(sq.String, nullable=False )
    publisher_id = sq.Column(sq.Integer, sq.ForeignKey('publisher.publisher_id'), nullable=False)

    publisher = relationship(Publisher, backref='book')
class Stock(Base):
    __tablename__ = 'stock'

    stock_id = sq.Column(sq.Integer, primary_key=True)
    book_id = sq.Column(sq.Integer, sq.ForeignKey('book.book_id'), nullable=False)
    shop_id = sq.Column(sq.Integer, sq.ForeignKey('shop.shop_id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    book = relationship(Book, backref='stock')
    shop = relationship(Shop, backref='stock')


class Sale(Base):
    __tablename__ = 'sale'

    sale_id = sq.Column(sq.Integer, primary_key=True)
    sale_price = sq.Column(sq.Integer, nullable=False)
    sale_datasale = sq.Column(sq.Date, nullable=False)
    stock_id = sq.Column(sq.Integer, sq.ForeignKey('stock.stock_id'), nullable=False)
    sale_stock = sq.Column(sq.Integer, nullable=False)

    stock = relationship(Stock, backref='sale')


def create_tables(engine):
    Base.metadata.create_all(engine)



