from fastapi import APIRouter

from .auth.router import router as auth_router
from .user.router import router as user_router
from .product.router import router as product_router

router = APIRouter(prefix="/api")

router.include_router(
    auth_router, 
    prefix="/auth", 
    tags=["Auth"]
)

router.include_router(
    user_router, 
    prefix="/user", 
    tags=["User Infos"]
)

router.include_router(
    product_router, 
    prefix="/product", 
    tags=["Product Infos"]
)