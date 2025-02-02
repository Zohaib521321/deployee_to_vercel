from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

class TokenUtils:
    SECRET_KEY = "your_secret_key"
    ALGORITHM = "HS256"
    TOKEN_EXPIRE_DAYS = 30  # Token expires in 30 days

    @staticmethod
    def create_access_token(uid: str):
        expire = datetime.utcnow() + timedelta(days=TokenUtils.TOKEN_EXPIRE_DAYS)
        encode = {
            "id": uid,
            "exp": expire
        }
        return jwt.encode(encode, TokenUtils.SECRET_KEY, TokenUtils.ALGORITHM)

    @staticmethod
    def verify_access_token(token: str):
        try:
            payload = jwt.decode(token, TokenUtils.SECRET_KEY, algorithms=[TokenUtils.ALGORITHM])
            uid = payload.get("id")
            if not uid:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
            return uid  
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token",
                headers={"WWW-Authenticate": "Bearer"},
            )

security = HTTPBearer()

def protected_route(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    return TokenUtils.verify_access_token(token)  # Returns UID
