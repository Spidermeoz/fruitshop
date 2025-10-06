# app/models/product.py
from sqlalchemy import Column, Integer, String, Numeric, Text
from app.db.session import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    image_url = Column(Text)
    description = Column(Text)
