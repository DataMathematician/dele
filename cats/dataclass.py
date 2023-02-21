from sqlalchemy.orm import mapped_column, relationship, Mapped
from sqlalchemy import Integer, String, Column, ForeignKey

from mapper import mapper  

@mapper.mapped_as_dataclass(unsafe_hash=True)
class Cat:
    __tablename__ = 'cats'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    name: Mapped[str] = mapped_column(String(64))
    surname: Mapped[list["CatDog"]] = relationship(default_factory=list, back_populates='surname')
  
  
@mapper.mapped_as_dataclass(unsafe_hash=True)
class CatDog:
    __tablename__ = 'cats_dogs'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True,init=False)
    name: Mapped[str] = mapped_column(String(64))
    cat_id: Mapped[int] = mapped_column(ForeignKey("cats.id"))
    surname: Mapped["Cat"] = relationship(default=None)
    