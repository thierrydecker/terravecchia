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
    cookies = Column(String)
    method = Column(String)
    path_params = Column(String)
    query_params = Column(String)
    request_headers = Column(String)
    url = Column(String)
    path = Column(String)
