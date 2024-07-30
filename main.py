from fastapi import FastAPI
from api.photo_api.photo import photo_router
app = FastAPI(docs_url="/")

app.include_router(photo_router)
