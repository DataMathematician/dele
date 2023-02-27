from sqlalchemy.orm import mapped_column, relationship, Mapped
from sqlalchemy import Integer, String, Column, ForeignKey

from mapper import mapper  


@mapper.mapped_as_dataclass(unsafe_hash=True)
class Cat:
    __tablename__ = 'cats'
    __table_args__ = {
        "comment": "комментарий к животнымы",
        "md_header": "Кошки"
    }
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    name: Mapped[str] = mapped_column(String(64))
    surname_parrot: Mapped[list["Parrot"]] = relationship(default_factory=list, back_populates='surname')
    source: Mapped[str] = mapped_column(String(32), comment='источник', init=False)
    entity: Mapped[str] = mapped_column(String(32), comment='сущность', init=False)

    def __post_init__(self):
        self.entity = 'Кошка'
        self.source = '1С ЗУП'
    

@mapper.mapped_as_dataclass(unsafe_hash=True)
class Parrot:
    __tablename__ = 'parrots'
    __table_args__ = {
        "comment": "комментарий к животнымы",
        "md_header": "Попугаи"
    }
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    cat_id: Mapped[int] = mapped_column(ForeignKey("cats.id"))
    surname_cat: Mapped["Cat"] = relationship(default=None)
    

@mapper.mapped_as_dataclass(unsafe_hash=True)
class Dog:
    __tablename__ = 'dogs'
    __table_args__ = {
        "comment": "комментарий к животнымы",
        "md_header": "Собаки"
    }
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    surname: Mapped[str] = mapped_column(String(64))
  
  
@mapper.mapped_as_dataclass(unsafe_hash=True)
class CatDog:
    __tablename__ = 'cats_dogs'
    __table_args__ = {
        "comment": "комментарий к животнымы",
        "md_header": "Кошко - собаки"
    }
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True,init=False)
    name: Mapped[str] = mapped_column(String(64))
    cat_id: Mapped[int] = mapped_column(ForeignKey("cats.id"))
    surname: Mapped["Cat"] = relationship(default=None)
    