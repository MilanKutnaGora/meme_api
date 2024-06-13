from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.encoders import jsonable_encoder
from typing import List
from pydantic import BaseModel
from boto3 import client

app = FastAPI()

# Создание клиента S3
s3 = client('s3', aws_access_key_id='access_key', aws_secret_access_key='secret_key')

# Создание API для S3
@app.post("/s3", response_model=str)
async def upload_to_s3(file: bytes):
    s3.put_object(Body=file, Bucket='bucket_name', Key='file_name')
    return 'File uploaded successfully'

@app.get("/s3/{key}", response_model=str)
async def get_from_s3(key: str):
    try:
        response = s3.get_object(Bucket='bucket_name', Key=key)
        return response['Body'].read().decode('utf-8')
    except Exception as e:
        raise HTTPException(status_code=404, detail="File not found")