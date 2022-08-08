from pydantic import BaseModel


class ModelError(BaseModel):
    error: str
    message: str
    detail: str

    class Config:
        schema_extra = {
            'example': {
                'error': 'error-code',
                'message': 'Brief description',
                'detail': 'Long description',
            }
        }
