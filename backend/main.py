from fastapi import FastAPI, Depends, Body, Path, Request # Server
from data.tasks import tasks # Data
from pydantic import BaseModel, Field # Types
from fastapi.responses import JSONResponse
from typing import Optional, List # Types

# Routes
from routes.task_router import task_router

# Auth
from utils.jwt_manager import create_token, validate_token
from schemas.JWTBearer import JWTBearer

# Schemas
from schemas.User import User

# Cors
from fastapi.middleware.cors import CORSMiddleware

# App
app = FastAPI()

# Routes
app.include_router(task_router)

# Middleware
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

app.title = 'Simple Task API with FastAPI'
app.description = 'Simple Task API with FastAPI'
app.version = '0.0.1'

@app.get('/api', tags=["Home"])
def index():
    return {'info': 'Welcome to Simple Task API with FastAPI'}