from sqlalchemy.inspection import inspect
from sqlalchemy.orm import load_only
from sqlalchemy.orm import Session

from app.helpers.columns import sanitise


def select(
    db: Session,
    sm_model,
    pm_model,
    columns=None,
    limit=0,
    offset=0,
):
    mapper = inspect(sm_model)
    pk_columns = [
        column.name
        for column in mapper.columns
        if column.primary_key
    ]
    db_query = db.query(sm_model)
    if columns:
        columns = sanitise(
            columns=columns,
            valid_columns=pm_model.schema()['properties']
        )
        if 'all' not in columns:
            db_query = db_query.options(load_only(*columns))
    else:
        db_query = db_query.options(load_only(*pk_columns))
    if limit != 0:
        db_query = db_query.limit(limit)
    if offset > 0:
        db_query = db_query.offset(offset)
    return db_query
