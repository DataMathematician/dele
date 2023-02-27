from pydantic.dataclasses import dataclass
from dataclasses import field

from sqlalchemy.orm import mapped_column, relationship, Mapped
from sqlalchemy import Integer, String, Column, ForeignKey

from mapper import mapper  

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
    