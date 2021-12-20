#pip install fastapi
#pip install uvicorn

#uvicorn app:app --reload

from fastapi import FastAPI
from routes.mat import mat

app = FastAPI()

app.include_router(mat)