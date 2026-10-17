from datetime import date

from sqlalchemy import MetaData, String, Date, create_engine
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column

dbms = ""
engine = create_engine(dbms, echo=True)
metadata = MetaData()


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), unique=True)
    author: Mapped[str] = mapped_column(String(50))
    publishing_date: Mapped[date] = mapped_column(Date)

    def __repr__(self):
        return f"Book(id={self.id!r}, title={self.title!r}, author={self.author!r}, publishing_date={self.publishing_date}, state={self.state!r})"


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
