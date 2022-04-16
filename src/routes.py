
from fastapi import APIRouter, HTTPException,Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schema import RestaurantSchema, Response
import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#obtener todos los restaurantes registrados
@router.get("/")
async def get_restaurants(skip: int = 0, limit: int =100 ,db:Session = Depends(get_db)):
    _restaurant = crud.get_restaurants(db,skip, limit)
    return Response(code=200,status="Ok", message="Seccess Fetch all restaurants", result=_restaurant)

#buscar un restaurante por id
@router.get("/{id}")
async def get_by_id(id:str, db: Session = Depends(get_db)):
    _restaurant = crud.get_restaurant_by_id(db, id)
    return Response(code=200, status="Ok", message="Success Fetch data", result=_restaurant).dict(exclude_none=True)

#crear un restaurante
@router.post('/')
async def create(request:RestaurantSchema, db: Session = Depends(get_db)):
    print("llegada")
    crud.create_restaurant(db,restaurant = request)
    return Response(code=200, status='Ok', message="Restaurant created successfylly").dict(exclude_none=True)

#Actualizar un restaurante por id
@router.put("/{id}")
async def update_restaurant(request:RestaurantSchema, db: Session = Depends(get_db)):
    _restaurant = crud.update_restaurant(db, restaurant_id= request.id,
                            name= request.name,
                            rating= request.rating,
                            site = request.site,
                            email = request.email,
                            phone = request.phone,
                            street = request.street,
                            city = request.city,
                            state = request.state,
                            lat = request.lat,
                            lng = request.lng)
                        
    return Response(code=200, status="Ok", message="Successfully update restaurant", result=_restaurant)

#eliminar un restaurante, busqueda por id
@router.delete("/{id}")
async def delete(id: str, db: Session =  Depends(get_db)):
    crud.remove_restaurant(db, restaurant_id= id)
    return Response(code=200, status="Ok", message="Succesfully delete data").dict(exclude_none=True)