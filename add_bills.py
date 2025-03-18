from fastapi import FastAPI, APIRouter

router = APIRouter()
app = FastAPI()

examples_responses = {
    200: {
     "description": "Successful Response",
     "content": {
         "application/json": {
             "example": {"message": "Item created successfully", "item_id": 123}
         }
     },
 },
 402: {
     "description": "Validation Error",
     "content": {
         "application/json": {
             "example": {
                 "detail": [
                     {
                         "loc": ["body", "name"],
                         "msg": "field required",
                         "type": "value_error.missing"
                     }
                 ]
             }
         }
     },
 },
}

@router.post("/add_bills", responses=examples_responses)
def process_data(event): 
    print(f"event recibido:")
    print(event)
