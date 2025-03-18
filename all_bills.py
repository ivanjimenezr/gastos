from fastapi import FastAPI, APIRouter

router = APIRouter()
app = FastAPI()

@router.post("/all_bills")
def process_data(): 
   return {"message": "all_bills, el proceso está en curso."}
