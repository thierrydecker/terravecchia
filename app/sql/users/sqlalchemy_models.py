from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import UniqueConstraint

from app.sql.database import Base


class User(Base):

    __tablename__ = "users"

    uuid = Column(
            String(36),
            primary_key=True,
            index=True,
    )

    id = Column(
            String(50),
            index=True,
    )

    first_name = Column(
            String(100),
    )

    last_name = Column(
            String(100),
    )

    UniqueConstraint(
            'id',
            name='un_id',
    )
