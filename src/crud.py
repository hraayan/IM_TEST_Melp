
from sqlalchemy.orm import Session
from models import Restaurant
from schema import RestaurantSchema

#obtener todos los restaurantes
def get_restaurants(db:Session, skip:int=0, limit: int=100):
    return db.query(Restaurant).offset(skip).limit(limit).all()

# obtener un restaurante por id
def get_restaurant_by_id(db:Session, restaurant_id: str):
    return db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()

#crear un restaurante
def create_restaurant(db:Session, restaurant: RestaurantSchema):
    _restaurant = Restaurant(id = restaurant.id, rating = restaurant.rating,
                            name = restaurant.name,
                            site = restaurant.site,
                            email = restaurant.email,
                            phone = restaurant.phone,
                            street = restaurant.street,
                            city = restaurant.city,
                            state = restaurant.state,
                            lat = restaurant.lat,
                            lng = restaurant.lng)
    

    db.add(_restaurant)
    db.commit()
    db.refresh(_restaurant)
    return _restaurant

#eliminar un restaurante por id
def remove_restaurant(db:Session, restaurant_id:str):
    _restaurant = get_restaurant_by_id(db=db, restaurant_id= restaurant_id)
    db.delete(_restaurant)
    db.commit()
# actualizar un restaurante por id
def update_restaurant(db:Session, restaurant_id: str ,name: str,
                        rating: int,
                        site: str,
                        email: str,
                        phone: str,
                        street: str,
                        city: str,
                        state: str,
                        lat: float,
                        lng: float):
    _restaurant = get_restaurant_by_id(db=db, restaurant_id= restaurant_id)
    _restaurant.name = name
    _restaurant.rating = rating
    _restaurant.site = site
    _restaurant.email = email
    _restaurant.phone = phone
    _restaurant.street = street
    _restaurant.city = city
    _restaurant.state = state
    _restaurant.lat = lat
    _restaurant.lng = lng

    db.commit()
    db.refresh(_restaurant)
    return _restaurant