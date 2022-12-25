from fastapi import FastAPI, HTTPException, Response, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import utils, schemas, database, models, oauth2


router = APIRouter()

@router.post("/", status_code=201, response_model = schemas.UserReturn)
async def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):

    user.password = utils.hash(user.password)

    user = models.User(**user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.put("/", status_code=201, response_model = schemas.UserReturn)
async def update_user(updated_user: schemas.UserCreate, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    query = db.query(models.User).filter(models.User.id == current_user.id)

    updated_user.password = utils.hash(updated_user.password)

    query.update({**updated_user.dict()}, synchronize_session = False)
    db.commit()
    user = query.first()
    return user


@router.post("/address", status_code=201, response_model = schemas.AddressReturn)
async def create_address(address: schemas.AddressCreate, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    address = models.Address(user_id=current_user.id, **address.dict())
    db.add(address)
    db.commit()
    db.refresh(address)

    return address


@router.get("/address", response_model = List[schemas.AddressReturn])
async def get_addresses(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    addresses = db.query(models.Address).filter(models.Address.user_id == current_user.id).all()
    return addresses


@router.get("/address/{id}", response_model = schemas.AddressReturn)
async def get_address(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    address = db.query(models.Address).filter(models.Address.id == id and models.Address.user_id == current_user.id).first()
    if not address:
        raise HTTPException(status_code=404, detail=f"address with id: {id} was not found!")
    return address


@router.put("/address/{id}", status_code=201)
async def update_address(id: int, updated_address: schemas.AddressCreate, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    query = db.query(models.Address).filter(models.Address.id == id)
    address = query.first()
    if not address:
        raise HTTPException(status_code=404, detail=f"Address with id: {id} was not found!")

    if address.user_id != current_user.id:
        raise HTTPException(status_code=403, detail=f"address with ID: {id} is not belong to this user")

    query.update({**updated_address.dict()}, synchronize_session = False)
    db.commit()
    update_address = query.first()
    return updated_address


@router.delete("/address/{id}", status_code=204)
async def delete_address(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    query = db.query(models.Address).filter(models.Address.id == id)
    address = query.first()
    if not address:
        raise HTTPException(status_code=404, detail=f"Address with id: {id} was not found!")

    if address.user_id != current_user.id:
        raise HTTPException(status_code=403, detail=f"address with ID: {id} is not belong to this user")

    query.delete(synchronize_session = False)
    db.commit()
    return Response(status_code=204)


@router.post("/payment", status_code=201, response_model = schemas.PaymentReturn)
async def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    payment = models.Payment(user_id=current_user.id, **payment.dict())
    db.add(payment)
    db.commit()
    db.refresh(payment)

    return payment

@router.get("/payment", response_model = List[schemas.PaymentReturn])
async def get_payments(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    payments = db.query(models.Payment).filter(models.Payment.user_id == current_user.id).all()
    return payments


@router.get("/payment/{id}", response_model = schemas.PaymentReturn)
async def get_payment(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    payment = db.query(models.Payment).filter(models.Payment.id == id and models.Payment.user_id == current_user.id).first()
    if not payment:
        raise HTTPException(status_code=404, detail=f"payment with id: {id} was not found!")
    return payment


@router.put("/payment/{id}", status_code=201)
async def update_payment(id: int, updated_payment: schemas.PaymentCreate, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    query = db.query(models.Payment).filter(models.Payment.id == id)
    payment = query.first()
    if not payment:
        raise HTTPException(status_code=404, detail=f"payment with id: {id} was not found!")

    if payment.user_id != current_user.id:
        raise HTTPException(status_code=403, detail=f"payment with ID: {id} is not belong to this user")

    query.update({**updated_payment.dict()}, synchronize_session = False)
    db.commit()
    update_payment = query.first()
    return updated_payment


@router.delete("/payment/{id}", status_code=204)
async def delete_payment(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    query = db.query(models.Payment).filter(models.Payment.id == id)
    payment = query.first()
    if not payment:
        raise HTTPException(status_code=404, detail=f"payment with id: {id} was not found!")

    if payment.user_id != current_user.id:
        raise HTTPException(status_code=403, detail=f"payment with ID: {id} is not belong to this user")

    query.delete(synchronize_session = False)
    db.commit()
    return Response(status_code=204)