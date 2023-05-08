"""
To create a new model:
1) Create a module database.models.<table_name>.py
2) Create a class in <TableName> and inherit from ModelBase class
3) In database.models.__init__.py add: "from .<TableName> import <TableName>"
"""
from sqlalchemy.orm import declarative_base


ModelBase = declarative_base()
