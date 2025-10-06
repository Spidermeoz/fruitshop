# app/main.py
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.db.session import SessionLocal
from app.models.product import Product

app = FastAPI(title="Fruit Shop")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def home(request: Request):
    db = SessionLocal()
    try:
        products = db.query(Product).all()
    finally:
        db.close()
    return templates.TemplateResponse("index.html", {"request": request, "products": products})
