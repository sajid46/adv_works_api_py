from fastapi import APIRouter, HTTPException
import pyodbc
from db import get_db_connection

router = APIRouter()

@router.get("/")
def welcome():
    '''Welcome'''
    return {"message":"Welcome AdventureWorks2016 API"}