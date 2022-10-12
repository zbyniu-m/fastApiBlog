from fastapi import FastAPI
from database import models
from database.database import engine
from rooters import post


app = FastAPI()
app.include_router(post.router)


models.Base.metadata.create_all(engine)
