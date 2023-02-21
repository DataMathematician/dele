from pydantic.dataclasses import dataclass
from dataclasses import field

from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, Column

from mapper import mapper  

@mapper.mapped
@dataclass(unsafe_hash=True)
class Dog:
    __tablename__ = 'dogs'
    __sa_dataclass_metadata_key__ = "sa"
    id = mapped_column(Integer, primary_key=True)
    name: str = field(metadata={"sa":Column(String(64))})
    surname: str = field(metadata={"sa":Column(String(64))})
    