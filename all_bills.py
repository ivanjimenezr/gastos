from fastapi import FastAPI, APIRouter
from pymongo import MongoClient

router = APIRouter()
app = FastAPI()

@router.get("/all_bills")
def process_data(): 
   return {"message": "all_bills, el proceso está en curso."}
