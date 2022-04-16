from fastapi import FastAPI
import models
from config import engine
from routes import router

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="MELP by Harry Baez")


@app.get('')
async def Home():
    return "Welcome"

app.include_router(router, prefix="/restaurants", tags=["Restaurantes"])


#uvicorn main:app --reload