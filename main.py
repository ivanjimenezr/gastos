from fastapi import FastAPI

app = FastAPI()

@app.get("/hola/{nombre}")
def read_item(nombre: str):
 return {"message": f"Hola {nombre}, bienvenido a FastAPI"}
