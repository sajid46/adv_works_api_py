from fastapi import HTTPException
import pyodbc

const_str = (
    "DRIVER={SQL Server};"
    "SERVER=.\\SQLExpress;"
    "DATABASE=AdventureWorks2016;"
    "Trusted_Connection=yes;"
    "TrustedServerCertification=True;"
)

def get_db_connection():
    '''Return a database connection'''
    try:
        conn = pyodbc.connect(const_str)
        return conn
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        raise HTTPException(status_code=500, detail=f"❌ Database connection failed: {e}")
        return None