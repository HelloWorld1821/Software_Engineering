from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import (
   administrator_api, run_api, user_api
)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3100"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(administrator_api.router)
app.include_router(user_api.router)
app.include_router(run_api.router)