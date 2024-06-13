from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.encoders import jsonable_encoder
from typing import List
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# Создание базы данных
engine = create_engine('postgresql://user:password@localhost:5432/meme_db')
Session = sessionmaker(bind=engine)
session = Session()

# Создание модели медиа-фаила
Base = declarative_base()

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    file_path = Column(String)

# Создание API для медиа-фаилов
@app.post("/media", response_model=Media)
async def upload_media(file: bytes):
    media = Media(file_path='path/to/file')
    session.add(media)
    session.commit()
    return media

@app.get("/media/{id}", response_model=Media)
async def get_media(id: int):
    media = session.query(Media).filter(Media.id == id).first()
    if media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    return media

@app.delete("/media/{id}")
async def delete_media(id: int):
    media_to_delete = session.query(Media).filter(Media.id == id).first()
    if media_to_delete is None:
        raise HTTPException(status_code=404, detail="Media not found")
    session.delete(media_to_delete)
    session.commit()
    return JSONResponse(status_code=204)