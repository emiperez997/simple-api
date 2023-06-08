from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from utils.jwt_manager import validate_token
from jwt.exceptions import ExpiredSignatureError

# Middleware
class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        try:
          data = validate_token(auth.credentials)
          if data['email'] != "admin@gmail.com":
              raise HTTPException(status_code=403, detail="Forbidden")
        except ExpiredSignatureError:
          raise HTTPException(status_code=401, detail="Token has expired")