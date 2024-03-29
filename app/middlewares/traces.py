from datetime import datetime
from uuid import uuid1

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.database import sql_db_url
from app.config.traces import excluded_status_codes
from app.sql.traces import sqlalchemy_models as sm


async def trace_activity(request, response):

    if response.status_code in excluded_status_codes:
        return

    engine = create_engine(
        sql_db_url,
    )

    session_local = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )

    db = session_local()
    trace = sm.Traces()

    trace.uuid = str(uuid1())
    trace.time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    trace.status_code = response.status_code
    trace.base_url = str(request.base_url)
    trace.client_host = str(request.client.host)
    trace.client_port = str(request.client.port)
    trace.cookies = str(request.cookies)
    trace.method = request.method
    trace.path_params = str(request.path_params)
    trace.query_params = str(request.query_params)
    trace.request_headers = str(request.headers)
    trace.url = str(request.url)
    trace.path = request.url.components.path

    db.add(trace)
    db.commit()
    db.close()
