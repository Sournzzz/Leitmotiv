from datetime import date

from sqlalchemy import (
    Column,
    MetaData,
    PrimaryKeyConstraint,
    String,
    Date,
    ForeignKey,
    Table,
    create_engine,
)

from sqlalchemy.orm import Session, DeclarativeBase, Mapped, relationship, mapped_column

dbms = ""
engine = create_engine(dbms, echo=True)
metadata = MetaData()


class Base(DeclarativeBase):
    pass


author_book = Table(
    "author_book",
    Base.metadata,
    Column("book_id", ForeignKey("books.id")),
    Column("author_id", ForeignKey("authors.id")),
)


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    original_language: Mapped[str] = mapped_column(String(30))
    first_publishing_date: Mapped[date] = mapped_column(Date)


class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    lastname: Mapped[str | None] = mapped_column(String(50))


"""
EXPAND THE CLASS WHENEVER YOU NEED MORE BEHAVIOUR, WHEN YOU NEED TO REPRESENT EACH ASSOCIATION AS A PYTHON OBJECT 
class BookAuthor(Base):
    __tablename__ = "bookauthor"
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"), primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"), primary_key=True)

    __table_args__ = PrimaryKeyConstraint("book_id", "author_id")

"""

Base.metadata.create_all(engine)


def insert_book(book_dict):
    with Session(engine) as session:
        book = Book(
            title=book_dict["title"],
            author=book_dict["author"],
            publishing_date=book_dict["publishing_date"],
        )
        session.add_all([book])
        session.commit()
