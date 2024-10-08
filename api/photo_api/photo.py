from fastapi import (APIRouter, Request,
                     Body, UploadFile, File)
import random

photo_router = APIRouter(prefix="/photo", tags=["Фотки"])
# первый вариант
@photo_router.post("/add_photo")
async def add_photo(post_id: int,
                    photo_file: UploadFile = File(...)):
    file_id = random.randint(1, 1000000000)
    if photo_file:
        with open(f"database/photos/photo_{file_id}_{post_id}.txt", "wb") as photo:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)
        return {"status": 1, "message": "успешно загружено"}
    return {"status": 0, "message": "ошибка загрузки"}
from fastapi import (APIRouter, Request,
                     Body, UploadFile, File)
import random

photo_router = APIRouter(prefix="/photo", tags=["Фотки"])
# второй вариант
@photo_router.post("/add_photo2")
async def add_photo(post_id: int,
                    photo_file: UploadFile = File(...)):
    file_id = random.randint(1, 1000000000)
    if photo_file:
        photo = open(f"database/photos/photo_{file_id}_{post_id}.txt", "wb")
        try:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)
        finally:
            photo.close()
        return {"status": 1, "message": "успешно загружено"}
    return {"status": 0, "message": "ошибка загрузки"}




