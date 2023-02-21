from sqlalchemy.orm import registry
from sqlalchemy.schema import MetaData

metadata = MetaData()

mapper = registry(metadata=metadata)