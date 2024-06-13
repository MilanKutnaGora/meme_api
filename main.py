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

# Создание модели мема
Base = declarative_base()

class Meme(Base):
    __tablename__ = 'memes'
    id = Column(Integer, primary_key=True)
    image = Column(String)
    text = Column(String)

# Создание API для мемов
@app.get("/memes", response_model=List[Meme])
async def get_memes(page: int = 1, size: int = 10):
    memes = session.query(Meme).offset((page - 1) * size).limit(size).all()
    return memes

@app.get("/memes/{id}", response_model=Meme)
async def get_meme(id: int):
    meme = session.query(Meme).filter(Meme.id == id).first()
    if meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return meme

@app.post("/memes", response_model=Meme)
async def create_meme(meme: Meme):
    session.add(meme)
    session.commit()
    return meme

@app.put("/memes/{id}", response_model=Meme)
async def update_meme(id: int, meme: Meme):
    meme_to_update = session.query(Meme).filter(Meme.id == id).first()
    if meme_to_update is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    meme_to_update.image = meme.image
    meme_to_update.text = meme.text
    session.commit()
    return meme_to_update

@app.delete("/memes/{id}")
async def delete_meme(id: int):
    meme_to_delete = session.query(Meme).filter(Meme.id == id).first()
    if meme_to_delete is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    session.delete(meme_to_delete)
    session.commit()
    return JSONResponse(status_code=204)
