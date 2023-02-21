from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from sqlalchemy import inspect


engine = create_engine("sqlite:///smt.db")
inspector = inspect(engine)
from cats import dataclass
from parrots import dataclass
from dogs import dataclass 

from mapper import mapper
mapper.metadata.create_all(engine)


# for table in inspector.get_table_names():
#     print('\n')
#     print(table)
#     for column in inspector.get_columns(table):
#        print("Column: %s" % column['name'])
       
# from cats.dataclass import Cat, CatDog
# with Session(engine) as session:
#     session.add(CatDog(name='pipi'))
#     session.commit()
    

# with Session(engine) as session:
#     q = session.get(Cat, 2)
#     print(q)
    
    
from md_gen import MDGen

MDGen(mapper).generate()