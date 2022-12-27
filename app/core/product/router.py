from fastapi import FastAPI, HTTPException, Response, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import utils, schemas, database, models, oauth2

from sqlalchemy import func

router = APIRouter()


@router.post("/category", status_code=201, response_model = schemas.ProductCategoryReturn)
async def create_product_category(product_category: schemas.ProductCategoryCreate, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    product_category = models.Product_Category(user_id=current_user.id, **product_category.dict())
    db.add(product_category)
    db.commit()
    db.refresh(product_category)

    return product_category


@router.get("/category", response_model = List[schemas.ProductCategoryReturn])
async def get_product_categoryes(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    product_categoryes = db.query(models.Product_Category).filter(models.Product_Category.user_id == current_user.id).all()
    return product_categoryes


@router.get("/category/{id}", response_model = schemas.ProductCategoryReturn)
async def get_product_category(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    product_category = db.query(models.Product_Category).filter(models.Product_Category.id == id and models.Product_Category.user_id == current_user.id).first()
    if not product_category:
        raise HTTPException(status_code=404, detail=f"product_category with id: {id} was not found!")
    return product_category


@router.put("/category/{id}", status_code=201)
async def update_product_category(id: int, updated_product_category: schemas.ProductCategoryCreate, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    query = db.query(models.Product_Category).filter(models.Product_Category.id == id)
    product_category = query.first()
    if not product_category:
        raise HTTPException(status_code=404, detail=f"product_category with id: {id} was not found!")

    if product_category.user_id != current_user.id:
        raise HTTPException(status_code=403, detail=f"product_category with ID: {id} is not belong to this user")

    query.update({**updated_product_category.dict()}, synchronize_session = False)
    db.commit()
    update_product_category = query.first()
    return updated_product_category


@router.delete("/category/{id}", status_code=204)
async def delete_product_category(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    query = db.query(models.Product_Category).filter(models.Product_Category.id == id)
    product_category = query.first()
    if not product_category:
        raise HTTPException(status_code=404, detail=f"product_category with id: {id} was not found!")

    if product_category.user_id != current_user.id:
        raise HTTPException(status_code=403, detail=f"product_category with ID: {id} is not belong to this user")

    query.delete(synchronize_session = False)
    db.commit()
    return Response(status_code=204)


@router.post("/", status_code=201, response_model = schemas.ProductReturn)
async def create_payment(product: schemas.ProductCreate, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    product = models.Product(user_id=current_user.id, **product.dict())
    db.add(product)
    db.commit()
    db.refresh(product)

    return product

@router.get("/", response_model = List[schemas.ProductReturn])
async def get_payments(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    payments = db.query(models.Product).filter(models.Product.user_id == current_user.id).all()
    return payments


@router.get("/{id}", response_model = schemas.ProductReturn)
async def get_payment(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    product = db.query(models.Product).filter(models.Product.id == id and models.Product.user_id == current_user.id).first()
    if not product:
        raise HTTPException(status_code=404, detail=f"product with id: {id} was not found!")
    return product


@router.put("/{id}", status_code=201)
async def update_payment(id: int, updated_payment: schemas.ProductCreate, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    query = db.query(models.Product).filter(models.Product.id == id)
    product = query.first()
    if not product:
        raise HTTPException(status_code=404, detail=f"product with id: {id} was not found!")

    if product.user_id != current_user.id:
        raise HTTPException(status_code=403, detail=f"product with ID: {id} is not belong to this user")

    query.update({**updated_payment.dict()}, synchronize_session = False)
    db.commit()
    update_payment = query.first()
    return updated_payment


@router.delete("/{id}", status_code=204)
async def delete_payment(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    query = db.query(models.Product).filter(models.Product.id == id)
    product = query.first()
    if not product:
        raise HTTPException(status_code=404, detail=f"product with id: {id} was not found!")

    if product.user_id != current_user.id:
        raise HTTPException(status_code=403, detail=f"product with ID: {id} is not belong to this user")

    query.delete(synchronize_session = False)
    db.commit()
    return Response(status_code=204)