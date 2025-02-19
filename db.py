import os
import pyodbc
from fastapi import HTTPException

# ✅ Load environment variable to determine environment (default: local)
ENV = os.getenv("APP_ENV", "local")  # Set this variable in production

CONNECTION_STRINGS = {
    "local": (
        "DRIVER={SQL Server};"
        "SERVER=.\\SQLEXPRESS;"  # Local SQL Server
        "DATABASE=AdventureWorks2016;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=True;"
    ),
    "production": (
        "DRIVER={SQL Server};"
        "SERVER=your-production-server-name;"  # Replace with actual production server
        "DATABASE=AdventureWorks2016;"
        "UID=your_username;"  # Use SQL authentication in production
        "PWD=your_password;"  # Avoid hardcoding passwords; use env variables instead
        "TrustServerCertificate=True;"
    ),
}

# ✅ Select the correct connection string
conn_str = CONNECTION_STRINGS.get(ENV, CONNECTION_STRINGS["local"])

def get_db_connection():
    '''Return a database connection'''
    try:
        conn = pyodbc.connect(conn_str)
        return conn
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        raise HTTPException(status_code=500, detail=f"❌ Database connection failed: {e}")
        return None