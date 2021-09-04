from sqlalchemy import Boolean, Column, Integer, String

from app.db.base_class import Base
from app.db.mixin_class import CommonColumnsMixin


class User(Base, CommonColumnsMixin):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    def __str__(self):
        return self.id
