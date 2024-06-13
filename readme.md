Тестовое задание: Python Developer

Разработайте веб-приложение на Python, используя FastAPI, которое предоставляет API для работы с коллекцией мемов. Приложение должно состоять из двух сервисов: сервис с публичным API с бизнес-логикой и сервис для работы с медиа-файлами, используя S3-совместимое хранилище (н-р, MinIO).     

Функциональность:

●  GET /memes: Получить список всех мемов (с пагинацией).

●  GET /memes/{id}: Получить конкретный мем по его ID.

●  POST /memes: Добавить новый мем (с картинкой и текстом).

●  PUT /memes/{id}: Обновить существующий мем.                                        

●  DELETE /memes/{id}: Удалить мем. 

Требования:                          

●  Используйте реляционную СУБД для хранения данных.

●  Обеспечьте обработку ошибок и валидацию входных данных.

●  Используйте Swagger/OpenAPI для документирования API.

●  Напишите хотя бы несколько unit-тестов для проверки основной      функциональности.

●  Напишите Readme, из которого понятна функциональность проекта и инструкция по локальному запуску для разработки.

●  Проект должен состоять минимум из: 1 сервис с публичным API, 1 сервис с приватным API для изображений, 1 сервис СУБД, 1 сервис S3-storage.

●  Напишите docker-compose.yml для запуска проекта.

# Meme API

## Overview

Meme API is a RESTful API for managing memes.

## Endpoints

### GET /memes

* Returns a list of all memes.
* Supports pagination.

### GET /memes/{id}

* Returns a specific meme by its ID.
* Returns a 404 if the meme is not found.

### POST /memes

* Creates a new meme.
* Requires a JSON body with the meme's image and text.
* Returns the created meme.

### PUT /memes/{id}

* Updates a specific meme by its ID.
* Requires a JSON body with the updated meme's image and text.
* Returns the updated meme.

### DELETE /memes/{id}

* Deletes a specific meme by its ID.
* Returns a 204 if the meme is deleted.

## Media Service

### POST /media

* Uploads a media file.
* Returns the uploaded media.

### GET /media/{id}

* Returns a specific media file by its ID.
* Returns a 404 if the media is not found.

### DELETE /media/{id}

* Deletes a specific media file by its ID.
* Returns a 204 if the media is deleted.

## S3 Storage

### POST /s3

* Uploads a file to S3.
* Returns the uploaded file.

### GET /s3/{key}

* Returns a specific file from S3 by its key.
* Returns a 404 if the file is not found.

### Запуск тестов

`python -m unittest test.py`

### Запуск приложения

`docker-compose up`