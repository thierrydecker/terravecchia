from datetime import datetime
from uuid import uuid1

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from starlette.concurrency import iterate_in_threadpool

from app.config.database import sql_db_url
from app.sql.traces import sqlalchemy_models as sm

excluded_status_code = {}


async def trace_activity(request, response):

    if response.status_code in excluded_status_code:
        return

    request_headers = request.headers
    for header in request_headers:
        print('header:', header, request_headers[header])
    request_url = request.url
    print('url:', request_url)
    request_components = request.url.components
    print('url_components:', request_components)
    request_components = request.url.query
    print('url_components:', request_components)
    response_body = [chunk async for chunk in response.body_iterator]
    response.body_iterator = iterate_in_threadpool(iter(response_body))
    print('body:', response_body[0].decode())

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

    db.add(trace)
    db.commit()
    db.close()
