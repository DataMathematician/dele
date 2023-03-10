from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from sqlalchemy import inspect


engine = create_engine("sqlite:///smt.db")
inspector = inspect(engine)
from data_cls import dataclass
from mapper import mapper
mapper.metadata.create_all(engine)


# for table in inspector.get_table_names():
#     print('\n')
#     print(table)
#     for column in inspector.get_columns(table):
#        print("Column: %s" % column['name'])
       
# from data_cls.dataclass import Cat
# with Session(engine) as session:
#     session.add(Cat(name='pipi'))
#     session.commit()
    
# with Session(engine) as session:
#     q = session.get(Cat, 5)
#     print(q)
    
    
from md_gen import MDGen

MDGen(mapper).generate()