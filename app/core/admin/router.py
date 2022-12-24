from fastapi import FastAPI, HTTPException, Response, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import utils, schemas, database, models, oauth2

from sqlalchemy import func

router = APIRouter()