from typing import List
from fastapi import FastAPI, HTTPException, Response, Depends

from sqlalchemy.orm import Session

from .core import models, database, routers
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
async def root():
    return {"message": "E-commerce app"}

app.include_router(routers.router)


