from fastapi import APIRouter , BackgroundTasks
from fastapi.responses import JSONResponse
from app.models import AuthenticationModel
import time
from app.utils import protected_route,Depends

router=APIRouter()
def send_email():
    time.sleep(5)
    print("Sending email in the background")
@router.get("/")
def default_auth():
    return JSONResponse(
        status_code=200,
        content={
            "message":"Default Route for the auth",
            "statusCode":200
        }
    )
@router.post("/signup")
def signup_user(user:AuthenticationModel):
    return JSONResponse(
        status_code=200,
        content={
            "message":"successfully signup",
            "statusCode":200,
            "data":user.model_dump()
        }
    )
@router.get("/sendEmailInBackground")
async def send_email_in_background(task:BackgroundTasks):
    task.add_task(send_email)
    return JSONResponse(
        status_code=200,
        content={
            "message":"Email will be sent in the background",
            "statusCode":200
        }
    )
@router.get("/protectedRoute")
def protected_route(uid: str = Depends(protected_route)):
    return JSONResponse(
        content={
            "message":f"Accessed protected route with uid: {uid}",
            "statusCode":200,
        },
        status_code=200
    )