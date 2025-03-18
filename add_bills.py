from fastapi import FastAPI, APIRouter

router = APIRouter()
app = FastAPI()

@router.post("/add_bills", responses=examples_responses)
def process_data(event): 
    print(f"event recibido:")
    print(event)
