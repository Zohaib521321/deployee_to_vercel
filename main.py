from fastapi import FastAPI
from app.api import router as auth_router,token_router 
from app.exception import setup_exception_handlers
from app.core.cors import setup_cors
import uvicorn

app=FastAPI()
setup_cors(app)
setup_exception_handlers(app)

# ✅ Include API Routes
app.include_router(auth_router, prefix="/api/auth", tags=["Authentication"])
app.include_router(token_router, prefix="/api/token", tags=["Token"])

# ✅ Start FastAPI Server
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
