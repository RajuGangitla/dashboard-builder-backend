from fastapi import FastAPI
from dotenv import load_dotenv
from routers import query

app=FastAPI()

app.include_router(query.router)