from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import routes_custom
from src.models import models
from config.database import engine


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


# Include routes Blog
app.include_router(routes_custom)

# Create Database
models.Base.metadata.create_all(engine)




