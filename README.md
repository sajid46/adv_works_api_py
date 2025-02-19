## This API - SQL Server -> AdventureWorks2016

``` http://127.0.0.1:8000```

``` http://127.0.0.1:8000/welcome```

``` http://127.0.0.1:8000/products```

``` http://127.0.0.1:8000/docs  (swagger)```

## How to Switch Between Local & Production
### For Local Development (local Mode)
- No need to do anything! By default, it will use the local SQL Server .\\SQLEXPRESS.

### For Production (production Mode)
- Set an environment variable before running FastAPI:

🔹 On Windows (Command Prompt)

```sh
set APP_ENV=production
uvicorn app:app --reload ```

🔹 On Mac/Linux(Bash)

```sh
export APP_ENV=production
uvicorn app:app --reload ```

## Alternative: Use a .env File
If you prefer, you can use a .env file to store environment variables.

### Install python-dotenv

```pip install python-dotenv```

### Create a .env File
✅ Inside your project directory, create a file called .env:

```APP_ENV=production
DB_USER=your_username
DB_PASSWORD=your_password
DB_SERVER=your-production-server-name
```
### Modify db.py to Read .env Variables
```
from dotenv import load_dotenv
import os
import pyodbc

# ✅ Load .env file
load_dotenv()

# ✅ Detect Environment
ENV = os.getenv("APP_ENV", "local")

# ✅ Read credentials from .env
DB_USER = os.getenv("DB_USER", "your_local_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "your_local_password")
DB_SERVER = os.getenv("DB_SERVER", ".\\SQLEXPRESS")

# ✅ Define connection strings dynamically
if ENV == "production":
    conn_str = f"DRIVER={{SQL Server}};SERVER={DB_SERVER};DATABASE=AdventureWorks2016;UID={DB_USER};PWD={DB_PASSWORD};TrustServerCertificate=True;"
else:
    conn_str = "DRIVER={SQL Server};SERVER=.\\SQLEXPRESS;DATABASE=AdventureWorks2016;Trusted_Connection=yes;TrustServerCertificate=True;"

def get_db_connection():
    """Returns a database connection based on the selected environment."""
    try:
        conn = pyodbc.connect(conn_str)
        return conn
    except Exception as e:
        print(f"❌ Database Connection Failed: {e}")
        return None
```