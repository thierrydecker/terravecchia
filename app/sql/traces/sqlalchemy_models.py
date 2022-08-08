from sqlalchemy import Column
from sqlalchemy import String, DateTime, Integer

from app.sql.database import Base


class Traces(Base):

    __tablename__ = 'traces'

    uuid = Column(String(36), primary_key=True, index=True, )
    time_stamp = Column(DateTime, index=True, )
    status_code = Column(Integer)
    base_url = Column(String)
    client_host = Column(String)
    client_port = Column(String)
