from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.drum import router as drumRouter
from routes.pokemon import router as pokemonRouter
from database.connection import engine
from database import models
from origins import origins

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(CORSMiddleware,
                    allow_credentials=True,
                    allow_origins=origins,
                    allow_methods=["*"],
                    allow_headers=["*"])

app.include_router(drumRouter)
app.include_router(pokemonRouter)



@app.get("/")
def printHelloWorld():
    return {"message": "Hello"}


@app.get("/cartitems")
def returnCartItems():
    return {"data": ["item1", "item2", "item3"]}

# @app.get("/cart/{name}")
# def returnCart(name):
#     return {"cart": "1" + name}