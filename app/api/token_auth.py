from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.utils import TokenUtils
token_router=APIRouter()
@token_router.get("/token")
def print_token():
    access_token=TokenUtils.create_access_token("123456")
    return JSONResponse(
        content={
            "message":f"Your token is {access_token}",
            "statusCode":200
        }
    )
