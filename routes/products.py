from fastapi import APIRouter, HTTPException
import pyodbc
from db import get_db_connection

router = APIRouter()

@router.get("/products")
def get_products():
    '''Fetch all products from Production.Product'''
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    try:
        cursor = conn.cursor()
        query = "SELECT TOP 10 ProductID, Name, ProductNumber, ListPrice FROM Production.Product"
        cursor.execute(query)

        products = []
        for row in cursor.fetchall():
            products.append({
                "ProductID": row.ProductID,
                "Name": row.Name,
                "ProductNumber": row.ProductNumber,
                "ListPrice": row.ListPrice
            })

        cursor.close()
        conn.close()

        return {"products": products}
    
    except Exception as e:
        print(f"❌ SQL Query error: {e}")
        raise HTTPException(status_code=500, detail=f"❌ SQL Query error: {e}")