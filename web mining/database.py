# pip install sqlalchemy

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer , primary_key=True)
    title = Column(String)
    pubdate = Column(String)
    summary = Column(String)
    author = Column(String)
    imgsrc = Column(String)

    def __str__(self):
       return self.title

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer,primary_key=True)
    title = Column(String)
    rrcount = Column(String)
    price = Column(String)

    def __str__(self):
        return self.title

#from the beginning
if __name__ == "__main__":
    engine = create_engine('sqlite:///example.db')
    Base.metadata.create_all(engine)