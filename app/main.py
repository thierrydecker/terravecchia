from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exception import CustomException
from app.routers import users
from app.routers import root
from app.config.urls import app_prefix
from app.middlewares.traces import trace_activity

app = FastAPI(
    docs_url=f"{app_prefix}/docs",
    redoc_url=f"{app_prefix}/redoc",
)

app.include_router(users.router)
app.include_router(root.router)


@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.content,
    )


@app.middleware('http')
async def activity_logging(request: Request, call_next):
    response = await call_next(request)
    await trace_activity(request=request, response=response)
    return response
