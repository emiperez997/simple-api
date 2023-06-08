from fastapi import APIRouter, Path, Body
from schemas.User import User
from utils.jwt_manager import create_token

@app.post('/api/login', tags=["Auth"], status_code=200)
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
      token: str = create_token(user.dict())
      return { "info": "Success", "data": token }
    return { "info": "Unauthorized", "data": user.dict() }