from uuid import uuid1

from sqlalchemy.orm import Session

from app.sql.users import sqlalchemy_models as sm
from app.sql.users import pydantic_models as pm
from app.exceptions.custom_exception import CustomException
from app.helpers.query_builders import select


def get_users(
    db: Session,
    offset: int = 0,
    limit: int = 100,
    columns: list[str] = None,
    filters: str = None,
) -> list[sm.User]:

    db_users = select(
        db=db,
        sm_model=sm.User,
        pm_model=pm.User,
        columns=columns,
        limit=limit,
        offset=offset,
    )
    db_users = db_users.all()
    return db_users


def get_user(
    db: Session,
    user_id: str,
    columns: list[str] = None,
) -> sm.User:

    db_user = select(
        db=db,
        sm_model=sm.User,
        pm_model=pm.User,
        columns=columns,
    )
    db_user = db_user.filter(sm.User.id == user_id).first()
    return db_user


def create_user(
    db: Session,
    user_id: str,
    user_model: pm.UserCreate,
) -> sm.User:

    db_user = get_user(db, user_id=user_id)
    if db_user:
        raise CustomException(
            status_code=400,
            content={
                'error'  : 'user-003',
                'message': 'User exists',
                'detail' : f'User: {user_id} already exists',
            }
        )
    uuid = str(uuid1())
    db_user = sm.User(
        uuid=uuid,
        id=user_id,
        first_name=user_model.first_name,
        last_name=user_model.last_name,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(
    db: Session,
    user_id: str,
) -> sm.User:

    db_user = get_user(db=db, user_id=user_id, columns=['all'], )
    if not db_user:
        raise CustomException(
            status_code=404,
            content={
                'error'  : 'user-001',
                'message': 'User not found',
                'detail' : f'User: {user_id} was not found',
            }
        )
    db.delete(db_user)
    db.commit()
    return db_user


def patch_user(
    db: Session,
    user_id: str,
    user_model: pm.UserUpdate,
) -> sm.User:

    db_user = get_user(db=db, user_id=user_id, columns=['all'], )
    if not db_user:
        raise CustomException(
            status_code=404,
            content={
                'error'  : 'user-001',
                'message': 'User not found',
                'detail' : f'User: {user_id} was not found',
            }
        )
    if user_model.first_name and user_model.first_name != db_user.first_name:
        db_user.first_name = user_model.first_name
    if user_model.last_name and user_model.first_name != db_user.last_name:
        db_user.last_name = user_model.last_name
    db.commit()
    db.refresh(db_user)
    return db_user
