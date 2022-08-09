from fastapi import APIRouter
from fastapi import Query
from fastapi import Depends

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from app.sql.database import get_db
from app.sql.users import crud
from app.sql.users import pydantic_models as pm
from app.config.urls import app_prefix
from app.exceptions.custom_exception import CustomException
from app.helpers.columns import sanitise
from app.models.custom_models import ModelError

router = APIRouter(
    prefix=f'{app_prefix}/users',
    tags=["Users endpoints"],
)


@router.get(
    path='',
    response_model=list[pm.User],
    name='Gets users',
    description='The endpoint returns a list of users',
    responses={
        400: {'model': ModelError},
        422: {'model': ModelError},
    }
)
def get_users(
    offset: int = Query(
        default=0,
        ge=0,
        description='The number of elements to skip'
    ),
    limit: int = Query(
        default=0,
        ge=0,
        description='The number of elements to return'
    ),
    columns: list[str] = Query(
        default=[],
        description="The columns to return"
    ),
    filters: str = Query(
        default=None,
        description="The condition in Lucene syntax"
    ),
    db: Session = Depends(get_db),
):

    if columns:
        columns = sanitise(
            columns=columns,
            valid_columns=pm.User.schema()['properties']
        )
    users = jsonable_encoder(
        crud.get_users(
            db=db,
            offset=offset,
            limit=limit,
            columns=columns,
            filters=filters,
        )
    )
    headers = {
        'Pagination-Count': str(len(users)),
        'Pagination-Page' : str(len(users)),
        'Pagination-Limit': str(limit),
    }
    return JSONResponse(
        content=users,
        headers=headers,
    )


@router.get(
    path="/{user_id}",
    response_model=pm.User,
    name='Gets one users',
    description='The endpoint returns one users',
    responses={
        404: {'model': ModelError},
        422: {'model': ModelError},
    }
)
def get_one_user(
    user_id: str,
    columns: list[str] = Query(
        default=[],
        description="The columns to return"
    ),
    db: Session = Depends(get_db),
):
    if columns:
        columns = sanitise(
            columns=columns,
            valid_columns=pm.User.schema()['properties']
        )
    user = jsonable_encoder(
        crud.get_user(
            db=db,
            user_id=user_id,
            columns=columns
        )
    )
    if not user:
        raise CustomException(
            status_code=404,
            content={
                'error'  : 'user-001',
                'message': 'User not found',
                'detail' : f'User: {user_id} was not found',
            }
        )
    return JSONResponse(
        content=user,
    )


@router.post(
    path='/{user_id}',
    response_model=pm.User,
    status_code=201,
    name='Creates one user',
    description='The endpoint creates a user and returns it',
    responses={
        404: {'model': ModelError},
        422: {'model': ModelError},
    }
)
def create_user(
    user_id: str,
    user_model: pm.UserCreate,
    db: Session = Depends(get_db),
):
    user = jsonable_encoder(
        crud.create_user(
            db=db,
            user_id=user_id,
            user_model=user_model
        )
    )
    return JSONResponse(
        status_code=201,
        content=user,
    )


@router.delete(
    path='/{user_id}',
    status_code=202,
    response_model=pm.User,
    name='Deletes one user',
    description='The endpoint deletes a user and returns it',
    responses={
        404: {'model': ModelError},
        422: {'model': ModelError},
    },
)
def delete_user(
    user_id: str,
    db: Session = Depends(get_db),
):
    user = jsonable_encoder(
        crud.delete_user(
            db=db,
            user_id=user_id,
        )
    )
    return JSONResponse(
        status_code=202,
        content=user,
    )


@router.patch(
    path='/{user_id}',
    response_model=pm.User,
    name='Patches one user',
    description='The endpoint patches a user and returns it',
    responses={
        404: {'model': ModelError},
        422: {'model': ModelError},
    }
)
def patch_user(
    user_id: str,
    user_model: pm.UserUpdate,
    db: Session = Depends(get_db),

):

    user = jsonable_encoder(
        crud.patch_user(
            db=db,
            user_model=user_model,
            user_id=user_id,
        )
    )
    return JSONResponse(
        content=user,
    )
