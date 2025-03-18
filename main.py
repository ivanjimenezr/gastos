from fastapi import FastAPI
from fastapi.responses import JSONResponse

import all_bills, add_bills

app = FastAPI()

app.include_router(all_bills.router, tags=["bills"])
app.include_router(add_bills.router, tags=["bills"])

@app.get("/")
async def read_root():
    return JSONResponse(content={"message": "Application is running"}, status_code=200)
