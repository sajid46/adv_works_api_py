from fastapi import FastAPI, HTTPException
from routes import products, welcome
import pyodbc

app = FastAPI()
    
app.include_router(welcome.router)
app.include_router(products.router)
