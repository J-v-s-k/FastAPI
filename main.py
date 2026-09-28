from fastapi import FastAPI,Depends
from models import Product
from database import SessionLocal,engine
import database_models
from sqlalchemy.orm import Session
app=FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "hello world"
products=[
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]

def init_db():
    db=SessionLocal()
    count=db.query(database_models.Product).count()
    if count==0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()
init_db()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/products")
def get_all_products(db:Session=Depends(get_db)):
    db_products=db.query(database_models.Product).all()
    return db_products

@app.get("/product/{id}")
def get_product(id :int,db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        return db_product

    return "Product Not Found"

@app.post("/product")
def add_product(product:Product,db:Session=Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/product")
def update_product(id:int,product:Product,db:Session=Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "product updated"
    else:
        return "No product found"

@app.delete("/product")
def delete_product(id:int,db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
            db.delete(db_product)
            db.commit()
    else:
        return "product not found"

