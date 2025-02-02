from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import logging

# Configure Logging
logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

def setup_exception_handlers(app: FastAPI):
    @app.get("/")
    def default_route():
        return JSONResponse(
            status_code=200,
            content={"message": "Default route of our server", "statusCode": 200},
        )

    @app.exception_handler(400)
    async def bad_request_handler(request: Request, exc: HTTPException):
        logging.error(f"Bad Request: {request.url} - {exc.detail}")
        return JSONResponse(
            status_code=400,
            content={"message": "Bad Request. Please check your input.", "statusCode": 400},
        )

    @app.exception_handler(404)
    async def not_found_handler(request: Request, exc: HTTPException):
        logging.error(f"Route Not Found: {request.url}")
        return JSONResponse(
            status_code=404,
            content={"message": "Oops! The route does not exist.", "statusCode": 404},
        )

    @app.exception_handler(405)
    async def method_not_allowed_handler(request: Request, exc: HTTPException):
        logging.error(f"Method Not Allowed: {request.method} {request.url}")
        return JSONResponse(
            status_code=405,
            content={"message": "Method Not Allowed. Check your HTTP method.", "statusCode": 405},
        )

    @app.exception_handler(500)
    async def internal_server_error_handler(request: Request, exc: HTTPException):
        logging.error(f"Internal Server Error: {request.url} - {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={"message": "An unexpected error occurred.", "statusCode": 500},
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """
        Handle validation errors from Pydantic model validation.
        """
        # You can log the validation error details if needed
        logging.error(f"Validation Error: {exc.errors()} at {request.url}")
        error_messages = [error['msg'] for error in exc.errors()]

        return JSONResponse(
            status_code=422,
            content={
                "message": "Validation Error",
                "statusCode": 422,
                "errors": error_messages,
            }
        )
